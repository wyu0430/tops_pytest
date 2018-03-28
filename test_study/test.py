# coding=utf-8
import json
import random


def answer_error(answer):
    answer_list = [1, 2, 3, 4]
    answer_list.remove( answer )
    error_answer = random.sample( answer_list, 1 )
    return error_answer[0]


def dict_to_json(dictionary):
    if type( dictionary ) == dict:
        return json.dumps( dictionary )
    else:
        return 'error dict'


def json_to_dict(json_str):
    try:
        return json.loads( json_str )
    except:
        return 'error json'


a = 1.23456
print round( a, 2 )
