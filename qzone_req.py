import urllib.parse
import urllib.request
import urllib.response
import settings
import random

values = {'t': str(random.uniform(0, 1)), 'g_tk': settings.g_tk}
data = urllib.parse.urlencode(values)
url_data = settings.api_url + "?" + data


def make_request(qq, end_time):
    postdata = {
        'refresh_type': '2',
        'relation_type:': '8',
        'uin': qq,
        'attach_info': 'endtime=' + end_time + '&offset=0&tlistsec=0&tlistusec=0&recomfeed='
    }
    form = urllib.parse.urlencode(postdata)
    request = urllib.request.Request(str(url_data), form.encode('UTF-8'))
    request.add_header('User-Agent',
                       'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, '
                       'like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36')
    request.add_header('Upgrade-Insecure-Requests', '1')
    request.add_header('Content-Type', 'application/x-www-form-urlencoded')
    request.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8')
    request.add_header('Cookie',
                       'RK=[...]; '
                       '__Q_w_s__QZN_TodoMsgCnt=1; '
                       'pgv_pvi=[...]; '
                       'pac_uid=1_' + qq + '; '
                       '__Q_w_s__appDataSeed=1; '
                       'QZ_FE_WEBP_SUPPORT=1; '
                       'cpu_performance_v8=49; '
                       '__Q_w_s_hat_seed=1; '
                       'eas_sid=[...]; '
                       'tvfe_boss_uuid=[...]; '
                       'ptui_loginuin=' + qq + '; '
                       'luin=o0' + qq + '; '
                       'lskey=[...]; '
                       'o_cookie=' + qq + '; '
                       'pgv_pvid=[...]; '
                       'ptisp=ctc; '
                       'ptcz=[...]; pt2gguin=o0' + qq + '; '
                       'uin=o0' + qq + '; '
                       'skey=[...]; '
                       'p_uin=o0' + qq + '; '
                       'p_skey=[...]; '
                       'pt4_token=[...]')
    return request
