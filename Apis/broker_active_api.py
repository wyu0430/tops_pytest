# coding=utf-8

from pithy import request, response
from common import public_configure
from common.utils import sign, get_md5


# http://activity.dev.apitops.com/activity/api/v1/swagger.json
class ActiveQa( object ):
    def __init__(self):
        self.base_url = public_configure.active_url_test

    @sign()
    @request( url='http://gateway.test.apitops.com/oauth/Authorization/Login', method='post' )
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
        res = self.__login( username, password ).json
        ak = res['Data']['AccessToken']
        self.session.headers['Authorization'] = ak
        # uk = res['Data']['UserToken']
        # broker_id = res['Data']['BrokerID']
        return True

    @sign()
    @request( url='/activity/api/v1/broker/cd/season/player', method='get' )
    def get_season_player(self):
        """获取当前玩家信息"""
        return response()

    @sign()
    @request( url='/activity/api/v1/broker/cd/season/rank', method='get' )
    def get_active_rank(self, seasonId):
        """获取排行版"""
        params = {
            'seasonId': seasonId,
        }
        return response( params=params )

    @sign()
    @request(url='/activity/api/v1/broker/cd/season/gates', method='get')
    def get_season_gates(self):
        """获取当前赛季关卡信息"""
        return response()

    @sign()
    @request( url='/activity/api/v1/broker/cd/qa/question', method='get' )
    def get_question(self, gateId):
        """获取问题"""
        params = {
            'gateId': gateId
        }

        return response(params=params)

    @sign()
    @request( url='/activity/api/v1/broker/cd/qa/quickQuestion', method='get' )
    def get_quict_question(self, gateId):
        """快速获取问题"""
        params = {
            'gateId': gateId
        }

        return response(params=params)

    @sign()
    @request(url='/activity/api/v1/broker/cd/qa/answer', method='post')
    def post_answer(self,subjectOrder, subjectId, submitAnswerCode, gateId):
        """提交答案接口"""
        json = {
                  "subjectOrder": subjectOrder,
                  "subjectId": subjectId,
                  "submitAnswerCode": submitAnswerCode,
                  "gateId": gateId
                }
        return response( json=json )

    @sign()
    @request( url='/activity/api/v1/broker/cd/season/share', method='post' )
    def confirm_season_share(self):
        """确认分享接口"""
        return response()

    @sign()
    @request( url='/activity/api/v1/cd/fi/bind', method='get' )
    def bind_player(self, inviteCode):
        """王者绑定接口"""
        params = {
            'inviteCode': inviteCode,
        }
        return response( params=params )

    @sign()
    @request( url='/activity/api/v1/cd/fi/bindInviteList', method='get' )
    def bind_list(self, pageIndex, pageSize):
        """王者绑定列表接口"""
        params = {
            'pageIndex': pageIndex,
            'pageSize': pageSize
        }
        return response( params=params )
# if __name__ == '__main__':
#     customer = Customer()
#     customer.login('15157163734', '147852' )
#     print customer.customer_detail(82901).json
