from nonebot import on_command, CommandSession
from urllib.request import Request, urlopen
from urllib.parse import urlencode
import datetime
import pytz
import ast
import pymongo
import threading
import random
import re
import json

f = open('config.json', 'r', encoding='utf-8')# 读取config
json_res = json.load(f)

enable_allcmd = json_res['enable_allcmd']
enable_time = json_res['enable_time']
enable_finder = json_res['enable_finder']
enable_rdsfz = json_res['enable_rdsfz']
enable_tfish = json_res['enable_tfish']
enable_handrush = json_res['enable_handrush']
enable_rdsimg = json_res['enable_rdsimg']

# mongodb操作
mdb_conn = json_res['mdb_conn']# mongodb连接地址

client = pymongo.MongoClient(mdb_conn)
db = client['QBOT_DB']# 数据库名称
apiuse_col = db['api_use_time']# 调用情况集合
sfz_col = db['sfz']# 身份证存储集合
handrush_col = db['handrush']# 手冲集合

# 所有指令
@on_command('allcmd')
async def _(session: CommandSession):
    if enable_allcmd == 'true':
        req_qid = str(session.event.user_id)
        await session.send(
            f'''
            [CQ:at,qq={req_qid}]All Commands

            用法：@Chens_QBOT [命令]

            命令：
            基本：
                allcmd      显示本命令
                time        显示当前时间
            查询类：
                finder      查询各种数据
                rdsfz       随机身份证
                tfish       摸鱼
            R18：
                handrush    是否手冲
                rdsimg      随机涩图
            '''.strip()
        )
    elif enable_allcmd == 'false':
        pass
    else:
        pass

# 指令报时
@on_command('time')
async def _(session: CommandSession):
    if enable_time == 'true':
        req_qid = str(session.event.user_id)

        gmt8 = 'Asia/Shanghai'
        ymd = datetime.datetime.now(tz=pytz.timezone(gmt8)).strftime('%Y-%m-%d')
        gmt8_time = datetime.datetime.now(tz=pytz.timezone(gmt8)).strftime('%H:%M:%S')
        await session.send(f'[CQ:at,qq={req_qid}]当前GMT+8 Time是：\n{ymd} {gmt8_time}')
    elif enable_time == 'false':
        pass
    else:
        pass

# 社工库查找
@on_command('finder')
async def _(session: CommandSession):
    if enable_finder == 'true':
        for i in apiuse_col.find():
            if 'finder' in i['api_name']:
                today_apiuse = int(i['today'])
                total_apiuse = int(i['total'])
                send_apiname = {'api_name' : 'finder'}
                apiuse_today = {'$set' : {'today' : str(today_apiuse + 1)}}
                apiuse_total = {'$set' : {'total' : str(total_apiuse + 1)}}
                apiuse_col.update_many(send_apiname, apiuse_today)
                apiuse_col.update_many(send_apiname, apiuse_total)
                break
            else:
                pass

        s_msg = session.current_arg_text.strip()
        req_qid = str(session.event.user_id)
        if not s_msg:
            s_msg = (
                await session.aget(
                    prompt=f'''
                    [CQ:at,qq={req_qid}]查询内容不能为空
                    使用示例：
                        @Chens_QBOT finder [MODE] [INFO]

                    MODE：查找模式（必需）
                        q2p 通过QQ号查询密保手机
                        p2q 手机号查询绑定QQ
                        q2l QQ号查询LOL信息
                        l2q LOL查询QQ信息
                        q2pwd QQ号查询老密
                        w2p 微博通过ID查手机号
                        p2w 微博通过手机号查ID
                        sms 短轰

                    INFO：要查询的信息（必需）
                        一般为qid或手机号
                    '''.strip()
                ))
            while not s_msg:
                await session.aget(
                    prompt=f'''
                    [CQ:at,qq={req_qid}]查询内容不能为空
                    使用示例：
                        @Chens_QBOT finder [MODE] [INFO]

                    MODE：查找模式（必需）
                        q2p 通过QQ号查询密保手机
                        p2q 手机号查询绑定QQ
                        q2l QQ号查询LOL信息
                        l2q LOL查询QQ信息
                        q2pwd QQ号查询老密
                        w2p 微博通过ID查手机号
                        p2w 微博通过手机号查ID
                        sms 短轰

                    INFO：要查询的信息（必需）
                        一般为qid或手机号
                    '''.strip()
                )

        sp_msg = s_msg.split()

        if len(sp_msg) == 1:
            await session.send(
                    f'''
                    [CQ:at,qq={req_qid}]INFO不能为空
                    使用示例：
                        @Chens_QBOT finder [MODE] [INFO]

                    MODE：查找模式（必需）
                        q2p 通过QQ号查询密保手机
                        p2q 手机号查询绑定QQ
                        q2l QQ号查询LOL信息
                        l2q LOL查询QQ信息
                        q2pwd QQ号查询老密
                        w2p 微博通过ID查手机号
                        p2w 微博通过手机号查ID
                        sms 短轰

                    INFO：要查询的信息（必需）
                        一般为qid或手机号
                    '''.strip()
                )

        elif len(sp_msg) == 2:
            if sp_msg[0] == 'q2p':# 通过QQ号查询密保手机
                ua = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.47'}
                url = 'https://api.xywlapi.cc/qqapi'
                data = {'qq' : sp_msg[1]}
                data = urlencode(data).encode('UTF-8')
                requ = Request(url=url, data=data, headers=ua)
                repo = urlopen(requ).read()
                brepo_str = repo.decode()
                brepo_dict = ast.literal_eval(brepo_str)

                repo_stat = brepo_dict['status']
                if repo_stat == 200:
                    repo_msg = brepo_dict['message']
                    repo_qid = brepo_dict['qq']
                    repo_phone = brepo_dict['phone']
                    repo_ph_place = brepo_dict['phonediqu']
                    send_message = f'[CQ:at,qq={req_qid}]finder StatusCode：{repo_stat} {repo_msg}\n查询qid：{repo_qid}\n绑定手机：{repo_phone}\n归属地：{repo_ph_place}'
                    await session.send(send_message)
                else:
                    repo_msg = brepo_dict['message']
                    send_message = f'[CQ:at,qq={req_qid}]finder StatusCode：{repo_stat} {repo_msg}'
                    await session.send(send_message)

            elif sp_msg[0] == 'p2q':# 手机号查询绑定QQ
                ua = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.47'}
                url = 'https://api.xywlapi.cc/qqphone'
                data = {'phone' : sp_msg[1]}
                data = urlencode(data).encode('UTF-8')
                requ = Request(url=url, data=data, headers=ua)
                repo = urlopen(requ).read()
                brepo_str = repo.decode()
                brepo_dict = ast.literal_eval(brepo_str)

                repo_stat = brepo_dict['status']
                if repo_stat == 200:
                    repo_msg = brepo_dict['message']
                    repo_qid = brepo_dict['qq']
                    repo_phone = sp_msg[1]
                    repo_ph_place = brepo_dict['phonediqu']
                    send_message = f'[CQ:at,qq={req_qid}]finder StatusCode：{repo_stat} {repo_msg}\n查询手机：{repo_phone}\n绑定qid：{repo_qid}\n归属地：{repo_ph_place}'
                    await session.send(send_message)
                else:
                    repo_msg = brepo_dict['message']
                    send_message = f'[CQ:at,qq={req_qid}]finder StatusCode：{repo_stat} {repo_msg}'
                    await session.send(send_message)

            elif sp_msg[0] == 'q2l':# QQ号查询LOL信息
                ua = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.47'}
                url = 'https://api.xywlapi.cc/qqlol'
                data = {'qq' : sp_msg[1]}
                data = urlencode(data).encode('UTF-8')
                requ = Request(url=url, data=data, headers=ua)
                repo = urlopen(requ).read()
                brepo_str = repo.decode()
                brepo_dict = ast.literal_eval(brepo_str)

                repo_stat = brepo_dict['status']
                if repo_stat == 200:
                    repo_msg = brepo_dict['message']
                    repo_qid = brepo_dict['qq']
                    repo_name = brepo_dict['name']
                    repo_daqu = brepo_dict['daqu']
                    send_message = f'[CQ:at,qq={req_qid}]finder StatusCode：{repo_stat} {repo_msg}\n查询qid：{repo_qid}\n游戏名：{repo_name}\n服务器：{repo_daqu}'
                    await session.send(send_message)
                else:
                    repo_msg = brepo_dict['message']
                    send_message = f'[CQ:at,qq={req_qid}]finder StatusCode：{repo_stat} {repo_msg}'
                    await session.send(send_message)

            elif sp_msg[0] == 'l2q':# LOL查询QQ信息
                ua = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.47'}
                url = 'https://api.xywlapi.cc/lolname'
                data = {'name' : sp_msg[1]}
                data = urlencode(data).encode('UTF-8')
                requ = Request(url=url, data=data, headers=ua)
                repo = urlopen(requ).read()
                brepo_str = repo.decode()
                brepo_dict = ast.literal_eval(brepo_str)

                repo_stat = brepo_dict['status']
                if repo_stat == 200:
                    repo_msg = brepo_dict['message']
                    repo_qid = brepo_dict['qq']
                    repo_name = brepo_dict['name']
                    repo_daqu = brepo_dict['daqu']
                    send_message = f'[CQ:at,qq={req_qid}]finder StatusCode：{repo_stat} {repo_msg}\n查询游戏名：{repo_name}\n服务器：{repo_daqu}\n绑定qid：{repo_qid}'
                    await session.send(send_message)
                else:
                    repo_msg = brepo_dict['message']
                    send_message = f'[CQ:at,qq={req_qid}]finder StatusCode：{repo_stat} {repo_msg}'
                    await session.send(send_message)

            elif sp_msg[0] == 'q2pwd':# QQ号查询老密
                ua = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.47'}
                url = 'https://api.xywlapi.cc/qqlm'
                data = {'qq' : sp_msg[1]}
                data = urlencode(data).encode('UTF-8')
                requ = Request(url=url, data=data, headers=ua)
                repo = urlopen(requ).read()
                brepo_str = repo.decode()
                brepo_dict = ast.literal_eval(brepo_str)

                repo_stat = brepo_dict['status']
                if repo_stat == 200:
                    repo_msg = brepo_dict['message']
                    repo_qid = brepo_dict['qq']
                    repo_qqlm = brepo_dict['qqlm']
                    send_message = f'[CQ:at,qq={req_qid}]finder StatusCode：{repo_stat} {repo_msg}\n查询qid：{repo_qid}\nlm_id：{repo_qqlm}'
                    await session.send(send_message)
                else:
                    repo_msg = brepo_dict['message']
                    send_message = f'[CQ:at,qq={req_qid}]finder StatusCode：{repo_stat} {repo_msg}'
                    await session.send(send_message)

            elif sp_msg[0] == 'w2p':# 微博通过ID查手机号
                ua = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.47'}
                url = 'https://api.xywlapi.cc/wbapi'
                data = {'id' : sp_msg[1]}
                data = urlencode(data).encode('UTF-8')
                requ = Request(url=url, data=data, headers=ua)
                repo = urlopen(requ).read()
                brepo_str = repo.decode()
                brepo_dict = ast.literal_eval(brepo_str)

                repo_stat = brepo_dict['status']
                if repo_stat == 200:
                    repo_msg = brepo_dict['message']
                    wid = sp_msg[1]
                    repo_phone = brepo_dict['phone']
                    repo_ph_place = brepo_dict['phonediqu']
                    send_message = f'[CQ:at,qq={req_qid}]finder StatusCode：{repo_stat} {repo_msg}\n查询微博id：{wid}\n绑定手机：{repo_phone}\n归属地：{repo_ph_place}'
                    await session.send(send_message)
                else:
                    repo_msg = brepo_dict['message']
                    send_message = f'[CQ:at,qq={req_qid}]finder StatusCode：{repo_stat} {repo_msg}'
                    await session.send(send_message)

            elif sp_msg[0] == 'p2w':# 微博通过手机号查ID
                ua = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.47'}
                url = 'https://api.xywlapi.cc/wbphone'
                data = {'phone' : sp_msg[1]}
                data = urlencode(data).encode('UTF-8')
                requ = Request(url=url, data=data, headers=ua)
                repo = urlopen(requ).read()
                brepo_str = repo.decode()
                brepo_dict = ast.literal_eval(brepo_str)

                repo_stat = brepo_dict['status']
                if repo_stat == 200:
                    repo_msg = brepo_dict['message']
                    phone = sp_msg[1]
                    repo_wid = brepo_dict['id']
                    repo_ph_place = brepo_dict['phonediqu']
                    send_message = f'[CQ:at,qq={req_qid}]finder StatusCode：{repo_stat} {repo_msg}\n查询手机：{phone}\n绑定微博id：{repo_wid}\n归属地：{repo_ph_place}'
                    await session.send(send_message)
                else:
                    repo_msg = brepo_dict['message']
                    send_message = f'[CQ:at,qq={req_qid}]finder StatusCode：{repo_stat} {repo_msg}'
                    await session.send(send_message)

            elif sp_msg[0] == 'sms':# 短轰
                await session.send('停用')
                # client = pymongo.MongoClient('mongodb://localhost:27017/')
                # dblist = client.list_database_names()
                # db = client['QBOT_DB']
                # col = db['sms_bomber_url']

            else:
                await session.send(
                    f'''
                    [CQ:at,qq={req_qid}]参数错误
                    使用示例：
                        @Chens_QBOT finder [MODE] [INFO]

                    MODE：查找模式（必需）
                        q2p 通过QQ号查询密保手机
                        p2q 手机号查询绑定QQ
                        q2l QQ号查询LOL信息
                        l2q LOL查询QQ信息
                        q2pwd QQ号查询老密
                        w2p 微博通过ID查手机号
                        p2w 微博通过手机号查ID
                        sms 短轰

                    INFO：要查询的信息（必需）
                        一般为qid或手机号
                    '''.strip()
                )
        else:
            await session.send(
                    f'''
                    [CQ:at,qq={req_qid}]参数错误
                    使用示例：
                        @Chens_QBOT finder [MODE] [INFO]

                    MODE：查找模式（必需）
                        q2p 通过QQ号查询密保手机
                        p2q 手机号查询绑定QQ
                        q2l QQ号查询LOL信息
                        l2q LOL查询QQ信息
                        q2pwd QQ号查询老密
                        w2p 微博通过ID查手机号
                        p2w 微博通过手机号查ID
                        sms 短轰

                    INFO：要查询的信息（必需）
                        一般为qid或手机号
                    '''.strip()
                )
    elif enable_finder == 'false':
        pass
    else:
        pass

# 随机身份证
@on_command('rdsfz')
async def _(session: CommandSession):
    if enable_rdsfz == 'true':
        for i in apiuse_col.find():
            if 'rdsfz' in i['api_name']:
                today_apiuse = int(i['today'])
                total_apiuse = int(i['total'])
                send_apiname = {'api_name' : 'rdsfz'}
                apiuse_today = {'$set' : {'today' : str(today_apiuse + 1)}}
                apiuse_total = {'$set' : {'total' : str(total_apiuse + 1)}}
                apiuse_col.update_many(send_apiname, apiuse_today)
                apiuse_col.update_many(send_apiname, apiuse_total)
                break
            else:
                pass

        n = random.randint(1, 32199)
        req_qid = str(session.event.user_id)

        for i in sfz_col.find():
            if i['sfz_num'] == n:
                send_sfz = i['sfz_info']
                await session.send(f'[CQ:at,qq={req_qid}]rdsfz：内容\n{send_sfz}')
                break
            else:
                pass
    elif enable_rdsfz == 'false':
        pass
    else:
        pass

# 摸鱼
@on_command('tfish')
async def _(session: CommandSession):
    if enable_tfish == 'true':
        ua = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.47'}
        url = 'http://bjb.yunwj.top/php/mo-yu/php.php'
        requ = Request(url=url, headers=ua)
        repo = urlopen(requ).read()
        repo_str = bytes(repo).decode()
        repo_dict = ast.literal_eval(repo_str)

        send_str = repo_dict['wb']
        send_rep = send_str.replace('【换行】', '')
        send_rep = re.sub(r'[0-9]+', '', send_rep)
        send_rep = re.sub(r'小时', '8小时', send_rep)
        send_rep = re.sub(r'是一个分享生活和释放压力的地方', '厕所是一个分享生活和释放压力的地方，', send_rep)
        send_rep = re.sub(r'大胆表达可以让你释放压力摸鱼办', '大胆表达可以让你释放压力，', send_rep)
        send_rep = re.sub(r'周末还有天元旦还有天', '', send_rep)

        stat = repo_dict['zt']
        stat_str = repo_dict['nr']

        req_qid = str(session.event.user_id)
        send_message = f'[CQ:at,qq={req_qid}]摸鱼：{stat_str} StatusCode：{stat}\n{send_rep}'
        await session.send(send_message)
    elif enable_tfish == 'false':
        pass
    else:
        pass

# 手冲
@on_command('handrush')
async def _(session: CommandSession):
    if enable_handrush == 'true':
        for i in apiuse_col.find():
            if 'handrush' in i['api_name']:
                today_apiuse = int(i['today'])
                total_apiuse = int(i['total'])
                send_apiname = {'api_name' : 'handrush'}
                apiuse_today = {'$set' : {'today' : str(today_apiuse + 1)}}
                apiuse_total = {'$set' : {'total' : str(total_apiuse + 1)}}
                apiuse_col.update_many(send_apiname, apiuse_today)
                apiuse_col.update_many(send_apiname, apiuse_total)
                break
            else:
                pass

            
        rnd_out = random.choice(['可以', '可以', '可以', '不可以', '不可以', '不可以', '不可以', '不可以', '不可以', '不可以'])
        qid = str(session.event.user_id)
        for i in handrush_col.find():
            if qid in i['qid']:
                inqid = True
                db_qid = i['qid']
                today_rush = int(i['today_rush'])
                total_rush = int(i['total_rush'])
                break
            else:
                inqid = False
                pass
            
        if inqid == True:
            if rnd_out == '可以':
                add_qid = {'qid' : db_qid}
                new_today_rush = {'$set' : {'today_rush' : str(today_rush + 1)}}
                new_total_rush = {'$set' : {'total_rush' : str(total_rush + 1)}}
                handrush_col.update_many(add_qid, new_today_rush)
                handrush_col.update_many(add_qid, new_total_rush)
                await session.send(f'[CQ:at,qq={qid}]：今天{rnd_out}手冲\n总计已冲{total_rush + 1}发')
            elif rnd_out == '不可以':
                await session.send(f'[CQ:at,qq={qid}]：今天{rnd_out}手冲\n总计已冲{total_rush}发')
            else:
                pass
        elif inqid == False:
            if rnd_out == '可以':
                newusr_rush_dict = {'qid' : qid, 'today_rush' : '0', 'total_rush' : '0'}
                handrush_col.insert_one(newusr_rush_dict)
                await session.send(f'[CQ:at,qq={qid}]：今天{rnd_out}手冲\n总计已冲1发')
                add_qid = {'qid' : qid}
                new_today_rush = {'$set' : {'today_rush' : str(today_rush + 1)}}
                new_total_rush = {'$set' : {'total_rush' : str(total_rush + 1)}}
                handrush_col.update_many(add_qid, new_today_rush)
                handrush_col.update_many(add_qid, new_total_rush)

            elif rnd_out == '不可以':
                newusr_rush_dict = {'qid' : qid, 'today_rush' : '0', 'total_rush' : '0'}
                handrush_col.insert_one(newusr_rush_dict)
                await session.send(f'[CQ:at,qq={qid}]：今天{rnd_out}手冲\n总计已冲0发')
            else:
                pass
        else:
            pass
    elif enable_handrush == 'false':
        pass
    else:
        pass

# 随机涩图
@on_command('rdsimg')
async def _(session: CommandSession):
    if enable_rdsimg == 'true':
        for i in apiuse_col.find():
            if 'rdsimg' in i['api_name']:
                today_apiuse = int(i['today'])
                total_apiuse = int(i['total'])
                send_apiname = {'api_name' : 'rdsimg'}
                apiuse_today = {'$set' : {'today' : str(today_apiuse + 1)}}
                apiuse_total = {'$set' : {'total' : str(total_apiuse + 1)}}
                apiuse_col.update_many(send_apiname, apiuse_today)
                apiuse_col.update_many(send_apiname, apiuse_total)
                break
            else:
                pass
            
        ua = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.47'}
        # url = 'https://api.lolicon.app/setu/v2'
        url = 'https://www.dmoe.cc/random.php?return=json'
        # data = {'r18' : 2, 'num' : 1}
        requ = Request(url=url, headers=ua)
        repo = urlopen(requ).read()
        brepo_str = repo.decode()
        brepo_dict = ast.literal_eval(brepo_str)

        imgurl = brepo_dict['imgurl']
        send_img = re.sub(r'\\', '', imgurl)
        stat = brepo_dict['code']
        req_qid = str(session.event.user_id)

        await session.send(f'[CQ:image,file={send_img}]')
        await session.send(f'[CQ:at,qq={req_qid}]RandomSetu StatusCode：{stat}')
    elif enable_rdsimg == 'false':
        pass
    else:
        pass

