# coding=utf-8

import redis


class Test:
    # 销冠新房url
    SAAS_BASE_URL = 'http://saasapi.test.apitops.com/topsales-web/v4'

    # gateway url
    GATEWAY_BASE_URL = 'http://gateway.test.apitops.com'

    # saas db
    SAAS_DATABASE = 'mysql+pymysql://root:root12qw!@QW@test.mysql.apitops.com:4310/tops_building_saas?charset=utf8'

    # active db
    TEST_ACTIVE = 'mysql+pymysql://root:root12qw!@QW@test.mysql.apitops.com:4310/tops_activity_operation?charset=utf8'

    # broker_center db
    TEST_BROKER = 'mysql+pymysql://root:root12qw!@QW@test.mysql.apitops.com:4310/tops_broker_center?charset=utf8'

    # code db
    TEST_CODE = 'mysql+pymysql://admin:7fmyfCv4UUhU7Vd8ehLN9rdN7EMm7p@dev.mysql.apitops.com:4307/tops_message?charset=utf8'

    # test_redis
    TEST_REDIS = redis.Redis( host='test.redis.apitops.com', port=7380, password='pQwL2HC794kBmDkUwkm9HDwNX8BkTr',db=17 )

    class ACCOUNT:
        BOPS_TOP = 'top', '123456'

class Dev:

    # 运营活动开发环境DB
    DEV_ACTIVE = 'mysql+pymysql://admin:7fmyfCv4UUhU7Vd8ehLN9rdN7EMm7p@dev.mysql.apitops.com:4308/tops_activity_operation?charset=utf8'

CONFIG = Test