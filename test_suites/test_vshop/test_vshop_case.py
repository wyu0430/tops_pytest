# coding=utf-8
import unittest
import time
from Apis.vshop_api import Vshop
from common import public_configure

login_name = "15157163734"
password = "147852"


class TestVshopCase(unittest.TestCase):
    def test_vshop_case1(self):
        vshop = Vshop()
        vshop.login(login_name, password)
        # 微店楼盘列表
        res = vshop.myBuildingListVdian(1)
        json = res.json
        code = res.status_code
        assert json['Code'] == 0 and code == 200 and res.elapsed.seconds <= 3
        res = vshop.myBuildingListVdian(3)
        json = res.json
        code = res.status_code
        assert json['Code'] == 0 and code == 200 and res.elapsed.seconds <= 3
        res = vshop.myBuildingListVdian(5)
        json = res.json
        code = res.status_code
        assert json['Code'] == 0 and code == 200 and res.elapsed.seconds <= 3
        # 我的微店接口
        res = vshop.myVdian(112)
        json = res.json
        code = res.status_code
        assert json['Code'] == 0 and code == 200 and res.elapsed.seconds <= 3
        # # 批量添加楼盘
        # res = vshop.collectionBuildings([1,1], [485,26])
        # json = res.json
        # code = res.status_code
        # assert json['Code'] == 0 and code == 200 and res.elapsed.seconds <= 3


