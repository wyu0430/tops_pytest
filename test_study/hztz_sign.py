# coding=utf-8
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0; BKL-AL20 Build/HUAWEIBKL-AL20; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043906 Mobile Safari/537.36 MicroMessenger/6.6.3.1260(0x26060339) NetType/WIFI Language/zh_CN',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'PHPSESSID=gio66aom4doc3oh5nirbbfbfgt'
}
body = {
    'obj': 1
}
res = requests.post('http://wechat.hsinvestment.com.cn/index/signin/addSave', headers=headers, data=body, allow_redirects=False)

print res.text