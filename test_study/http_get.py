# coding=utf-8
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'
}

res = requests.get('https://toutiao.io/k/8ld3eo ', headers=headers, allow_redirects=False)

print res.headers['Location']