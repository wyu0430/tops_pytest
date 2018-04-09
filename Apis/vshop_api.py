# coding=utf-8

from pithy import request, response

from common import public_configure
from common.utils import sign, get_md5


class Vshop( object ):

    def __init__(self):
        self.base_url = public_configure.brokerService_url_ga
        self.latitude = 30.222176
        self.longitude = 120.183798

    @sign()
    @request(url=public_configure.gateway_url_test + '/oauth/Authorization/Login', method='post' )
    def __login(self, username, password):
        """登录接口"""
        json = {
            'agent': 'android',
            'appcode': 'app_broker',
            'loginName': username,
            'password': get_md5(password)
        }

        return {'json': json}

    def login(self, username, password):
        """获取登录基本参数"""
        res = self.__login(username, password).json
        ak = res['Data']['AccessToken']
        self.session.headers['Authorization'] = ak
        # uk = res['Data']['UserToken']
        # broker_id = res['Data']['BrokerID']

    @request(url='/broker-service-web/v1/building/buildingList', method='get')
    def buildingList(self, cityId):
        """楼盘列表接口"""
        params = {
            'cityId': cityId
        }
        return response( params=params )

    @request(url='/broker-service-web/v1/building/myBuildingListVdian', method='get')
    def myBuildingListVdian(self, category):
        """微店列表接口"""
        params = {
            'pageIndex': 1,
            'pageSize': 10,
            'category': category
        }
        return response(params=params)

    @request( url='/broker-service-web/v1/building/myVdian', method='get' )
    def myVdian(self, cityId):
        """我的微店接口"""
        params = {
            'cityId': cityId
        }
        return response(params=params)

    @request( url='/broker-service-web/v1/building/collectionBuildings', method='post' )
    def collectionBuildings(self, buildingCategory=[], buildingId=[]):
        """批量收藏楼盘接口"""
        json = [
                {
                    "buildingCategory": buildingCategory[0],
                    "buildingId": buildingId[0],
                    "isFavor": True
                },
                {
                    "buildingCategory": buildingCategory[1],
                    "buildingId": buildingId[1],
                    "isFavor": True
                }
            ]

        return response(json=json)
