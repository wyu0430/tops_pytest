# coding=utf-8

from pithy import request, response

from common import public_configure
from common.utils import sign, get_md5

host = public_configure.gateway_url_test


class RedDog(object):
    def __init__(self):
        self.base_url = host
        self.latitude = 30.222176
        self.longitude = 120.183798

    @sign()
    @request(url='/oauth/Authorization/Login', method='post')
    def __login(self, username, password):
        """登录接口"""
        json = {
            'agent': 'android',
            'appcode': 'app_broker',
            'loginName': username,
            'password': get_md5( password )
        }

        return {'json': json}

    def login(self, username, password):
        """获取登录基本参数"""
        res = self.__login( username, password).json
        ak = res['Data']['AccessToken']
        self.session.headers['Authorization'] = ak
        # uk = res['Data']['UserToken']
        broker_id = res['Data']['BrokerID']
        return broker_id

    @sign()
    @request(url='/club-activity/reddog/button', method='get' )
    def reddog_button(self, brokerId):
        """判断红包雨时间接口"""
        params = {
            'brokerId': brokerId
        }
        return response( params=params )

    @sign()
    @request( url='/club-activity/reddog', method='get' )
    def reddog_get(self, brokerId, campaignId):
        """点击红包"""
        params = {
            'brokerId': brokerId,
            'campaignId': campaignId
        }
        return response( params=params )

    @sign()
    @request( url='/club-activity/reddog', method='post')
    def reddog_post(self, brokerId, campaignId, count):
        """提交成绩"""
        json = {
            'brokerId': brokerId,
            'campaignId': campaignId,
            'count': count
        }
        return response( json=json )


    @sign()
    @request(url='/club-activity/reddog/del', method='get')
    def reddog_del(self, campaignId):
        """redis数据清理"""
        params = {
            'campaignId': campaignId,
        }
        return response(params=params)


class TurntableLottery(object):
    """大转盘抽奖"""

    def __init__(self):
        self.base_url = public_configure.gateway_url_test



if __name__ == '__main__':
    tl = TurntableLottery()
    print tl.lottery_init(34108).content