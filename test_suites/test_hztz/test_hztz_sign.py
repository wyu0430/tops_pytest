# coding=utf8
from Apis.requests_test import Hztz
import json
import pytest

class TestHztzSign( object ):
    @pytest.fixture( autouse=True)
    def before(self):
        b = 'aaaaaaaaa'
        return b

    def test_hztz_sign_case(self, before):
        print before
        hztz = Hztz()
        res = hztz.sign(1)
        # 获取当前玩家信息
        json = res.json()
        text = res.text
        print(text)
        assert not json['hs_result']

