# coding=utf-8
import unittest
import time
from Apis.broker_active_api import ActiveQa
from db.db_active import get_active_answer_by_content

from common import public_configure

login_name = "15396258500"
password = "198436"
answer_list = [1, 2, 3, 4]
subject_num_Proportion = [1, 1, 1, 1, 1, 1, 2, 2, 2]

# 水军用户
user_list = ["17200000010","17100000096","17100000097","17200000001","17100000100","17100000101","17100000102","17100000103","17100000104","17100000105","17100000106","17100000107","17100000099","17200000003","17200000004","17200000005","17200000006","17200000009","17200000011","17200000013","13632345678","13622345678","18911111189","13888887868","13382345678","18911111182","13888887870","18911111187","18911111186","18911111188","13888887866","13392345678","18911111184","13888887867","13888887869","13612345678","18911111185","17000000101","17000000102","17000000103","17000000104","17000000105","17000000106","17000000107","17000000108","17000000109","17000000110","17000000111","17000000112","17000000113","17000000114","17000000115","17000000116","17000000117","17000000118","17000000119","17000000120","17300000076","17300000050","17000000001","17000000002","17000000003","17000000004","17000000005","17000000006","17000000007","17000000008","17000000009","17000000010","17000000011","17000000012","17000000013","17000000014","17000000015","17000000016","17000000017","17000000018","17000000019","17000000020","15962345678","15952345678","18911111142","15972345678","15822345678","15842345678","15922345678","18911111148","13888887887","18911111141","18911111146","15862345678","15852345678","13888887888","18911111150","15832345678","13888887890","15982345678","13888887889","13888887891","13888887892","13888887893","13888887894","18911111194","13888887896","13888887897","13888887898","13888887899","13888887900","18911111191","18911111192","18911111193","13888887895","18911111195","18911111196","18911111197","18911111198","18911111199","18911111200","17200000016","17200000017","17200000018","17200000019","17200000020","17200000021","17200000022","17200000023","17200000024","17200000025","17200000026","17200000027","17200000028","17200000029","17200000030","17200000031","17200000032","13888887877","17100000003","18911111208","17100000001","17100000005","18911111209","18212345678","18812345678","13877777777","18911111203","13888887880","13877777778","18911111205","18911111210","18112345678","18911111201","13888887878","18911111206","13877777779","18412345678","13877777774","18612345678","13877777776","13888887879","13888887876","18911111204","17100000004","18911111207","17100000002","17100000026","17100000027","17100000028","17100000029","17100000030","17100000031","17100000032","17100000033","17100000034","17100000035","17100000036","17100000037","17100000038","17100000039","17100000040","17100000041","17100000042","17100000043","17100000044","17100000045","18911111129","13372345678","13888887875","13322345678","18911111124","18911111127","13352345678","13888887874","18911111122","13888887871","18911111126","13888887872","13888887873","18911111123","13342345678","18911111125","18911111121","18911111130","18911111128","13362345678","17000000081","17000000082","17000000083","17000000084","17000000085","17000000086","17000000087","17000000088","17000000089","17000000090","17000000091","17000000092","17000000093","17000000094","17000000095","17000000096","17000000097","17000000098","17000000099","17000000100","17000000061","17000000062","17000000063","17000000064","17000000065","17000000066","17000000067","17000000068","17000000069","17000000070","17000000071","17000000072","17000000073","17000000074","17000000075","17000000076","17000000077","17000000078","17000000079","17000000080","18911111151","13888887918","18911111157","13888887919","13888887914","18911111156","13888887915","18911111153","13888887920","18911111154","18911111159","13888887912","18911111155","13888887917","13888887911","13888887916","18911111160","13888887913","18911111152","18911111158","17100000006","17100000007","17100000008","17100000009","17100000010","17100000011","17100000012","17100000013","17100000014","17100000015"]
pwd_list = ["kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","tjxiaoguan","tjxiaoguan","tjxiaoguan","tjxiaoguan","tjxiaoguan","tjxiaoguan","tjxiaoguan","tjxiaoguan","tjxiaoguan","tjxiaoguan","tjxiaoguan","tjxiaoguan","tjxiaoguan","tjxiaoguan","tjxiaoguan","tjxiaoguan","tjxiaoguan","tjxiaoguan","tjxiaoguan","tjxiaoguan","tjxiaoguan","tjxiaoguan","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","000001","xiaoguan123456","xiaoguan123456","199212","123456","sz123456","123456","123456a","sz123456","sz123456","xiaoguan123456","sz123456","sz123456","sz123456","sz123456","sz123456","xiaoguan123456","sz123456","xiaoguan123456","club123456","kakao001","kakao001","kakao001","kakao001","kakao001","kakao001","kakao001","kakao001","kakao001","kakao001","kakao001","kakao001","kakao001","kakao001","kakao001","kakao001","kakao001","kakao001","kakao001","kakao2016888","kakao2016888","kakao2016888","kakao2016888","kakao2016888","kakao2016888","kakao2016888","kakao2016888","kakao2016888","kakao2016888","kakao2016888","kakao2016888","kakao2016888","kakao2016888","kakao2016888","kakao2016888","kakao2016888","654321","654321","654321","654321","654321","654321","654321","654321","654321","654321","654321","654321","654321","654321","654321","654321","654321","654321","654321","654321","654320","654321","654321","654321","654321","654321","654321","654321","654321","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","20150628","20150628","20150628","20150628","20150628","20150628","20150628","20150628","20150628","20150628","20150628","20150628","20150628","20150628","20150628","20150628","20150628","20150628","20150628","20150628","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","kakaotops001","123456","123456","123456","123456","123456","123456","123456","123456","123456","123456"]

class TestActiveQaCaseGa( unittest.TestCase ):

    def test_active_qa_ga_case(self):
        activeqa = ActiveQa()
        activeqa.login( login_name, password )
        for i in range(1, 2):
            """全部回答正确后金币、星星数量增加校验"""
            # 获取当前玩家信息
            res = activeqa.get_season_player()
            json = res.json
            assert json['Code'] == 0 and res.status_code == 200 and res.elapsed.seconds <= 3
            # 获取目前金币数量
            accountBalance_begin = json['Data']['accountBalance']
            # 获取当前关卡，用于获取关卡需要的金币数量
            gateId = json['Data']['locationGate']
            """获取当前关卡信息"""
            res = activeqa.get_season_gates()
            json = res.json
            assert json['Code'] == 0 and res.status_code == 200 and res.elapsed.seconds <= 3
            # 获取关卡需要的金币数量以及当前关卡与星星情况
            for i in json['Data']['seasonGates']:
                if i['gateId'] == gateId:
                    enterNeedGold = i['enterNeedGold']
                    ownStar = i['ownStar']
                    passNeedStar = i['passNeedStar']
                    # 获取当前所在第几关卡
                    # orderNum = i['orderNum']
            '''获取题目组'''
            res = activeqa.get_question( gateId )
            json = res.json
            assert json['Code'] == 0 and res.status_code == 200 and res.elapsed.seconds <= 3
            # 初始化题目编号
            subjectOrder = 0
            # 初始化专业题与非专业提数量
            professional_subject_no = 0
            unprofessional_subject_no = 0
            for subject in json['Data']:
                subjectOrder = subjectOrder + 1
                subjectId = subject['subject']['subjectId']
                subjectContent = subject['subject']['subjectContent']
                # print(subjectContent)
                # 数据库获取答案
                subject_answer_code = get_active_answer_by_content( subjectContent )[0]['subject_answer']
                # 获取是否为专业提
                subject_level = get_active_answer_by_content( subjectContent )[0]['subject_level']
                assert subject_level in [0, 1]
                if subject_level == 0:
                    '''专业题'''
                    professional_subject_no = professional_subject_no + 1
                elif subject_level == 1:
                    '''非专业题'''
                    unprofessional_subject_no = unprofessional_subject_no + 1
                # 调用提交答案接口
                res = activeqa.post_answer( subjectOrder, subjectId, subject_answer_code, gateId )
                json = res.json
                isRight = json['Data']['isRight']
                assert isRight
                assert json['Code'] == 0 and res.status_code == 200 and res.elapsed.seconds <= 3
                # time.sleep(0.01)
            # # 断言专业题与非专业题比例
            # assert professional_subject_no == subject_num_Proportion[orderNum - 1]
            # assert unprofessional_subject_no == 5 - professional_subject_no
            # 答题完成后获取玩家信息
            res = activeqa.get_season_player()
            json = res.json
            # 答题完成后，获取当前关卡
            gateId_end = json['Data']['locationGate']
            assert json['Code'] == 0 and res.status_code == 200 and res.elapsed.seconds <= 3
            # *********断言金币数量是否增加**********
            accountBalance_end = json['Data']['accountBalance']
            assert accountBalance_end == accountBalance_begin + enterNeedGold
            # ***********断言星星是否增加***********
            """获取当前关卡信息"""
            res = activeqa.get_season_gates()
            json = res.json
            assert json['Code'] == 0 and res.status_code == 200 and res.elapsed.seconds <= 3
            # 获取关卡需要的金币数量以及当前关卡与星星情况
            for i in json['Data']['seasonGates']:
                if i['gateId'] == gateId_end:
                    ownStar_end = i['ownStar']
                    unlocked_end = i['unlocked']
            if passNeedStar != -1:
                assert ownStar < passNeedStar
                if ownStar < passNeedStar - 1:
                    assert ownStar_end == ownStar + 1
                    assert gateId_end == gateId
                else:
                    assert gateId_end == gateId + 1
                    assert ownStar_end == 0
                    assert unlocked_end

    def test_get_season_player(self):
        """获取玩家信息"""
        activeqa = ActiveQa()
        activeqa.login( login_name, password )
        res = activeqa.get_season_player()
        json = res.json
        assert json['Code'] == 0 and res.status_code == 200 and res.elapsed.seconds <= 3

    def test_get_seasonrank(self):
        """获取排行版"""
        activeqa = ActiveQa()
        activeqa.login( login_name, password )
        res = activeqa.get_season_player()
        json = res.json
        assert json['Code'] == 0 and res.status_code == 200 and res.elapsed.seconds <= 3
        seasonId = json['Data']['seasonId']
        res = activeqa.get_active_rank( seasonId )
        json = res.json
        assert json['Code'] == 0 and res.status_code == 200 and res.elapsed.seconds <= 3
        lenth_rank = len(json['Data']['rank'])
        assert lenth_rank <= 20

    def test_get_seasongates(self):
        """获取当前关卡信息"""
        activeqa = ActiveQa()
        activeqa.login( login_name, password )
        res = activeqa.get_season_gates()
        json = res.json
        print(res.elapsed.seconds)
        assert json['Code'] == 0 and res.status_code == 200 and res.elapsed.seconds <= 3

    def test_active_qa_ga_error_case(self):
        for i in range(1, 3):
            """全部回答正确后金币、星星数量增加校验"""
            activeqa = ActiveQa()
            activeqa.login( login_name, password )
            # 获取当前玩家信息
            res = activeqa.get_season_player()
            json = res.json
            assert json['Code'] == 0 and res.status_code == 200 and res.elapsed.seconds <= 3
            # 获取目前金币数量
            accountBalance_begin = json['Data']['accountBalance']
            # 获取当前关卡，用于获取关卡需要的金币数量
            gateId = json['Data']['locationGate']
            """获取当前关卡信息"""
            res = activeqa.get_season_gates()
            json = res.json
            assert json['Code'] == 0 and res.status_code == 200 and res.elapsed.seconds <= 3
            # 获取关卡需要的金币数量以及当前关卡与星星情况
            for i in json['Data']['seasonGates']:
                if i['gateId'] == gateId:
                    enterNeedGold = i['enterNeedGold']
                    ownStar = i['ownStar']
                    passNeedStar = i['passNeedStar']
                    # 获取当前所在第几关卡
                    # orderNum = i['orderNum']
            '''获取题目组'''
            res = activeqa.get_question( gateId )
            json = res.json
            assert json['Code'] == 0 and res.status_code == 200 and res.elapsed.seconds <= 3
            # 初始化题目编号
            subjectOrder = 0
            # 初始化专业题与非专业提数量
            professional_subject_no = 0
            unprofessional_subject_no = 0
            for subject in json['Data']:
                subjectOrder = subjectOrder + 1
                subjectId = subject['subject']['subjectId']
                subjectContent = subject['subject']['subjectContent']
                # print(subjectContent)
                # 数据库获取答案
                subject_answer_code = 0
                # 获取是否为专业提
                subject_level = get_active_answer_by_content( subjectContent )[0]['subject_level']
                assert subject_level in [0, 1]
                if subject_level == 0:
                    '''专业题'''
                    professional_subject_no = professional_subject_no + 1
                elif subject_level == 1:
                    '''非专业题'''
                    unprofessional_subject_no = unprofessional_subject_no + 1
                # 调用提交答案接口
                res = activeqa.post_answer( subjectOrder, subjectId, subject_answer_code, gateId )
                json = res.json
                isRight = json['Data']['isRight']
                assert not isRight
                assert json['Code'] == 0 and res.status_code == 200 and res.elapsed.seconds <= 3
                # time.sleep(0.01)
            # # 断言专业题与非专业题比例
            # assert professional_subject_no == subject_num_Proportion[orderNum - 1]
            # assert unprofessional_subject_no == 5 - professional_subject_no
            # 答题完成后获取玩家信息
            res = activeqa.get_season_player()
            json = res.json
            # 答题完成后，获取当前关卡
            gateId_end = json['Data']['locationGate']
            assert json['Code'] == 0 and res.status_code == 200 and res.elapsed.seconds <= 3
            # *********断言金币数量是否增加**********
            accountBalance_end = json['Data']['accountBalance']
            assert accountBalance_end == accountBalance_begin - enterNeedGold
            # ***********断言星星是否增加***********
            """获取当前关卡信息"""
            res = activeqa.get_season_gates()
            json = res.json
            assert json['Code'] == 0 and res.status_code == 200 and res.elapsed.seconds <= 3
            # 获取关卡需要的金币数量以及当前关卡与星星情况
            for i in json['Data']['seasonGates']:
                if i['gateId'] == gateId_end:
                    ownStar_end = i['ownStar']
                    unlocked_end = i['unlocked']
            # if passNeedStar != -1:
            #     assert ownStar < passNeedStar
            #     if ownStar < passNeedStar - 1:
            #         assert ownStar_end == ownStar - 1
            #         assert gateId_end == gateId
            #     else:
            #         assert gateId_end == gateId + 1
            #         assert ownStar_end == 0
            #         assert unlocked_end

    def test_active_qa_ga_case2(self):
        activeqa = ActiveQa()
        activeqa.login( login_name, password )
        for i in range(1, 6):
            """全部回答正确后金币、星星数量增加校验"""
            # 获取当前玩家信息
            res = activeqa.get_season_player()
            json = res.json
            assert json['Code'] == 0 and res.status_code == 200 and res.elapsed.seconds <= 3
            # 获取目前金币数量
            accountBalance_begin = json['Data']['accountBalance']
            # 获取当前关卡，用于获取关卡需要的金币数量
            gateId = json['Data']['locationGate']
            gateId = 8
            """获取当前关卡信息"""
            res = activeqa.get_season_gates()
            json = res.json
            assert json['Code'] == 0 and res.status_code == 200 and res.elapsed.seconds <= 3
            # 获取关卡需要的金币数量以及当前关卡与星星情况
            for i in json['Data']['seasonGates']:
                if i['gateId'] == gateId:
                    enterNeedGold = i['enterNeedGold']
                    ownStar = i['ownStar']
                    passNeedStar = i['passNeedStar']
                    # 获取当前所在第几关卡
                    # orderNum = i['orderNum']
            '''获取题目组'''
            res = activeqa.get_question( gateId )
            json = res.json
            assert json['Code'] == 0 and res.status_code == 200 and res.elapsed.seconds <= 3
            # 初始化题目编号
            subjectOrder = 0
            # 初始化专业题与非专业提数量
            professional_subject_no = 0
            unprofessional_subject_no = 0
            for subject in json['Data']:
                subjectOrder = subjectOrder + 1
                subjectId = subject['subject']['subjectId']
                subjectContent = subject['subject']['subjectContent']
                # print(subjectContent)
                # 数据库获取答案
                subject_answer_code = get_active_answer_by_content( subjectContent )[0]['subject_answer']
                # 获取是否为专业提
                subject_level = get_active_answer_by_content( subjectContent )[0]['subject_level']
                assert subject_level in [0, 1]
                if subject_level == 0:
                    '''专业题'''
                    professional_subject_no = professional_subject_no + 1
                elif subject_level == 1:
                    '''非专业题'''
                    unprofessional_subject_no = unprofessional_subject_no + 1
                # 调用提交答案接口
                res = activeqa.post_answer( subjectOrder, subjectId, subject_answer_code, gateId )
                json = res.json
                isRight = json['Data']['isRight']
                assert isRight
                assert json['Code'] == 0 and res.status_code == 200 and res.elapsed.seconds <= 3
                # time.sleep(0.01)
            # # 断言专业题与非专业题比例
            # assert professional_subject_no == subject_num_Proportion[orderNum - 1]
            # assert unprofessional_subject_no == 5 - professional_subject_no
            # 答题完成后获取玩家信息
            res = activeqa.get_season_player()
            json = res.json
            # 答题完成后，获取当前关卡
            gateId_end = json['Data']['locationGate']
            assert json['Code'] == 0 and res.status_code == 200 and res.elapsed.seconds <= 3
            # *********断言金币数量是否增加**********
            accountBalance_end = json['Data']['accountBalance']
            # assert accountBalance_end == accountBalance_begin + enterNeedGold
            # ***********断言星星是否增加***********
            """获取当前关卡信息"""
            res = activeqa.get_season_gates()
            json = res.json
            # assert json['Code'] == 0 and res.status_code == 200 and res.elapsed.seconds <= 3
            # # 获取关卡需要的金币数量以及当前关卡与星星情况
            # for i in json['Data']['seasonGates']:
            #     if i['gateId'] == gateId_end:
            #         ownStar_end = i['ownStar']
            #         unlocked_end = i['unlocked']
            # if passNeedStar != -1:
            #     assert ownStar < passNeedStar
            #     if ownStar < passNeedStar - 1:
            #         assert ownStar_end == ownStar + 1
            #         assert gateId_end == gateId
            #     else:
            #         assert gateId_end == gateId + 1
            #         assert ownStar_end == 0
            #         assert unlocked_end