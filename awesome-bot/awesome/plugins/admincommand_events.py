from nonebot import on_command, CommandSession
import nonebot
import pymongo
import threading
import json
import datetime
import pytz

f = open('config.json', 'r', encoding='utf-8')# 读取config
json_res = json.load(f)
superusers = json_res['superusers']# 超级用户
superusers = set(superusers)# list2set

# mongodb操作
mdb_conn = json_res['mdb_conn']# mongodb连接地址

client = pymongo.MongoClient(mdb_conn)
db = client['BANBOT']# 数据库名称
kick_col = db['kicklist']
ban_col = db['banlist']

@on_command('adminkick')# 踢出
async def _(session: CommandSession):
    bot = nonebot.get_bot()

    s_msg = session.current_arg_text.strip().split()
    req_qid = str(session.event.user_id)
    
    if session.event.user_id in superusers:
        if len(s_msg) != 3:
            await session.send(
                f'''
[CQ:at,qq={req_qid}]
语法错误，示例：
/adminkick [GRPID] [QID] [REASON]
'''.strip()
            )
        else:
            try:
                todo_grpid = s_msg[0]
                if todo_grpid == 'this':
                    todo_grpid = session.event.group_id
                    todo_qid = int(s_msg[1])
                    reason = s_msg[2]

                    await bot.set_group_kick(group_id=todo_grpid, user_id=todo_qid)

                    gmt8 = 'Asia/Shanghai'
                    gmt8_time = datetime.datetime.now(tz=pytz.timezone(gmt8)).strftime('%Y-%m-%d %H:%M:%S')

                    todo_grpid = str(session.event.group_id)
                    todo_qid = s_msg[1]

                    up_dict = {
                        'kick_time' : gmt8_time, 
                        'kick_grp' : todo_grpid, 
                        'kick_qid' : todo_qid, 
                        'kick_reason' : reason, 
                        'performer' : req_qid
                    }

                    kick_col.insert_one(up_dict)

                    await session.send(f'[CQ:at,qq={req_qid}]Kick Success')
                else:
                    todo_grpid = int(s_msg[0])
                    todo_qid = int(s_msg[1])
                    reason = s_msg[2]

                    await bot.set_group_kick(group_id=todo_grpid, user_id=todo_qid)

                    gmt8 = 'Asia/Shanghai'
                    gmt8_time = datetime.datetime.now(tz=pytz.timezone(gmt8)).strftime('%Y-%m-%d %H:%M:%S')

                    todo_grpid = s_msg[0]
                    todo_qid = s_msg[1]

                    up_dict = {
                        'kick_time' : gmt8_time, 
                        'kick_grp' : todo_grpid, 
                        'kick_qid' : todo_qid, 
                        'kick_reason' : reason, 
                        'performer' : req_qid
                    }

                    kick_col.insert_one(up_dict)

                    await session.send(f'[CQ:at,qq={req_qid}]Kick Success')
            except:
                await session.send(f'[CQ:at,qq={req_qid}]Kick Error')
    else:
        pass

@on_command('adminban')# 永久踢出并封禁
async def _(session: CommandSession):
    bot = nonebot.get_bot()

    s_msg = session.current_arg_text.strip().split()
    req_qid = str(session.event.user_id)

    if session.event.user_id in superusers:
        if len(s_msg) != 3:
            await session.send(
                f'''
[CQ:at,qq={req_qid}]
语法错误，示例：
/adminban [GRPID] [QID] [REASON]
'''.strip()
            )
        else:
            try:
                todo_grpid = s_msg[0]
                if todo_grpid == 'this':
                    todo_grpid = session.event.group_id
                    todo_qid = int(s_msg[1])
                    reason = s_msg[2]

                    await bot.set_group_kick(group_id=todo_grpid, user_id=todo_qid)

                    gmt8 = 'Asia/Shanghai'
                    gmt8_time = datetime.datetime.now(tz=pytz.timezone(gmt8)).strftime('%Y-%m-%d %H:%M:%S')

                    todo_grpid = str(session.event.group_id)
                    todo_qid = s_msg[1]

                    up_dict = {
                        'ban_time' : gmt8_time, 
                        'ban_grp' : todo_grpid, 
                        'ban_qid' : todo_qid, 
                        'ban_reason' : reason, 
                        'performer' : req_qid
                    }

                    ban_col.insert_one(up_dict)

                    await session.send(f'[CQ:at,qq={req_qid}]Ban Success')
                else:
                    todo_grpid = int(s_msg[0])
                    todo_qid = int(s_msg[1])
                    reason = s_msg[2]

                    await bot.set_group_kick(group_id=todo_grpid, user_id=todo_qid)

                    gmt8 = 'Asia/Shanghai'
                    gmt8_time = datetime.datetime.now(tz=pytz.timezone(gmt8)).strftime('%Y-%m-%d %H:%M:%S')

                    todo_grpid = s_msg[0]
                    todo_qid = s_msg[1]

                    up_dict = {
                        'ban_time' : gmt8_time, 
                        'ban_grp' : todo_grpid, 
                        'ban_qid' : todo_qid, 
                        'ban_reason' : reason, 
                        'performer' : req_qid
                    }

                    ban_col.insert_one(up_dict)

                    await session.send(f'[CQ:at,qq={req_qid}]Ban Success')
            except:
                gmt8 = 'Asia/Shanghai'
                gmt8_time = datetime.datetime.now(tz=pytz.timezone(gmt8)).strftime('%Y-%m-%d %H:%M:%S')

                todo_grpid = s_msg[0]
                todo_qid = s_msg[1]
                reason = s_msg[2]

                up_dict = {
                    'ban_time' : gmt8_time, 
                    'ban_grp' : todo_grpid, 
                    'ban_qid' : todo_qid, 
                    'ban_reason' : reason, 
                    'performer' : req_qid
                }

                ban_col.insert_one(up_dict)

                await session.send(f'[CQ:at,qq={req_qid}]Ban Error, but also added to ban_col')
    else:
        pass
