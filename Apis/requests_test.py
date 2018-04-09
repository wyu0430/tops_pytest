# coding=utf-8

import requests


class Hztz(object):
    def __init__(self):
        self.base_url = 'http://wechat.hsinvestment.com.cn'
        self.header = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0; BKL-AL20 Build/HUAWEIBKL-AL20; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043906 Mobile Safari/537.36 MicroMessenger/6.6.3.1260(0x26060339) NetType/WIFI Language/zh_CN',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie': 'PHPSESSID=gio66aom4doc3oh5nirbbfbfgt'
        }

    def sign(self, obj):
        """签到"""
        query = '/index/signin/addSave'
        headers = self.header
        headers['a'] = 1
        body = {
            'obj': obj
        }
        res = requests.post( url=self.base_url + query, headers=headers, data=body,
                             allow_redirects=False )
        return res
