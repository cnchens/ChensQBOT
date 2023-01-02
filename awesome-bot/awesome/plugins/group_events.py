from nonebot import on_notice, NoticeSession
from urllib.request import Request, urlopen
from urllib.parse import urlencode
import urllib.error
import json
import pymongo
import ast
import datetime
import pytz
import time
import nonebot

f = open('config.json', 'r', encoding='utf-8')# 读取config
json_res = json.load(f)

# mongodb操作
mdb_conn = json_res['mdb_conn']# mongodb连接地址

client = pymongo.MongoClient(mdb_conn)
db = client['BANBOT']# 数据库名称
grp_col = db['grp_members']
ban_col = db['banlist']
kick_col = db['kicklist']

# 入群
@on_notice('group_increase')
async def _(session: NoticeSession):
    bot = nonebot.get_bot()
    at_qid = str(session.event.user_id)
    for i in ban_col.find():
        if at_qid in i['ban_qid']:
            await session.send(f'[CQ:at,qq={at_qid}]自动踢出：您已经被本群封禁，如需解除请联系群主或群管理员！')
            kick_grpid = session.event.group_id
            kick_qid = session.event.user_id
            time.sleep(1)
            await bot.set_group_kick(group_id=kick_grpid, user_id=kick_qid)

            gmt8 = 'Asia/Shanghai'
            gmt8_time = datetime.datetime.now(tz=pytz.timezone(gmt8)).strftime('%Y-%m-%d %H:%M:%S')

            kick_grpid = str(kick_grpid)
            kick_qid = str(kick_qid)
            up_dict = {
                'kick_time' : gmt8_time, 
                'kick_grp' : kick_grpid, 
                'kick_qid' : kick_qid, 
                'kick_reason' : 'Automatic Kick by banlist', 
                'performer' : 'BOT'
            }

            kick_col.insert_one(up_dict)
            break
        else:
            pass

    grpid = str(session.event.group_id)
    at_qid = str(session.event.user_id)

    if grpid == '760327885':# aniakt
        await session.send(f'[CQ:at,qq={at_qid}]进群看公告\n群公告仔细看完，如果还有问题的再来找我')
    elif grpid == '706125200':# only
        await session.send(f'[CQ:at,qq={at_qid}]进群是吧，给我撅三回啊三回')
    elif grpid == '544033107':# gsakt
        await session.send(f'[CQ:at,qq={at_qid}]进群是吧，给我撅三回啊三回')
    elif grpid == '511824025':# akt4
        await session.send(f'[CQ:at,qq={at_qid}]欢迎入群，入群看群文件，里面东西失效不补，不禁言群是实时更新的')
    elif grpid == '317096220':# akt2
        await session.send(f'[CQ:at,qq={at_qid}]进群看公告，有事找群主')
    elif grpid == '730804591':# akt3
        await session.send(f'[CQ:at,qq={at_qid}]加新群760327885')
    elif grpid == '793395527':# 原神崩坏交流群
        await session.send(f'[CQ:at,qq={at_qid}]进群看公告，有事找群主')
    else:
        pass

    finder_qid = at_qid

    # gmt8_time = '无法获取'
    # repo_qqlm = '无法获取'
    # repo_phone = '无法获取'
    # repo_ph_place = '无法获取'
    # repo_wid = '无法获取'
    # repo_lol = '无法获取'

    try:
        global repo_phone, repo_ph_place
        ua = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.47'}
        url = 'https://api.xywlapi.cc/qqapi'
        data = {'qq' : finder_qid}
        data = urlencode(data).encode('UTF-8')
        requ = Request(url=url, data=data, headers=ua)

        repo = urlopen(requ).read()
        brepo_str = repo.decode()
        brepo_dict = ast.literal_eval(brepo_str)
        repo_stat = brepo_dict['status']
        if repo_stat == 200:
            repo_phone = brepo_dict['phone']
            repo_ph_place = brepo_dict['phonediqu']
        else:
            repo_phone = '没有找到'
            repo_ph_place = '没有找到'
    except:
        repo_phone = '获取失败'
        repo_ph_place = '获取失败'

    try:
        global repo_wid
        ua = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.47'}
        url = 'https://api.xywlapi.cc/qqapi'
        data = {'qq' : finder_qid}
        data = urlencode(data).encode('UTF-8')
        requ = Request(url=url, data=data, headers=ua)

        repo = urlopen(requ).read()
        brepo_str = repo.decode()
        brepo_dict = ast.literal_eval(brepo_str)
        repo_stat = brepo_dict['status']
        if repo_stat == 200:
            repo_phone = brepo_dict['phone']
            repo_ph_place = brepo_dict['phonediqu']
            ua = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.47'}
            url = 'https://api.xywlapi.cc/wbphone'
            data = {'phone' : repo_phone}
            data = urlencode(data).encode('UTF-8')
            requ = Request(url=url, data=data, headers=ua)
            repo = urlopen(requ).read()
            brepo_str = repo.decode()
            brepo_dict = ast.literal_eval(brepo_str)
            repo_stat = brepo_dict['status']
            if repo_stat == 200:
                repo_wid = brepo_dict['id']
            else:
                repo_wid = '没有找到'
        else:
            repo_wid = '没有找到'
    except:
        repo_wid = '获取失败'

    try:
        global repo_lol
        ua = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.47'}
        url = 'https://api.xywlapi.cc/qqlol'
        data = {'qq' : finder_qid}
        data = urlencode(data).encode('UTF-8')
        requ = Request(url=url, data=data, headers=ua)

        repo = urlopen(requ).read()
        brepo_str = repo.decode()
        brepo_dict = ast.literal_eval(brepo_str)
        repo_stat = brepo_dict['status']
        if repo_stat == 200:
            repo_lol_name = brepo_dict['name']
            repo_daqu = brepo_dict['daqu']
            repo_lol = repo_lol_name + repo_daqu
        else:
            repo_lol = '没有找到'
    except:
        repo_lol = '获取失败'

    try:
        global repo_qqlm
        ua = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.47'}
        url = 'https://api.xywlapi.cc/qqlm'
        data = {'qq' : finder_qid}
        data = urlencode(data).encode('UTF-8')
        requ = Request(url=url, data=data, headers=ua)

        repo = urlopen(requ).read()
        brepo_str = repo.decode()
        brepo_dict = ast.literal_eval(brepo_str)
        repo_stat = brepo_dict['status']
        if repo_stat == 200:
            repo_qqlm = brepo_dict['qqlm']
        else:
            repo_qqlm = '没有找到'
    except:
        repo_qqlm = '获取失败'

    gmt8 = 'Asia/Shanghai'
    gmt8_time = datetime.datetime.now(tz=pytz.timezone(gmt8)).strftime('%Y-%m-%d %H:%M:%S')

    add_dict = {
        'join_time' : gmt8_time, 
        'grp' : grpid, 
        'status' : 'in_grp', 
        'qid' : at_qid, 
        'qqlm' : repo_qqlm, 
        'phone' : repo_phone,
        'phone_location' : repo_ph_place, 
        'weibo' : repo_wid, 
        'lol' : repo_lol, 
        'real_name' : '无', 
        'sfz' : '无', 
        'home_location' : '无', 
        'else' : '无'
    }

    grp_col.insert_one(add_dict)

# 退群
@on_notice('group_decrease')
async def _(session: NoticeSession):
    grpid = str(session.event.group_id)
    type = session.event.sub_type
    op_qid = str(session.event.operator_id)

    for i in grp_col.find():
        if op_qid in i['qid']:
            db_qid = i['qid']
            u_qid = {'qid' : db_qid}
            u_stat = {'$set' : {'status' : type}}
            grp_col.update_many(u_qid, u_stat)
            break
        else:
            pass

    # if grpid != '760327885':
    #     if type == 'leave':
    #         send_message = '退群 ' + '退群原因：' + '主动退群（leave） 离开者：' + op_qid
    #         await session.send(send_message)
    #     elif type == 'kick':
    #         send_message = '退群 ' + '退群原因：' + '被踢出（kick） 操作者：' + op_qid
    #         await session.send(send_message)
    #     else:
    #         send_message = '退群 ' + '退群原因：' + '未知（' + type + '）' + '操作者/离开者：' + op_qid
    #         await session.send(send_message)
    # else:
    #     pass
