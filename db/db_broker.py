# coding=utf-8
from common.utils import DB
from common.db_config import CONFIG
import redis
import re

# 定义活动DB
code_db = DB(CONFIG.TEST_CODE)


def get_phone_code(phone):
    '''获取验证码'''
    res = code_db.query("SELECT * FROM notify_sms_log WHERE target_phone LIKE '%{}%' ORDER BY create_time DESC LIMIT 1;".format(phone))
    #   print(res.all()[0]['content'])
    try:
        code = re.findall( u'(验证码：)(\d+).+', res.all()[0]['content'] )[0][1]
    except:
        code = 0
    return code



# if __name__ == '__main__':
#     print get_phone_code(18999990003)
