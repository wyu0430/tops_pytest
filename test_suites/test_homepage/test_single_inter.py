# coding=utf-8
import unittest
from Apis.homepage_api import HomePage


class Test_Single_Interface(unittest.TestCase):

    def test_get_landing_first_page(self):
        """首页get_landing_first_page"""
        homepage = HomePage()
        homepage.login('15157163734', '147852')
        city_id = 112
        res = homepage.get_landing_first_page(city_id)
        json = res.json
        code = res.status_code
        assert (json['Code'] == 0)
        assert (code == 200)
        assert (res.elapsed.seconds <= 3 )

    def test_new_poduct_list(self):
        """首页new_poduct_list"""
        homepage = HomePage()
        homepage.login('15157163734', '147852')
        city_id = 112
        res = homepage.new_product_list(city_id)
        json = res.json
        code = res.status_code
        assert (json['Code'] == 0)
        assert (code == 200)
        assert (res.elapsed.seconds <= 3 )

    def test_local_advert_list(self):
        """首页local_advert_list"""
        homepage=HomePage()
        homepage.login('15157163734', '147852')
        city_id = 112
        res = homepage.local_advert_list(city_id)
        json = res.json
        code = res.status_code
        assert (json['Code'] == 0)
        assert (code == 200)
        assert (res.elapsed.seconds <= 3 )

    def test_recommend_list(self):
        """首页recommend_list"""
        homepage = HomePage()
        homepage.login('15157163734', '147852')
        city_id = 112
        res = homepage.recommend_list(city_id)
        json = res.json
        code = res.status_code
        assert (json['Code'] == 0)
        assert (code == 200)
        assert (res.elapsed.seconds <= 3 )

    def test_start_advertising(self):
        """首页start_advertising"""
        homepage = HomePage()
        homepage.login('15157163734', '147852')
        res = homepage.start_advertising()
        json = res.json
        code = res.status_code
        assert (json['Code'] == 0)
        assert (code == 200)
        assert (res.elapsed.seconds <= 3)
