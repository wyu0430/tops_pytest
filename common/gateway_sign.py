# coding=utf-8
from hashlib import md5
import md5
import re
import time
import datetime

def time_gmt():
    GMT_FORMAT = '%a, %d %b %Y %H:%M:%S GMT'
    time_gmt = datetime.datetime.now().strftime( GMT_FORMAT ) + '+0800'
    # print time_gmt
    return time_gmt

def get_md5_value(s):
    mString = md5.new()
    mString.update( s )
    return mString.hexdigest()


class GatewaySignV4(object):
    @staticmethod
    def sign_v4(host, query, Body='', Date=time_gmt()):
        def time_gmt():
            GMT_FORMAT = '%a, %d %b %Y %H:%M:%S GMT'
            time_gmt = datetime.datetime.now().strftime( GMT_FORMAT ) + '+0800'
            # print time_gmt
            return time_gmt
        AppKeySecret = '374fa3ab6b1fae595db5382afe415bce'
        if 'http://' in host or 'https://' in host:
            host = re.findall( '^http(s)?://(.+)$', host )[0][1]
            print 'host==============' + host
        if 'apikber' in query:
            if 'test' in host or 'beta' in host:
                AppKeySecret = 'f689950810264c04a105f0df3c2e9fc4'
            else:
                AppKeySecret = '12648400a71f4e4daa53f7f8a47c5873'
        if Body == '':
            Body_md5 = '00000000000000000000000000000000'
        else:
            print 'Body==============' + Body
            Body = md5.new( Body )
            Body_md5 = Body.hexdigest()

        str1 = host + query
        # print str1.lower()

        si = str1.lower() + Body_md5 + Date + AppKeySecret
        print 'si==================' + si
        sign_v4 = md5.new()
        sign_v4.update( si )
        return 'v4:' + sign_v4.hexdigest(), Date

