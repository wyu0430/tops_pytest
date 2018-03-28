# coding=utf-8

from pithy import request, response, make_session

from common import public_configure
from common.utils import sign, get_md5

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import time

# http://activity.dev.apitops.com/activity/api/v1/swagger.json
class BrokerCompanyShop( object ):
    def __init__(self):
        self.base_url = public_configure.brokeroa_url_test
        self.session = make_session()

    def getcookie(self, username, password):
        """登录接口"""
        driver = webdriver.Chrome()
        driver.implicitly_wait( 3 )
        driver.maximize_window()
        driver.get( public_configure.bops_url_test )
        time.sleep( 3 )
        driver.find_element_by_id( 'loginName' ).send_keys( username )
        driver.find_element_by_id( 'password' ).send_keys( password )
        driver.find_element_by_id( 'btnLoginCRM' ).click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="side-menu"]/li[4]/a/span').click()
        time.sleep( 1 )
        driver.find_element_by_xpath(('//*[@id="side-menu"]/li[4]/ul/li[2]/a')).click()
        time.sleep( 3 )
        driver.get( 'http://brokeroa.test.apitops.com/broker-oa-web/api/v5/common-data/city-list?pageIndex=1&pageSize=100' )
        cookie_broker_oa_sid = driver.get_cookie('_broker_oa_sid')['value']
        cookie_tempToken = driver.get_cookie('tempToken')['value']
        print cookie_broker_oa_sid
        print cookie_tempToken
        Cookie = {'_broker_oa_sid': cookie_broker_oa_sid, 'tempToken': cookie_tempToken }
        driver.quit()
        self.session.headers['Cookie'] = str(Cookie)
        return {'_broker_oa_sid': cookie_broker_oa_sid, 'tempToken': cookie_tempToken }

    @request( url='/broker-oa-web/api/v5/common-data/city-list', method='get' )
    def get_city_list(self):
        """获取城市列表"""
        header = {
            'Referer':'http://broker-oa.apitops.com/template/brokerCompany/brokerCompanyShop.html?adminKid=118279&uk=0c38b3df-4066-4d41-93d3-0ae77e0e2293&ak=50a67fe8-f126-4572-aff7-56e7ffbe0f67'
        }
        params = {
            'pageIndex': 1,
            'pageSize': 100
        }

        return response(params=params, header = header)

# if __name__ == '__main__':
#     BrokerCompanyShop = BrokerCompanyShop()
#     print BrokerCompanyShop.getcookie('top', '123456' )
