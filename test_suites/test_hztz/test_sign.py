# coding=utf8
from Apis.requests_api import Hztz
import json
import pytest


@pytest.fixture(autouse=True)
def before():
    obj = 1
    return obj


class TestHztzSign(object):
    def test_hztz_sign_case(self, before):
        print before
        hztz = Hztz()
        res = hztz.sign(before)
        # 获取当前玩家信息
        json = res.json()
        text = res.text
        print(text)