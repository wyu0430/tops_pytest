# coding=utf-8

from pithy import request

from common import public_configure
from common.utils import sign, get_md5

host = public_configure.base_url


class HomePage(object):
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
        self.session.headers['AccessToken'] = ak
        # uk = res['Data']['UserToken']
        # broker_id = res['Data']['BrokerID']

    @sign()
    @request(url='/broker-service-api/v1/brokerLandingPage/getLandingFirstPage', method='get' )
    def get_landing_first_page(self, cityId):
        """首页getLandingFirstPage接口"""
        params = {
            'advertiseKey': 'advert5',
            'latitude': self.latitude,
            'longitude': self.longitude,
            'cityId': cityId
        }
        return {'params': params}

    @sign()
    @request( url='/broker-service-api/v1/brokerLandingPage/newProductList', method='get' )
    def new_product_list(self, cityId):
        """首页newProductList接口"""
        params = {
            'cityId': cityId
        }
        return {'params': params}

    @sign()
    @request( url='/broker-service-api/v1/brokerLandingPage/localAdvertList', method='get' )
    def local_advert_list(self, cityId):
        """首页localAdvertList接口"""
        params = {
            'advertiseKey': 'advert5',
            'cityId': cityId
        }
        return {'params': params}

    @sign()
    @request( url='/broker-service-api/v1/brokerLandingPage/recommendList', method='get' )
    def recommend_list(self, cityId):
        """首页recommendList接口"""
        params = {
            'latitude': self.latitude,
            'longitude': self.longitude,
            'cityId': cityId
        }
        return {'params': params}

    @sign()
    @request( url='/broker-service-api/v1/brokerLandingPage/startAdvertising', method='get' )
    def start_advertising(self):
        """首页startAdvertising接口"""
        params = {
            'advertiseKey': 'advert5',
        }
        return {'params': params}
