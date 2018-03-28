# coding=utf8
from Apis.requests_test import Hztz
import json

class TestHztzSign( object ):

    # def setup_class(cls):
    #     cls.activeqa = ActiveQa()
    #     cls.activeqa.login( login_name, password )
    def test_hztz_sign_case(self):
        hztz = Hztz()
        res = hztz.sign(1)
        # 获取当前玩家信息
        json = res.json()
        text = res.text
        print(text)
        assert not json['hs_result']

