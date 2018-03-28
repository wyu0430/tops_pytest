# coding=utf-8

from pithy import request, response

from common import public_configure
from common.utils import sign, get_md5


class Customer( object ):
    def __init__(self):
        self.base_url = public_configure.gateway_url_ga

    @sign()
    @request( url='/oauth/Authorization/Login', method='post' )
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
        res = self.__login( username, password )
        ak = res.json['Data']['AccessToken']
        self.session.headers['Authorization'] = ak
        # uk = res['Data']['UserToken']
        # broker_id = res['Data']['BrokerID']
        return res

    @sign()
    @request( url='/broker-service-api/v1/customer/addEntity4App', method='post' )
    def add_customer(self, phone, customerName, gender, level):
        """添加客户接口"""
        json = {
            "brokerCustomerFormVO": {
                "brokerCustomerPhone": [{
                    "isPrimary": 1,
                    "phone": phone
                }],
                "clientId": 0,
                "customerId": 0,
                "customerName": customerName,
                "gender": gender,
                "isSecret": 0,
                "level": level,
                "sourceType": 10
            }
        }
        return response( json=json )

    @sign()
    @request(url='/broker-service-api/v1/customer', method='put')
    def edit_customer(self, customerId, customerName, phoneId, phone, gender, level):
        """编辑客户接口"""
        json = {
            "brokerCustomerPhone": [{
                "isPrimary": 1,
                "phone": phone,
                "phoneId": phoneId
            }],
            "clientId": "0",
            "customerId": customerId,
            "customerName": customerName,
            "gender": gender,
            "isSecret": 0,
            "level": level,
            "sourceType": 10
        }
        return response(json=json)

    @sign()
    @request( url='/broker-service-api/v1/customer/list', method='get' )
    def customer_list(self, sortType, filterType, pageIndex, pageSize):
        """客户列表接口"""
        params = {
            'sortType': sortType,
            'filterType': filterType,
            'pageIndex': pageIndex,
            'pageSize': pageSize
        }
        return response(params=params)

    @sign()
    @request( url='/broker-service-api/v1/customer/search', method='get' )
    def customer_search(self, query, pageIndex, pageSize):
        """客户搜索接口"""
        params = {
            'query': query,
            'pageIndex': pageIndex,
            'pageSize': pageSize
        }
        return response( params=params )

    @sign()
    @request( method='get' )
    def customer_detail(self, customer_id):
        """客户详情接口"""
        url = '/broker-service-api/v1/customer/customerDetail4App/{}'.format( customer_id )
        return response( url=url )

    @sign()
    @request( method='delete' )
    def delete_customer(self, customer_id):
        """删除客户"""
        url = '/broker-service-api/v1/customer/{}'.format( customer_id )
        return response( url=url )

    @sign()
    @request( url='/broker-service-api/v1/brokerHouseManage/submitApply', method='put' )
    def appointment_customer(self, applyType, bizTime, brokerId, buildingId, consultantId, customerId, orderNo,
                             recommendId, visitType):
        """提交申请接口"""
        json = {
            "applyRemark": "哈哈哈备注",
            "applyType": applyType,
            "bizTime": bizTime,
            "brokerId": brokerId,
            "buildingId": buildingId,
            "consultantId": consultantId,
            "customerId": customerId,
            "isOnBuilding": 1,
            "orderNo": orderNo,
            "recommendId": recommendId,
            "visitType": visitType
        }
        return response( json=json )

# if __name__ == '__main__':
#     customer = Customer()
#     customer.login('15157163734', '147852' )
#     print customer.customer_detail(82901).json
