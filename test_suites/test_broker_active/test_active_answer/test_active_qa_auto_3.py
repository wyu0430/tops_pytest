# coding=utf-8
import unittest
import time
from Apis.broker_active_api import ActiveQa
from db.db_active import get_active_answer
from random import choice
from common import public_configure
import random
import thread

import random


def answer_error(answer):
    answer_list = ['1', '2', '3', '0']
    answer_list.remove(answer)
    error_answer = random.sample(answer_list, 1)
    return error_answer[0]


# login_name = "15757184409"
# password = "a123456"
login_name = "15157163734"
password = "147852"

class TestActiveQaCase3( unittest.TestCase ):
    def test_active_qa_case3(self):
        Answered_questions = []
        for j in range(17880000201, 17880000300):
            login_name = str(j)
            password = "123123456"
            count = random.uniform( 2, 3 )
            for i in range( 1, int(count) ):
                '''随机调用排行版接口'''
                """------------------------------"""
                random_phb = random.uniform( 1, 3 )
                if random_phb == 2:
                    activeqa = ActiveQa()
                    activeqa.login( login_name, password )
                    res = activeqa.get_season_player()
                    json = res.json
                    assert json['Code'] == 0 and res.status_code == 200 and res.elapsed.seconds <= 3
                    seasonId = json['Data']['seasonId']
                    res = activeqa.get_active_rank( seasonId )
                    json = res.json
                    assert json['Code'] == 0 and res.status_code == 200 and res.elapsed.seconds <= 3
                """------------------------------"""
                """全部回答正确后金币增加校验"""
                activeqa = ActiveQa()
                activeqa.login( login_name, password )
                res = activeqa.get_season_player()
                json = res.json
                assert json['Code'] == 0 and res.status_code == 200 and res.elapsed.seconds <= 3
                # 获取目前金币数量
                accountBalance_begin = json['Data']['accountBalance']
                # 获取当前关卡
                gateId = json['Data']['locationGate']

                """断言获取星星数量与关卡星星数量总和是否一致"""
                """-----------------------------------"""
                accountBalance_begin = json['Data']['accountBalance']
                # 获取星星总数
                gotStarNum = json['Data']['gotStarNum']
                # 获取当前所在关卡
                locationGate = json['Data']['locationGate']
                # 当前关卡星星数量
                locationGateStarNum = json['Data']['locationGateStarNum']
                # 断言星星总数与关卡星星数是否相符合
                need_star_list = [1, 2, 3, 4, 5, 5, 6, 8]
                star_sum = 0
                for i in range( 0, locationGate - 1 ):
                    star_sum = need_star_list[i] + star_sum
                star_sum = star_sum + locationGateStarNum
                assert star_sum == gotStarNum
                # 获取当前关卡，用于获取关卡需要的金币数量
                gateId = json['Data']['locationGate']
                """获取当前关卡信息"""
                res = activeqa.get_season_gates()
                json = res.json
                assert json['Code'] == 0 and res.status_code == 200 and res.elapsed.seconds <= 3
                """-----------------------------------"""

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
                    if subjectId in Answered_questions:
                        print Answered_questions
                    # assert subjectId not in Answered_questions, "断言是否出现了重复题目"
                    Answered_questions.append(subjectId)
                    # 数据库获取答案
                    subject_answer_code = get_active_answer( subjectId )[0]['subject_answer']
                    # 调用提交答案接口
                    res = activeqa.post_answer( subjectOrder, subjectId, subject_answer_code, gateId )
                    json = res.json
                    isRight = json['Data']['isRight']
                    assert isRight
                    assert json['Code'] == 0 and res.status_code == 200 and res.elapsed.seconds <= 3
                    # time.sleep( 0.01 )
                # 答题完成后获取玩家信息
                res = activeqa.get_season_player()
                json = res.json
                assert json['Code'] == 0 and res.status_code == 200 and res.elapsed.seconds <= 3
                # 断言金币数量是否增加
                accountBalance_end = json['Data']['accountBalance']
                assert accountBalance_end == accountBalance_begin + enterNeedGold
            print Answered_questions
