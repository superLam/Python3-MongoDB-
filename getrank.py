# -*- coding: utf-8 -*-

import sys
from pymongo import MongoClient

def get_rank(user_id):
    #读取数据
    client = MongoClient()
    db = client.shiyanlou
    contests = db.contests

    #计算总分和时间
    
    times = 0
    scores = 0
    for score in db.contests.find({'user_id':user_id}):
        scores += score['score']
    for time in db.contests.find({'user_id':user_id}):
        times += time['submit_time']
    

    #依次返回分数，时间
    return  scores, times

if __name__ == '__main__':

    #获取用户id,python3 getrank.py 2,获取的就是id为2
    user_id = sys.argv[1]

    #根据用户ID获取分数、时间,需要输入int类型
    userdata = get_rank(int(user_id))  
    print(userdata)
