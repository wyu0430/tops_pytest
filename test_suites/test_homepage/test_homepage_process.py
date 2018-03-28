# coding=utf-8
import unittest
from Apis.homepage_api import HomePage

MAX_RESPONSE_TIME = 3


class Test_Homepage_Process(unittest.TestCase):

    def test_homepage_process(self):
        """首页流程测试"""
        homepage=HomePage()
        homepage.login('15157163734', '147852')
        city_id = 112
        res1 = homepage.get_landing_first_page(city_id)
        json = res1.json
        code = res1.status_code
        assert (json['Code'] == 0)
        assert ( code == 200)
        assert ( res1.elapsed.seconds <= MAX_RESPONSE_TIME )

        res2 = homepage.new_product_list(city_id)
        json = res2.json
        code = res2.status_code
        assert (json['Code'] == 0)
        assert ( code == 200)
        assert ( res2.elapsed.seconds <= MAX_RESPONSE_TIME )

        res3 = homepage.recommend_list(city_id)
        json = res3.json
        code = res3.status_code
        assert (json['Code'] == 0)
        assert ( code == 200)
        assert ( res3.elapsed.seconds <= MAX_RESPONSE_TIME )
        res4 = homepage.local_advert_list(city_id)
        json = res4.json
        code = res4.status_code
        assert (json['Code'] == 0)
        assert ( code == 200)
        assert ( res4.elapsed.seconds <= MAX_RESPONSE_TIME )

        res5 = homepage.start_advertising()
        json = res5.json
        code = res5.status_code
        assert (json['Code'] == 0)
        assert (code == 200)
        assert (res5.elapsed.seconds <= MAX_RESPONSE_TIME)
