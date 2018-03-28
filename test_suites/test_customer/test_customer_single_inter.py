# coding=utf-8
import unittest
import time
from Apis.customer_api import Customer
from common import public_configure

login_name = "15157163734"
password = "a1478520B"


class TestCustomerSingleInterface(unittest.TestCase):

    def test_login(self):
        """登录接口"""
        customer = Customer()
        res = customer.login( login_name, password )
        json = res.json
        code = res.status_code
        assert (json['Code'] == 0)
        assert (code == 200)
        assert (res.elapsed.seconds <= 3)

    def test_add_customer(self):
        """添加客户接口"""
        customer = Customer()
        customer.login( login_name, password )
        phone = public_configure.PublicConfigure.random_phone()
        customer_name = '自动化新增' + public_configure.PublicConfigure.random_name()
        res = customer.add_customer( phone, customer_name, 1, 2 )
        json = res.json
        code = res.status_code
        customer_id = json['Data']['customerId']
        assert (json['Code'] == 0)
        assert (code == 200)
        assert (res.elapsed.seconds <= 3)
        time.sleep( 1 )
        return customer_id

    def test_customer_detail(self):
        """客户详情接口"""
        customer = Customer()
        customer.login( login_name, password )
        res = customer.customer_detail( 82901 )
        json = res.json
        code = res.status_code
        assert (json['Code'] == 0)
        assert (code == 200)
        assert (res.elapsed.seconds <= 3)

    def test_edit_customer(self):
        """编辑客户接口"""
        customer = Customer()
        customer.login( login_name, password )
        customer_id = 82900
        phone_id = 59453
        phone = "86 14749375208"
        phone = phone.strip()
        customer_edit_name = "自动化编辑" + public_configure.PublicConfigure.random_name()
        res = customer.edit_customer( customer_id, customer_edit_name, phone_id, phone, 2, 1 )
        json = res.json
        code = res.status_code
        assert (json['Code'] == 0)
        assert (code == 200)
        assert (res.elapsed.seconds <= 3)

    def test_customer_list(self):
        """客户列表接口"""
        customer = Customer()
        customer.login( login_name, password )
        res = customer.customer_list( 1, 0, 1, 20 )
        json = res.json
        code = res.status_code
        assert (json['Code'] == 0)
        assert (code == 200)
        assert (res.elapsed.seconds <= 3)

    def test_customer_search(self):
        """客户查询接口"""
        customer = Customer()
        customer.login( login_name, password )
        search_query = '自动化'
        res = customer.customer_search( search_query, 1, 20 )
        json = res.json
        code = res.status_code
        assert (json['Code'] == 0)
        assert (code == 200)
        assert (res.elapsed.seconds <= 3)


    def test_delete_customer(self):
        """删除客户接口"""
        customer = Customer()
        customer.login( login_name, password )
        phone = public_configure.PublicConfigure.random_phone()
        customer_name = '自动化新增' + public_configure.PublicConfigure.random_name()
        res = customer.add_customer( phone, customer_name, 1, 2 )
        json = res.json
        code = res.status_code
        customer_id = json['Data']['customerId']
        assert (json['Code'] == 0)
        assert (code == 200)
        assert (res.elapsed.seconds <= 3)
        res = customer.delete_customer( customer_id )
        json = res.json
        code = res.status_code
        assert (json['Code'] == 0)
        assert (code == 200)
        assert (res.elapsed.seconds <= 3)

