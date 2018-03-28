# coding=utf-8
import requests

"""获取销冠经纪临时密码"""
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Content-Type': ' application/x-www-form-urlencoded; charset=utf-8',
    'appcode': 'system',
    'Cookie': '_tops_user_sid=a2e3dfb4-7a61-4f72-acb9-123dbe0baadb'
}
data = {
    'loginName': '17200000018'
}
res = requests.post( 'http://user.apitops.com/Authorization/GetTempPassword', headers=headers, data=data,
                     allow_redirects=False )
print res.text
