import json
import time
import urllib.parse
import urllib.request
import urllib.response
import datetime
import qzone_req
import settings
import db
import argparse
from color_out import *
from tqdm import *


def qzone_query(end_time, qq):
    response = urllib.request.urlopen(qzone_req.make_request(qq, end_time))
    s = response.read().decode('UTF-8')
    json_struct = json.loads(s)
    try:
        num_item = int(json_struct['data']['newcount']) - 1
    except KeyError:
        return 1
    if num_item is -1:
        return 1
    for node in json_struct['data']['all_feeds_data']:
        isself = node['singlefeed']['1']['user']['is_owner']
        text = node['singlefeed']['4']['summary']
        date = node['singlefeed']['0']['time']
        text = text.replace("\n", "<br>")
        text = text.replace("'", "''")
        if isself:
            timestr2 = datetime.datetime.fromtimestamp(date).strftime("%Y-%m-%d %H:%M:%S.%f")
            pr_red('[' + timestr2 + '] ' + '(' + qq + ') ' + text)
            if settings.insert_sql:
                db.sec_insert(node['singlefeed']['0']['feedskey'], str(date), qq, text)
        else:
            if settings.insert_sql:
                db.sec_insert_anon(node['singlefeed']['0']['feedskey'], str(date), text)
            if settings.show_unknown:
                timestr2 = datetime.datetime.fromtimestamp(date).strftime("%Y-%m-%d %H:%M:%S")
                tqdm.write('[' + timestr2 + '] ' + '(Unknown) ' + text)

    return int(json_struct['data']['all_feeds_data'][num_item]['singlefeed']['0']['time'])


def qzonesecret(qq, over_time=settings.default_end_time, force_update=False):
    t = int(time.time())
    last_time = db.get_last_time(qq)
    if not force_update:
        if last_time is not '0':
            over_time = last_time
    initial_t = t
    bar_item = tqdm(total=initial_t - int(over_time))
    tqdm.write("Start searching QQ " + qq)
    while t >= int(over_time):
        time_str = datetime.datetime.fromtimestamp(t).strftime("%Y-%m-%d")
        if settings.show_detail:
            tqdm.write("Outputing Data of QQ (" + qq + ') and time of ' + time_str)
        try:
            t = qzone_query(str(t), qq) - 1
            bar_item.set_description("T-stamp %s" % time_str)
            bar_item.update(initial_t - t)
            initial_t = t
        except Exception:
            time.sleep(5)
    db.update_id(qq, str(t))
    bar_item.close()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-q', help='the qq number you want to lookup',
                        dest='qq_num',
                        default=None,
                        required=True)
    parser.add_argument('-s', help='the start timestamp you want to spider',
                        dest='start_date',
                        default=settings.default_end_time)
    parser.add_argument('-F', help='whether the data is forced updated',
                        dest='force_update',
                        action='store_true',
                        default=False)
    args = parser.parse_args()
    qzonesecret(args.qq_num, over_time=args.start_date, force_update=(args.force_update is True))
    db.db_close()


if __name__ == '__main__':
    main()
