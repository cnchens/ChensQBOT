from nonebot import on_notice, NoticeSession
from urllib.request import Request, urlopen
from urllib.parse import urlencode
import json
import pymongo
import ast
import datetime
import pytz

f = open('config.json', 'r', encoding='utf-8')# 读取config
json_res = json.load(f)

# mongodb操作
mdb_conn = json_res['mdb_conn']# mongodb连接地址

client = pymongo.MongoClient(mdb_conn)
db = client['QBOT_DB']# 数据库名称
grp_col = db['grp_members']

# 入群
@on_notice('group_increase')
async def _(session: NoticeSession):
    notice_group_increase = json_res['notice_group_increase']
    group_increase_dict_enable = notice_group_increase['enable']
    group_increase_dict_method = notice_group_increase['method']
    group_increase_dict_notice_msg = notice_group_increase['notice_msg']

    if group_increase_dict_enable == 'true':
        grpid = session.event.group_id
        grpid = str(grpid)
        at_qid = session.event.user_id
        at_qid = str(at_qid)

    notice_group_increase = json_res['notice_group_increase']
    group_increase_dict_enable = notice_group_increase['enable']
    group_increase_dict_method = notice_group_increase['method']
    group_increase_dict_notice_msg = notice_group_increase['notice_msg']

    if group_increase_dict_enable == 'true':
        if group_increase_dict_method == 'special':
            pass
        elif group_increase_dict_method == 'basic':
            at_qid = session.event.user_id
            await session.send(f'[CQ:at,qq={at_qid}]' + group_increase_dict_notice_msg)
        else:
            pass

        finder_qid = at_qid
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
            repo_phone = '没有找到'
            repo_ph_place = '没有找到'

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

    elif group_increase_dict_enable == 'false':
        pass
    else:
        pass
    

# 退群
@on_notice('group_decrease')
async def _(session: NoticeSession):
    notice_group_decrease = json_res['notice_group_decrease']
    group_decrease_dict_enable = notice_group_decrease['enable']

    if group_decrease_dict_enable == 'true':
        grpid = session.event.group_id
        grpid = str(grpid)
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
            
        if type == 'leave':
            send_message = '退群 ' + '退群原因：' + '主动退群（leave） 离开者：' + op_qid
            await session.send(send_message)
        elif type == 'kick':
            send_message = '退群 ' + '退群原因：' + '被踢出（kick） 操作者：' + op_qid
            await session.send(send_message)
        else:
            send_message = '退群 ' + '退群原因：' + '未知（' + type + '）' + '操作者/离开者：' + op_qid
            await session.send(send_message)
    elif group_decrease_dict_enable == 'false':
        pass
    else:
        pass