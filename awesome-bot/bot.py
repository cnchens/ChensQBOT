import os
import nonebot
import config
import pymongo
import time
import json

f = open('config.json', 'r', encoding='utf-8')# 读取config
json_res = json.load(f)
mdb_conn = json_res['mdb_conn']# mongodb连接地址

client = pymongo.MongoClient(mdb_conn)# mongodb连接地址
dblist = client.list_database_names()
if 'QBOT_DB' not in dblist:
    print('首次运行，准备创建数据库')
    print('三秒后开始导入，请等待提示导入完成')
    time.sleep(3)
    
    db = client['QBOT_DB']

    apiuse_col = db['api_use_time']
    apiuse_dict = [
        {'api_name' : 'handrush', 'today' : '0', 'total' : '0'}, 
        {'api_name' : 'rdsimg', 'today' : '0', 'total' : '0'}, 
        {'api_name' : 'rdsfz', 'today' : '0', 'total' : '0'}, 
        {'api_name' : 'finder', 'today' : '0', 'total' : '0'}
    ]
    apiuse_col.insert_many(apiuse_dict)
    print('导入1/6')

    handrush_col = db['handrush']
    handrush_dict = {'qid' : 'x', 'today_rush' : 'x', 'total_rush' : 'x'}
    handrush_col.insert_one(handrush_dict)
    print('导入2/6')

    sfz_col = db['sfz']
    f = open('./awesome-bot/awesome/static/text/新8000w身份证.txt', 'r', encoding='UTF-8')
    n = 0
    for i in f:
        n = n + 1
        sfz_dict = {'sfz_num' : n, 'sfz_info' : i}
        sfz_col.insert_one(sfz_dict)
    print('导入3/6')

    grpmembers_col = db['kick']
    grpmembers_dict = {
                'join_time' : 'x', 
                'grp' : 'x', 
                'status' : 'x', 
                'qid' : 'x', 
                'qqlm' : 'x', 
                'phone' : 'x',
                'phone_location' : 'x', 
                'weibo' : 'x', 
                'lol' : 'x', 
                'real_name' : 'x', 
                'sfz' : 'x', 
                'home_location' : 'x', 
                'else' : 'x'
            }
    grpmembers_col.insert_one(grpmembers_dict)
    print('导入4/6')

    kick_col = db['kick']
    kick_dict = {'kick_time' : 'x', 'kick_grp' : 'x', 'kick_qid' : 'x', 'kick_reason' : 'x'}
    kick_col.insert_one(kick_dict)
    print('导入5/6')

    ban_col = db['kick']
    ban_dict = {'kick_time' : 'x', 'kick_grp' : 'x', 'kick_qid' : 'x', 'kick_reason' : 'x'}
    ban_col.insert_one(ban_dict)
    print('导入6/6')

    print('导入完成')
else:
    print('数据库检查通过，准备运行')
    time.sleep(3)

nonebot.init(config)
bot = nonebot.get_bot()
app = bot.asgi

if __name__ == '__main__':
    nonebot.init(config)
    nonebot.load_builtin_plugins()

    nonebot.load_plugins(
        os.path.join(os.path.dirname(__file__), 'awesome', 'plugins'),
        'awesome.plugins'
    )
    
    nonebot.run()