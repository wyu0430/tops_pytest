# coding=utf-8
import unittest
import pytest
import time
from Apis.broker_center_api import BrokerCenter
from db.db_broker import get_phone_code
from db.db_active import get_luck_draw_count,get_share_count


import random


class TestRegister( object ):

    def test_register_activity_count(self):
        brokerId = 34108
        broker_phone = '18999990122'
        password = '123123456'
        shop_code = 'KK888'
        """
        1、邀请好友
        2、注册
        3、绑定门店
        4、大转盘次数增加
        """
        register = BrokerCenter()
        # 获取已经邀请好友的次数
        old_share_count = get_share_count(brokerId)
        # 获取抽奖次数
        old_luck_draw_count = get_luck_draw_count(brokerId)
        # 邀请好友
        res = register.share_recommend_broker(brokerId, broker_phone)
        json = res.json
        assert json['Code'] == 0 and res.status_code == 200
        # 调用获取注册验证码接口
        res = register.send_phone_code(broker_phone)
        json = res.json
        assert json['Code'] == 0 and res.status_code == 200
        time.sleep(15)
        # 数据库查询验证码
        code = get_phone_code(broker_phone)
        res = register.sign_in_phone(code, broker_phone, password)
        json = res.json
        assert json['Code'] == 0 and res.status_code == 200
        # 登陆获取ak
        res = register.login(broker_phone, password)
        # 门店绑定
        res = register.outlet_code(shop_code)
        json = res.json
        assert json['Code'] == 0 and res.status_code == 200
        res = register.bind_broker_company(broker_phone, shop_code)
        json = res.json
        assert json['Code'] == 0 and res.status_code == 200
        # 获取礼包
        res = register.broker_share_get_broker_bag_list()
        json = res.json
        assert json['Code'] == 0 and res.status_code == 200
        # 获取分享后的邀请好友的次数
        time.sleep(10)
        new_share_count = get_share_count(brokerId)
        new_luck_draw_count = get_luck_draw_count( brokerId )
        # 断言被邀请者数据
        new_broker_id = register.login( broker_phone, password )
        print new_broker_id
        new_broker_luck_draw_count = get_luck_draw_count(new_broker_id)
        assert new_broker_luck_draw_count == 2, "注册+被邀请后转盘机会加2"
        assert new_share_count == old_share_count + 1
        if new_share_count % 3 == 0:
            assert new_luck_draw_count == old_luck_draw_count + 2
        else:
            assert new_luck_draw_count == old_luck_draw_count + 1

    # def test_register_activity_count1(self):
    #     """
    #     1、注册
    #     2、绑定门店
    #     3、大转盘次数增加
    #     """
    #     brokerId = 34108
    #     broker_phone = '18999980003'
    #     password = '123123456'
    #     shop_code = 'KK888'
    #     register = BrokerCenter()
    #     # 获取已经邀请好友的次数
    #     old_share_count = get_share_count(brokerId)
    #     # 获取抽奖次数
    #     old_luck_draw_count = get_luck_draw_count(brokerId)
    #     # # 邀请好友
    #     # res = register.share_recommend_broker(brokerId, broker_phone)
    #     # json = res.json
    #     # assert json['Code'] == 0 and res.status_code == 200 and res.elapsed.seconds <= 3
    #     # 调用获取注册验证码接口
    #     res = register.send_phone_code(broker_phone)
    #     json = res.json
    #     assert json['Code'] == 0 and res.status_code == 200 and res.elapsed.seconds <= 3
    #     time.sleep(15)
    #     # 数据库查询验证码
    #     code = get_phone_code(broker_phone)
    #     res = register.sign_in_phone(code, broker_phone, password)
    #     json = res.json
    #     assert json['Code'] == 0 and res.status_code == 200 and res.elapsed.seconds <= 3
    #     # 登陆获取ak
    #     res = register.login(broker_phone, password)
    #     # 门店绑定
    #     res = register.outlet_code(shop_code)
    #     json = res.json
    #     assert json['Code'] == 0 and res.status_code == 200 and res.elapsed.seconds <= 3
    #     res = register.bind_broker_company(broker_phone, shop_code)
    #     json = res.json
    #     assert json['Code'] == 0 and res.status_code == 200 and res.elapsed.seconds <= 3
    #     # 获取礼包
    #     res = register.broker_share_get_broker_bag_list()
    #     json = res.json
    #     assert json['Code'] == 0 and res.status_code == 200 and res.elapsed.seconds <= 3
    #     # 获取分享后的邀请好友的次数
    #     time.sleep(3)
    #     new_share_count = get_share_count(brokerId)
    #     new_luck_draw_count = get_luck_draw_count( brokerId )
    #     # 断言被邀请者数据
    #     new_broker_id = register.login( broker_phone, password )
    #     print new_broker_id
    #     new_broker_luck_draw_count = get_luck_draw_count(new_broker_id)
    #     assert new_broker_luck_draw_count == 1, "注册后转盘机会加1"
    #     assert new_share_count == old_share_count, "没有分享好友，分享次数不增加"