# coding=utf-8
import unittest
import time
from Apis.customer_api import Customer
from common import public_configure

login_name = "15157163734"
password = "a1478520B"


class TestCustomerCase( unittest.TestCase ):
    def test_customer_case1(self):
        """客户流程测试用例1"""
        # 添加客户
        customer = Customer()
        customer.login(login_name, password)
        phone = public_configure.PublicConfigure.random_phone()
        customer_name = '自动化新增' + public_configure.PublicConfigure.random_name()
        res = customer.add_customer( phone, customer_name, 1, 2 )
        json = res.json
        code = res.status_code
        customer_id = json['Data']['customerId']
        assert json['Code'] == 0 and code == 200 and res.elapsed.seconds <= 3
        time.sleep(1)
        # 客户详情
        res = customer.customer_detail(customer_id)
        json1 = res.json
        code = res.status_code
        phone_id = json1['Data']['brokerCustomerDTO']['brokerCustomerPhone'][0]['phoneId']
        assert json1['Code'] == 0 and code == 200 and res.elapsed.seconds <= 3
        assert json1['Data']['brokerCustomerDTO']['brokerCustomerPhone'][0]['phone'] == '86 '+phone
        assert json1['Data']['brokerCustomerDTO']['customerName'] == customer_name.decode('utf8')
        # 编辑客户
        phone_edit = "86 " + phone
        phone_edit = phone_edit.strip()
        customer_edit_name = "自动化编辑" + public_configure.PublicConfigure.random_name()
        res = customer.edit_customer( customer_id, customer_edit_name, phone_id, phone_edit, 2, 1 )
        json2 = res.json
        code = res.status_code
        assert (json2['Code'] == 0) and (code == 200) and (res.elapsed.seconds <= 3)
        # 客户详情
        res = customer.customer_detail(customer_id)
        json3 = res.json
        code = res.status_code
        assert json3['Code'] == 0 and code == 200 and res.elapsed.seconds <= 3
        assert json3['Data']['brokerCustomerDTO']['brokerCustomerPhone'][0]['phone'] == '86 ' + phone
        assert json3['Data']['brokerCustomerDTO']['customerName'] == customer_edit_name.decode('utf8')
        # 删除客户
        res = customer.delete_customer(customer_id)
        json4 = res.json
        code = res.status_code
        assert json4['Code'] == 0 and code == 200 and res.elapsed.seconds <= 3
        # 客户详情
        res = customer.customer_detail( customer_id )
        json5 = res.json
        code = res.status_code
        assert json5['Code'] == 3002 and code == 200 and res.elapsed.seconds <= 3
        assert '未在客户中心查询到相应客户'.decode('utf8') in json5['Message']

