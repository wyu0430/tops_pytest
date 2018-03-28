# coding=utf-8
import unittest
from Apis.broker_oa_api import BrokerCompanyShop



from common import public_configure

login_name = "top"
password = "123456"


class TestActiveQaCase( unittest.TestCase ):
    def test_active_qa_case(self):
        broker_company_shop = BrokerCompanyShop()
        broker_company_shop.getcookie( login_name, password )
        # 获取城市列表
        res = broker_company_shop.get_city_list()
        json = res.json
        assert json['Code'] == 0 and res.status_code == 200 and res.elapsed.seconds <= 3
