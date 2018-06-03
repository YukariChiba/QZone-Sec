import find
import argparse
import db
import settings
from tqdm import *


def main_entry():
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', help='the qq numbers list you want to lookup',
                        dest='qq_list',
                        default=None,
                        required=True)
    parser.add_argument('-s', help='the start timestamp you want to spider',
                        dest='start_date',
                        default=settings.default_end_time)
    args = parser.parse_args()
    qq_list = []
    for qq in open(args.qq_list):
        qq = qq.replace('\n', '')
        if qq is not '':
            qq_list.append(qq)
    bar_list = tqdm(total=len(qq_list), position=1)
    i = 1
    for qq in qq_list:
        find.qzonesecret(qq, over_time=args.start_date)
        bar_list.update(1)
        bar_list.set_description("Item %i" % i)
        i += 1
    bar_list.close()
    db.db_close()


if __name__ == '__main__':
    main_entry()



