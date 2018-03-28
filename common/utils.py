# coding=utf-8
import json
from collections import OrderedDict
from functools import wraps
from datetime import datetime
from hashlib import md5
from urllib import urlencode
from urlparse import urljoin, urlparse
import records
from contextlib import contextmanager

from pithy import request


class DB(object):

    def __init__(self, db_url):
        self.db_url = db_url

    def query(self, statement, **params):
        db = records.Database(self.db_url)
        res = db.query(statement, **params)
        db.close()
        return res


def get_md5(s):
    m = md5()
    m.update(s)
    return m.hexdigest()


class Sign(object):

    @staticmethod
    def v4(host, query, body, is_json):
        s_url = host + '?' + urlencode(query) if query else host
        s_body = '00000000000000000000000000000000'
        s_time = datetime.strftime(datetime.now(), "%a, %d %b %Y %H:%M:%S GMT+0800")
        s_secret_key = '374fa3ab6b1fae595db5382afe415bce'
        if body:
            if is_json:
                s_body = get_md5(json.dumps(body))
            else:
                s_body = get_md5(urlencode(body))
        return 'v4:' + get_md5(s_url.lower() + s_body + s_time + s_secret_key), s_time


def sign(version='v4'):
    def decorate(func):
        sign_func = getattr(Sign, version.lower())

        @wraps(func)
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            params = res.get_arg('params')
            data = res.get_arg('data')
            _json = res.get_arg('json')
            url = urlparse(res.url)
            if _json:
                signature = sign_func(url.netloc + url.path, params, _json, True)
            else:
                signature = sign_func(url.netloc + url.path, params, data, False)
            res.add_headers(Signature=signature[0], Date=signature[1])
            return res
        return wrapper
    return decorate


class DB(object):

    def __init__(self, db_url):
        self.db_url = db_url

    def query(self, statement, **params):
        db = records.Database(self.db_url)
        res = db.query(statement, **params)
        db.close()
        return res
