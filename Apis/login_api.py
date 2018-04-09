# coding=utf-8

from pithy import request

from common import public_configure
from common.utils import sign, get_md5

host = public_configure.gateway_url_ga


@sign()
@request(url=host + '/oauth/Authorization/Login', method='post' )
def login(username, password):
    json = {
        'agent': 'android',
        'appcode': 'app_broker',
        'loginName': username,
        'password': get_md5(password)
    }

    return {'json': json}


if __name__ == '__main__':
    login('15157163734', '147852' ).to_json()
