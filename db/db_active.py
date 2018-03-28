# coding=utf-8
from common.utils import DB
from common.db_config import CONFIG
import redis

# 定义活动DB
active_db = DB( CONFIG.TEST_ACTIVE )
active_redis = CONFIG.TEST_REDIS
broker_center_db = DB( CONFIG.TEST_BROKER )


# def get_building_from_ids(l):
#     """
#     从新房ID获取楼盘信息
#     """
#     return saas_db.query("select * from tbd_building where building_id in %s" % str(tuple(l)))
#
#
# def get_label_name_by_target_id(_id):
#     """
#     从target id查询label name
#     """
#     res = saas_db.query('select label_name from tbd_label_binding where is_deleted=0 and target_id=%s' % _id)
#     return [i.label_name for i in res]

def get_active_answer(id):
    '''获取销冠王者答案'''
    res = active_db.query( 'SELECT * FROM tact_cd_subject WHERE subject_id = {}'.format( id ) )
    return res


def get_active_answer_by_content(subject_content):
    '''获取销冠王者答案'''
    res = active_db.query( 'SELECT * FROM tact_cd_subject WHERE subject_content = ' + "'" + subject_content + "'" )
    print('SELECT * FROM tact_cd_subject WHERE subject_content LIKE  %"' + subject_content + '%"')
    return res


def get_share_num(user_id, seasonId):
    test_redis = active_redis
    a = test_redis.llen( 'TACT:CD:TEMP|user_share|{}:{}'.format( user_id, seasonId ) )
    return a


# 获取转盘次数
def get_luck_draw_count(broker_id):
    res = broker_center_db.query( 'SELECT * FROM tb_broker_luckywheel_lives WHERE broker_id ={} ;'.format( broker_id ) )
    try:
        count = res.first()['lives']
        return count
    except:
        return 0


# 获取已经分享的次数
def get_share_count(broker_id):
    res = broker_center_db.query( 'SELECT COUNT(*) FROM tb_broker_share WHERE parent_broker_id = {}  AND is_login = 1 AND update_time > "2018-03-05 09:00:00" ORDER BY create_time DESC;'.format( broker_id ) )
    try:
        count = res.first()["COUNT(*)"]
        return count
    except:
        return 0


# if __name__ == '__main__':
#     print get_luck_draw_count( 151451 )
