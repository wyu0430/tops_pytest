# coding=utf-8
import unittest
import time
from Apis.customer_api import Customer
from Apis.club_activity_api import RedDog
import random

from common import public_configure

login_name = "15157163734"
# password = "147852"
password = "147852"


class TestRedDogCase( unittest.TestCase ):
    def test_get_reddog(self):
        """获取按钮"""
        reddog = RedDog()
        brroker_id = reddog.login( login_name, password )
        res = reddog.reddog_button( brroker_id )
        json = res.json
        assert json['Code'] == 0 and res.status_code == 200 and res.elapsed.seconds <= 3

    def test_reddog_del(self):
        """redis数据清理"""
        reddog = RedDog()
        res = reddog.reddog_del(123)
        json = res.json
        assert json['Code'] == 0 and res.status_code == 200 and res.elapsed.seconds <= 3

    def test_reddog(self):
        """红包雨测试用例"""
        count = random.uniform(80, 100)
        reddog = RedDog()
        brroker_id = reddog.login(login_name, password)
        res = reddog.reddog_button(brroker_id)
        json = res.json
        assert json['Code'] == 0 and res.status_code == 200 and res.elapsed.seconds <= 3
        campaignId = json['Data']['campaignId']
        time.sleep(1)
        res = reddog.reddog_get(brroker_id, campaignId)
        json = res.json
        assert json['Code'] == 0 and res.status_code == 200 and res.elapsed.seconds <= 3
        time.sleep(1)
        res = reddog.reddog_post(brroker_id, campaignId, count)
        json = res.json
        assert json['Code'] == 0 and res.status_code == 200 and res.elapsed.seconds <= 3
    def test_reddog_for(self):
        """红包雨测试用例"""
        for i in range(17880000001, 17880000030):
            print (i)
            login_name = str(i)
            # login_name = '18012345678'
            password = '123123456'
            count = random.uniform(20, 70)
            count = int(count)
            reddog = RedDog()
            brroker_id = reddog.login(login_name, password)
            res = reddog.reddog_button(brroker_id)
            json = res.json
            assert json['Code'] == 0 and res.status_code == 200 and res.elapsed.seconds <= 3
            campaignId = json['Data']['campaignId']
            # time.sleep(1)
            res = reddog.reddog_get(brroker_id, campaignId)
            json = res.json
            assert json['Code'] == 0 and res.status_code == 200 and res.elapsed.seconds <= 3
            time.sleep(1)
            res = reddog.reddog_post(brroker_id, campaignId, count)
            # time.sleep(1)
            # res = reddog.reddog_post(brroker_id, campaignId, count)
            # time.sleep(1)
            # res = reddog.reddog_post(brroker_id, campaignId, count)
            # json = res.json
            assert json['Code'] == 0 and res.status_code == 200 and res.elapsed.seconds <= 3
