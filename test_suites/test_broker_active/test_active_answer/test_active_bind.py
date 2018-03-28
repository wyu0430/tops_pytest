# coding=utf-8
import unittest
import time
from Apis.broker_active_api import ActiveQa
from db.db_active import get_active_answer,get_share_num
import random
import os

login_name = "15157163734"
password = "147852"


class TestBind( unittest.TestCase ):
    def test_active_bind_case(self):
        """王者推荐用户"""
        login_name = "17880000202"
        password = "123123456"
        activebind = ActiveQa()
        activebind.login( login_name, password )
        res = activebind.bind_player('000075')
        json = res.json
        assert json['Code'] == 0 and res.status_code == 200 and res.elapsed.seconds <= 3

    def test_active_bind_list_case(self):
        """王者推荐列表"""
        activebind = ActiveQa()
        activebind.login( login_name, password )
        res = activebind.bind_list(1, 20)
        json = res.json
        assert json['Code'] == 0 and res.status_code == 200 and res.elapsed.seconds <= 3