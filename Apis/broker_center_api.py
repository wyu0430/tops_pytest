# coding=utf-8

from pithy import request, response

from common import public_configure
from common.utils import sign, get_md5

host = public_configure.gateway_url_test


class BrokerCenter(object):
    def __init__(self):
        self.base_url = host

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
        uk = res['Data']['UserToken']
        broker_id = res['Data']['BrokerID']
        return broker_id

    @sign()
    @request( method='get' )
    def share_recommend_broker(self, brokerId, brokerPhone):
        """H5领取好友邀请礼包接口"""
        url = '/broker-center-api/v1/share/recommendBroker/{}'.format( brokerId )
        params ={
            'brokerPhone': '86' + brokerPhone
        }
        return response( url=url, params=params )

    @sign()
    @request( url='/oauth/SignIn/SendPhoneCode', method='post' )
    def send_phone_code(self, phone):
        """获取注册验证码接口"""
        data = {
                "appcode": 'app_broker',
                "phone": '86' + phone
        }
        return response( data=data )

    @sign()
    @request( url='/oauth/SignIn/v3/SignInPhone', method='post' )
    def sign_in_phone(self, code, phone, password):
        """提交验证码接口"""
        data = {
            "app": 'app_broker',
            "code": code,
            "phone": '86' + phone,
            "password": get_md5(password)
        }
        return response( data=data )



    @sign()
    @request( method='get' )
    def outlet_code(self, shop_code):
        """查询门店是否存在"""
        url = '/broker-saas-api/v1/outlet/code/{}'.format( shop_code )
        return response( url=url )


    @sign()
    @request( url='/broker-center-api/v1/broker/bindBrokerCompany', method='put' )
    def bind_broker_company(self, phone, outletCode):
        """绑定门店"""
        json = {
            "brokerType": 2,
            "brokerName": 'test',
            "phone": '86' + phone,
            "longitude": 120.1839549732338,
            "latitude": 30.22223876236945,
            "outletCode": outletCode
        }
        return response( json=json )


    @sign()
    @request( url='/broker-center-api/v1/brokershare/getBrokerBagList', method='get' )
    def broker_share_get_broker_bag_list(self):
        """获取注册礼包"""
        return response()

if __name__ == '__main__':
    phone = '18999990003'
    brokerId = 34108
    register = BrokerCenter()
    res = register.share_recommend_broker( brokerId, phone )
    json = res.json
    print(json)