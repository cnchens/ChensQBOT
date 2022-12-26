from nonebot import on_command, CommandSession
import pymongo
import threading
import json

f = open('config.json', 'r', encoding='utf-8')# 读取config
json_res = json.load(f)
superusers = json_res['superusers']# 超级用户
superusers = set(superusers)# list2set

@on_command('adminkick')
async def _(session: CommandSession):
    req_qid = str(session.event.user_id)

    if session.event.user_id in superusers: