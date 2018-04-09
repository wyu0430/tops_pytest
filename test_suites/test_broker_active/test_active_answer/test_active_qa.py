# coding=utf-8
import unittest
import time
from Apis.broker_active_api import ActiveQa
from db.db_active import get_active_answer,get_share_num
import random
import os


def answer_error(answer):
    answer_list = ['1', '2', '3', '0']
    answer_list.remove(answer)
    error_answer = random.sample(answer_list, 1)
    return error_answer[0]


subject_num_Proportion = [1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2]
login_name = os.getenv('login_name', '18012345678')
password = os.getenv('password', '123123456')

login_name = "18012345678"
password = "123123456"
answer_list = [1, 2, 3, 4]
# 每一关专业题数量
subject_num_Proportion = [1, 1, 1, 1, 1, 1]


class TestActiveQaCase( unittest.TestCase ):

    def test_active_qa_case(self):
        """全部回答正确后金币、星星数量增加校验"""
        activeqa = ActiveQa()
        activeqa.login( login_name, password )
        # 获取当前玩家信息
        res = activeqa.get_season_player()
        json = res.json
        assert json['Code'] == 0 and res.status_code == 200 and res.elapsed.seconds <= 3
        # 获取目前金币数量
        accountBalance_begin = json['Data']['accountBalance']
        # 获取星星总数
        gotStarNum = json['Data']['gotStarNum']
        # 获取当前所在关卡
        locationGate = json['Data']['locationGate']
        # 当前关卡星星数量
        locationGateStarNum = json['Data']['locationGateStarNum']
        # # 断言星星总数与关卡星星数是否相符合
        # need_star_list = [1, 2, 3, 4, 5, 6]
        # star_sum = 0
        # for i in range( 0, locationGate - 1 ):
        #     star_sum = need_star_list[i] + star_sum
        # star_sum = star_sum + locationGateStarNum
        # assert star_sum == gotStarNum
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
                orderNum = i['orderNum']
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
            # 数据库获取答案
            subject_answer_code = get_active_answer( subjectId )[0]['subject_answer']
            # 获取是否为专业提
            subject_level = get_active_answer( subjectId )[0]['subject_level']
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
            assert isRight == True
            assert json['Code'] == 0 and res.status_code == 200 and res.elapsed.seconds <= 3
            # time.sleep(0.01)
        # 断言专业题与非专业题比例
        assert professional_subject_no == subject_num_Proportion[orderNum - 1]
        assert unprofessional_subject_no == 5 - professional_subject_no
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



    def test_active_quick_qa_case(self):
        """全部回答正确后金币、星星数量增加校验"""
        activeqa = ActiveQa()
        activeqa.login( login_name, password )
        # 获取当前玩家信息
        res = activeqa.get_season_player()
        json = res.json
        assert json['Code'] == 0 and res.status_code == 200 and res.elapsed.seconds <= 3
        # 获取目前金币数量
        accountBalance_begin = json['Data']['accountBalance']
        # 获取星星总数
        gotStarNum = json['Data']['gotStarNum']
        # 获取当前所在关卡
        locationGate = json['Data']['locationGate']
        # 当前关卡星星数量
        locationGateStarNum = json['Data']['locationGateStarNum']
        # # 断言星星总数与关卡星星数是否相符合
        # need_star_list = [1, 2, 3, 4, 5, 6]
        # star_sum = 0
        # for i in range( 0, locationGate - 1 ):
        #     star_sum = need_star_list[i] + star_sum
        # star_sum = star_sum + locationGateStarNum
        # assert star_sum == gotStarNum
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
                orderNum = i['orderNum']
        '''获取题目组'''
        res = activeqa.get_quict_question( gateId )
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
            # 数据库获取答案
            subject_answer_code = get_active_answer( subjectId )[0]['subject_answer']
            # 获取是否为专业提
            subject_level = get_active_answer( subjectId )[0]['subject_level']
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
            assert isRight == True
            assert json['Code'] == 0 and res.status_code == 200 and res.elapsed.seconds <= 3
            # time.sleep(0.01)
        # 断言专业题与非专业题比例
        assert professional_subject_no == subject_num_Proportion[orderNum - 1]
        assert unprofessional_subject_no == 5 - professional_subject_no
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
        lenth_rank = len( json['Data']['rank'] )
        assert lenth_rank <= 20

    def test_get_seasongates(self):
        """获取当前关卡信息"""
        activeqa = ActiveQa()
        activeqa.login( login_name, password )
        res = activeqa.get_season_gates()
        json = res.json
        assert json['Code'] == 0 and res.status_code == 200 and res.elapsed.seconds <= 3

    def test_confirm_season_share(self):
        """确认分享测试用例"""
        activeqa = ActiveQa()
        activeqa.login( login_name, password )
        # 获取关卡信息
        res = activeqa.get_season_gates()
        json = res.json
        assert json['Code'] == 0 and res.status_code == 200 and res.elapsed.seconds <= 3
        seasonId = json['Data']['season']['seasonId']
        # 获取当前玩家信息
        res = activeqa.get_season_player()
        json = res.json
        user_id = json['Data']['userId']
        assert json['Code'] == 0 and res.status_code == 200 and res.elapsed.seconds <= 3
        # 获取目前金币数量
        accountBalance_begin = json['Data']['accountBalance']
        # 从redis中获取分享前今日分享次数次数
        share_count_begin = get_share_num(user_id, seasonId)
        res = activeqa.confirm_season_share()
        time.sleep(1)
        json = res.json
        assert json['Code'] == 0 and res.status_code == 200 and res.elapsed.seconds <= 3
        # 从redis中获取分享后分享次数
        share_count_end = get_share_num(user_id, seasonId)
        # 获取分享后玩家信息
        res = activeqa.get_season_player()
        json = res.json
        assert json['Code'] == 0 and res.status_code == 200 and res.elapsed.seconds <= 3

        # 断言分享次数
        assert share_count_begin <= 2
        assert share_count_end <= 2
        if share_count_begin < 2:
            assert share_count_end == share_count_begin + 1
            # 获取目前金币数量
            accountBalance_end = json['Data']['accountBalance']
            assert accountBalance_end == accountBalance_begin + 100
        else:
            assert share_count_begin == share_count_end
            # 获取目前金币数量
            accountBalance_end = json['Data']['accountBalance']
            assert accountBalance_end == accountBalance_begin


    def test_active_qa_case0(self):
        """全部回答正确后金币、星星数量增加校验"""
        activeqa = ActiveQa()
        activeqa.login( login_name, password )
        # 获取当前玩家信息
        res = activeqa.get_season_player()
        json = res.json
        assert json['Code'] == 0 and res.status_code == 200 and res.elapsed.seconds <= 3, '获取当前玩家单接口断言'
        # 获取目前金币数量
        accountBalance_begin = json['Data']['accountBalance']
        # 获取当前关卡，用于获取关卡需要的金币数量
        gateId = json['Data']['locationGate']
        """获取当前关卡信息"""
        res = activeqa.get_season_gates()
        json = res.json
        assert json['Code'] == 0 and res.status_code == 200 and res.elapsed.seconds <= 3, '获取当前关卡信息单接口断言'
        # 获取关卡需要的金币数量以及当前关卡与星星情况
        for i in json['Data']['seasonGates']:
            if i['gateId'] == gateId:
                enterNeedGold = i['enterNeedGold']
                ownStar = i['ownStar']
                passNeedStar = i['passNeedStar']
        '''获取题目组'''
        res = activeqa.get_question( gateId )
        json = res.json
        assert json['Code'] == 0 and res.status_code == 200 and res.elapsed.seconds <= 3, '获取题目组单接口断言'
        # 获取题目编号
        subjectOrder = 0
        for subject in json['Data']:
            subjectOrder = subjectOrder + 1
            subjectId = subject['subject']['subjectId']
            # 数据库获取答案
            subject_answer_code = get_active_answer( subjectId )[0]['subject_answer']
            # 调用提交答案接口
            res = activeqa.post_answer( subjectOrder, subjectId, subject_answer_code, gateId )
            json = res.json
            isRight = json['Data']['isRight']
            assert isRight, '提交答案正确响应断言'
            assert json['Code'] == 0 and res.status_code == 200 and res.elapsed.seconds <= 3, '提交答案接口单接口断言'
            time.sleep(1)
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
                assert ownStar_end == ownStar + 1, '星星数量断言'
                assert gateId_end == gateId, '星星数量断言'
            else:
                assert gateId_end == gateId + 1, '关卡数量断言'
                assert ownStar_end == 0, '通过后星星数量断言'
                assert unlocked_end, '通过后关卡解锁断言'

    def test_active_qa_case1(self):
        """错误1题金币、星星数量增加校验"""
        # 设置错误题目数量
        error_answer_num = 1
        activeqa = ActiveQa()
        activeqa.login( login_name, password )
        res = activeqa.get_season_player()
        json = res.json
        assert json['Code'] == 0 and res.status_code == 200 and res.elapsed.seconds <= 3
        # 获取目前金币数量
        accountBalance_begin = json['Data']['accountBalance']
        # 获取当前关卡
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
        '''获取题目组'''
        res = activeqa.get_question(gateId)
        json = res.json
        assert json['Code'] == 0 and res.status_code == 200 and res.elapsed.seconds <= 3
        # 获取题目编号
        subjectOrder = 0
        # 随机选择题号答错
        error_no_list = random.sample([1, 2, 3, 4, 5], error_answer_num)
        for subject in json['Data']:
            subjectOrder = subjectOrder + 1
            subjectId = subject['subject']['subjectId']
            # 数据库获取答案
            subject_answer_code = get_active_answer( subjectId )[0]['subject_answer']
            # 调用提交答案接口
            if subjectOrder in error_no_list:
                res = activeqa.post_answer( subjectOrder, subjectId, answer_error(subject_answer_code), gateId )
                json = res.json
                isRight = json['Data']['isRight']
                assert isRight == False
                assert json['Data']['rightCode'] == subject_answer_code
                assert json['Code'] == 0 and res.status_code == 200 and res.elapsed.seconds <= 3

            else:
                res = activeqa.post_answer( subjectOrder, subjectId, subject_answer_code, gateId )
                json = res.json
                isRight = json['Data']['isRight']
                assert isRight == True
                assert json['Code'] == 0 and res.status_code == 200 and res.elapsed.seconds <= 3
            time.sleep(1)
        # 答题完成后获取玩家信息
        res = activeqa.get_season_player()
        json = res.json
        # 答题完成后，获取当前关卡
        gateId_end = json['Data']['locationGate']
        assert json['Code'] == 0 and res.status_code == 200 and res.elapsed.seconds <= 3
        # 断言金币数量是否增加
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

    def test_active_qa_case2(self):
        """错误2题后金币、星星数量增加校验"""
        # 设置错误题目数量
        error_answer_num = 2
        activeqa = ActiveQa()
        activeqa.login( login_name, password )
        res = activeqa.get_season_player()
        json = res.json
        assert json['Code'] == 0 and res.status_code == 200 and res.elapsed.seconds <= 3
        # 获取目前金币数量
        accountBalance_begin = json['Data']['accountBalance']
        # 获取当前关卡
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
        '''获取题目组'''
        res = activeqa.get_question( gateId )
        json = res.json
        assert json['Code'] == 0 and res.status_code == 200 and res.elapsed.seconds <= 3
        # 获取题目编号
        subjectOrder = 0
        # 随机选择题号答错
        error_no_list = random.sample( [1, 2, 3, 4, 5], error_answer_num )
        for subject in json['Data']:
            subjectOrder = subjectOrder + 1
            subjectId = subject['subject']['subjectId']
            # 数据库获取答案
            subject_answer_code = get_active_answer( subjectId )[0]['subject_answer']
            # 调用提交答案接口
            if subjectOrder in error_no_list:
                res = activeqa.post_answer( subjectOrder, subjectId, answer_error( subject_answer_code ), gateId )
                json = res.json
                isRight = json['Data']['isRight']
                assert not isRight
                assert json['Data']['rightCode'] == subject_answer_code
                assert json['Code'] == 0 and res.status_code == 200 and res.elapsed.seconds <= 3

            else:
                res = activeqa.post_answer( subjectOrder, subjectId, subject_answer_code, gateId )
                json = res.json
                isRight = json['Data']['isRight']
                assert isRight
                assert json['Code'] == 0 and res.status_code == 200 and res.elapsed.seconds <= 3
            time.sleep( 1 )
        # 答题完成后获取玩家信息
        res = activeqa.get_season_player()
        json = res.json
        # 答题完成后，获取当前关卡
        gateId_end = json['Data']['locationGate']
        assert json['Code'] == 0 and res.status_code == 200 and res.elapsed.seconds <= 3
        # 断言金币数量是否增加
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

    def test_active_qa_case3(self):
        """错误3题后金币、星星数量增加校验"""
        # 设置错误题目数量
        error_answer_num = 3
        activeqa = ActiveQa()
        activeqa.login( login_name, password )
        res = activeqa.get_season_player()
        json = res.json
        assert json['Code'] == 0 and res.status_code == 200 and res.elapsed.seconds <= 3
        # 获取目前金币数量
        accountBalance_begin = json['Data']['accountBalance']
        # 获取当前关卡
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
        '''获取题目组'''
        res = activeqa.get_question( gateId )
        json = res.json
        assert json['Code'] == 0 and res.status_code == 200 and res.elapsed.seconds <= 3
        # 获取题目编号
        subjectOrder = 0
        # 随机选择题号答错
        error_no_list = random.sample( [1, 2, 3, 4, 5], error_answer_num )
        for subject in json['Data']:
            subjectOrder = subjectOrder + 1
            subjectId = subject['subject']['subjectId']
            # 数据库获取答案
            subject_answer_code = get_active_answer( subjectId )[0]['subject_answer']
            # 调用提交答案接口
            if subjectOrder in error_no_list:
                res = activeqa.post_answer( subjectOrder, subjectId, answer_error( subject_answer_code ), gateId )
                json = res.json
                isRight = json['Data']['isRight']
                assert not isRight
                assert json['Data']['rightCode'] == subject_answer_code
                assert json['Code'] == 0 and res.status_code == 200 and res.elapsed.seconds <= 3

            else:
                res = activeqa.post_answer( subjectOrder, subjectId, subject_answer_code, gateId )
                json = res.json
                isRight = json['Data']['isRight']
                assert isRight == True
                assert json['Code'] == 0 and res.status_code == 200 and res.elapsed.seconds <= 3
            time.sleep( 1 )
        # 答题完成后获取玩家信息
        res = activeqa.get_season_player()
        json = res.json
        # 答题完成后，获取当前关卡
        gateId_end = json['Data']['locationGate']
        assert json['Code'] == 0 and res.status_code == 200 and res.elapsed.seconds <= 3
        # 断言金币数量是否增加
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
        if passNeedStar != -1:
            assert ownStar < passNeedStar
            if ownStar > 0:
                assert ownStar_end == ownStar - 1
                assert gateId_end == gateId
                assert unlocked_end
            else:
                assert gateId_end == gateId
                assert ownStar_end == ownStar
                assert unlocked_end

    def test_active_qa_case4(self):
        """错误4题后金币、星星数量增加校验"""
        # 设置错误题目数量
        error_answer_num = 4
        activeqa = ActiveQa()
        activeqa.login( login_name, password )
        res = activeqa.get_season_player()
        json = res.json
        assert json['Code'] == 0 and res.status_code == 200 and res.elapsed.seconds <= 3
        # 获取目前金币数量
        accountBalance_begin = json['Data']['accountBalance']
        # 获取当前关卡
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
        '''获取题目组'''
        res = activeqa.get_question( gateId )
        json = res.json
        assert json['Code'] == 0 and res.status_code == 200 and res.elapsed.seconds <= 3
        # 获取题目编号
        subjectOrder = 0
        # 随机选择题号答错
        error_no_list = random.sample( [1, 2, 3, 4, 5], error_answer_num )
        for subject in json['Data']:
            subjectOrder = subjectOrder + 1
            subjectId = subject['subject']['subjectId']
            # 数据库获取答案
            subject_answer_code = get_active_answer( subjectId )[0]['subject_answer']
            # 调用提交答案接口
            if subjectOrder in error_no_list:
                res = activeqa.post_answer( subjectOrder, subjectId, answer_error( subject_answer_code ), gateId )
                json = res.json
                isRight = json['Data']['isRight']
                assert isRight == False
                assert json['Data']['rightCode'] == subject_answer_code
                assert json['Code'] == 0 and res.status_code == 200 and res.elapsed.seconds <= 3

            else:
                res = activeqa.post_answer( subjectOrder, subjectId, subject_answer_code, gateId )
                json = res.json
                isRight = json['Data']['isRight']
                assert isRight == True
                assert json['Code'] == 0 and res.status_code == 200 and res.elapsed.seconds <= 3
            time.sleep( 1 )
        # 答题完成后获取玩家信息
        res = activeqa.get_season_player()
        json = res.json
        # 答题完成后，获取当前关卡
        gateId_end = json['Data']['locationGate']
        assert json['Code'] == 0 and res.status_code == 200 and res.elapsed.seconds <= 3
        # 断言金币数量是否增加
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
        if passNeedStar != -1:
            assert ownStar < passNeedStar
            if ownStar > 0:
                assert ownStar_end == ownStar - 1
                assert gateId_end == gateId
                assert unlocked_end == True
            else:
                assert gateId_end == gateId
                assert ownStar_end == ownStar
                assert unlocked_end == True

    def test_active_qa_case5(self):
        """错误5题后金币、星星数量增加校验"""
        # 设置错误题目数量
        error_answer_num = 5
        activeqa = ActiveQa()
        activeqa.login( login_name, password )
        res = activeqa.get_season_player()
        json = res.json
        assert json['Code'] == 0 and res.status_code == 200 and res.elapsed.seconds <= 3
        # 获取目前金币数量
        accountBalance_begin = json['Data']['accountBalance']
        # 获取当前关卡
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
        '''获取题目组'''
        res = activeqa.get_question( gateId )
        json = res.json
        assert json['Code'] == 0 and res.status_code == 200 and res.elapsed.seconds <= 3
        # 获取题目编号
        subjectOrder = 0
        # 随机选择题号答错
        error_no_list = random.sample( [1, 2, 3, 4, 5], error_answer_num )
        for subject in json['Data']:
            subjectOrder = subjectOrder + 1
            subjectId = subject['subject']['subjectId']
            # 数据库获取答案
            subject_answer_code = get_active_answer( subjectId )[0]['subject_answer']
            # 调用提交答案接口
            if subjectOrder in error_no_list:
                res = activeqa.post_answer( subjectOrder, subjectId, answer_error( subject_answer_code ), gateId )
                json = res.json
                isRight = json['Data']['isRight']
                assert not isRight
                assert json['Data']['rightCode'] == subject_answer_code
                assert json['Code'] == 0 and res.status_code == 200 and res.elapsed.seconds <= 3

            else:
                res = activeqa.post_answer( subjectOrder, subjectId, subject_answer_code, gateId )
                json = res.json
                isRight = json['Data']['isRight']
                assert isRight == True
                assert json['Code'] == 0 and res.status_code == 200 and res.elapsed.seconds <= 3
            time.sleep( 1 )
        # 答题完成后获取玩家信息
        res = activeqa.get_season_player()
        json = res.json
        # 答题完成后，获取当前关卡
        gateId_end = json['Data']['locationGate']
        assert json['Code'] == 0 and res.status_code == 200 and res.elapsed.seconds <= 3
        # 断言金币数量是否增加
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
        if passNeedStar != -1:
            assert ownStar < passNeedStar
            if ownStar > 0:
                assert ownStar_end == ownStar - 1
                assert gateId_end == gateId
                assert unlocked_end
            else:
                assert gateId_end == gateId
                assert ownStar_end == ownStar
                assert unlocked_end