# coding=utf-8
import unittest
import time
from Apis.broker_active_api import ActiveQa
from db.db_active import get_active_answer
import random

# gateId = 12

def answer_error(answer):
    answer_list = ['1', '2', '3', '0']
    answer_list.remove(answer)
    error_answer = random.sample(answer_list, 1)
    return error_answer[0]

from common import public_configure

login_name = "15157163734"
password = "147852"


class TestActiveQaCase( unittest.TestCase ):
    def test_active_qa_case(self):
        """第一关全部回答正确后金币增加校验"""
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
        # 获取关卡需要的金币数量
        for i in json['Data']['seasonGates']:
            if i['gateId'] == gateId:
                enterNeedGold = i['enterNeedGold']
        '''获取题目组'''
        res = activeqa.get_question( gateId )
        json = res.json
        assert json['Code'] == 0 and res.status_code == 200 and res.elapsed.seconds <= 3
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
            assert isRight == True
            assert json['Code'] == 0 and res.status_code == 200 and res.elapsed.seconds <= 3
            time.sleep(1)
        # 答题完成后获取玩家信息
        res = activeqa.get_season_player()
        json = res.json
        assert json['Code'] == 0 and res.status_code == 200 and res.elapsed.seconds <= 3
        # 断言金币数量是否增加
        accountBalance_end = json['Data']['accountBalance']
        assert accountBalance_end == accountBalance_begin + enterNeedGold

    def test_active_qa_case1(self):
        """第一关错误1题后金币增加校验"""
        # 错误题目数量
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
        # 获取关卡需要的金币数量
        for i in json['Data']['seasonGates']:
            if i['gateId'] ==gateId:
                enterNeedGold = i['enterNeedGold']
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
        assert json['Code'] == 0 and res.status_code == 200 and res.elapsed.seconds <= 3
        # 断言金币数量是否增加
        accountBalance_end = json['Data']['accountBalance']
        assert accountBalance_end == accountBalance_begin + enterNeedGold

    def test_active_qa_case2(self):
        """第一关错误2题后金币增加校验"""
        # 错误题目数量
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
        # 获取关卡需要的金币数量
        for i in json['Data']['seasonGates']:
            if i['gateId'] == gateId:
                enterNeedGold = i['enterNeedGold']
        '''获取题目组'''
        res = activeqa.get_question( gateId )
        json = res.json
        assert json['Code'] == 0 and res.status_code == 200 and res.elapsed.seconds <= 3
        # 获取题目编号
        subjectOrder = 0
        # 随机选择题号答错
        error_no_list = random.sample( [1, 2, 3, 4, 5], error_answer_num)
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
        assert json['Code'] == 0 and res.status_code == 200 and res.elapsed.seconds <= 3
        # 断言金币数量是否增加
        accountBalance_end = json['Data']['accountBalance']
        assert accountBalance_end == accountBalance_begin + enterNeedGold

    def test_active_qa_case3(self):
        """第一关错误3题后金币增加校验"""
        # 错误题目数量
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
        # 获取关卡需要的金币数量
        for i in json['Data']['seasonGates']:
            if i['gateId'] == gateId:
                enterNeedGold = i['enterNeedGold']
        '''获取题目组'''
        res = activeqa.get_question( gateId )
        json = res.json
        assert json['Code'] == 0 and res.status_code == 200 and res.elapsed.seconds <= 3
        # 获取题目编号
        subjectOrder = 0
        # 随机选择题号答错
        error_no_list = random.sample( [1, 2, 3, 4, 5], error_answer_num)
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
        assert json['Code'] == 0 and res.status_code == 200 and res.elapsed.seconds <= 3
        # 断言金币数量是否增加
        accountBalance_end = json['Data']['accountBalance']
        assert accountBalance_end == accountBalance_begin - enterNeedGold

    def test_active_qa_case4(self):
        """第一关错误4题后金币减少校验"""
        # 错误题目数量
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
        # 获取关卡需要的金币数量
        for i in json['Data']['seasonGates']:
            if i['gateId'] == gateId:
                enterNeedGold = i['enterNeedGold']
        '''获取题目组'''
        res = activeqa.get_question( gateId )
        json = res.json
        assert json['Code'] == 0 and res.status_code == 200 and res.elapsed.seconds <= 3
        # 获取题目编号
        subjectOrder = 0
        # 随机选择题号答错
        error_no_list = random.sample( [1, 2, 3, 4, 5], error_answer_num)
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
        assert json['Code'] == 0 and res.status_code == 200 and res.elapsed.seconds <= 3
        # 断言金币数量是否增加
        accountBalance_end = json['Data']['accountBalance']
        assert accountBalance_end == accountBalance_begin - enterNeedGold

    def test_active_qa_case5(self):
        """第一关错误5题后金币增加校验"""
        # 错误题目数量
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
        # 获取关卡需要的金币数量
        for i in json['Data']['seasonGates']:
            if i['gateId'] == gateId:
                enterNeedGold = i['enterNeedGold']
        '''获取题目组'''
        res = activeqa.get_question( gateId )
        json = res.json
        assert json['Code'] == 0 and res.status_code == 200 and res.elapsed.seconds <= 3
        # 获取题目编号
        subjectOrder = 0
        # 随机选择题号答错
        error_no_list = random.sample( [1, 2, 3, 4, 5], error_answer_num)
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
        assert json['Code'] == 0 and res.status_code == 200 and res.elapsed.seconds <= 3
        # 断言金币数量是否增加
        accountBalance_end = json['Data']['accountBalance']
        assert accountBalance_end == accountBalance_begin - enterNeedGold