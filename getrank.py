# -*- coding: utf-8 -*-

import sys
from pymongo import MongoClient

def get_rank(user_id):
    client = MongoClient()
    db = client.shiyanlou
    contests = db.contests

    #计算用户 user_id 排名、总分、花费时间
    
    #计算排名



    #计算总分
    def get_score():
        total = 0
        for scores in db.contests.find({'user_id':user_id}):
            total += scores['score']
        print total

    #计算时间
    def get_times():
        times = 0
        for time in db.contests.find({'user_id':user_id}):
            times += time['submit_time']
        print(times)

    #依次返回排名，分数，时间
    return rank, score, submit_time

if __name__ == '__main__':

    '''
    1. 判断参数格式是否符合要求
    2. 获取 user_id 参数
    '''
    user_id = sys.argv[1]

    #根据用户ID获取用户排名、分数、时间
    userdata = get_rank(user_id)
    print(userdata)
