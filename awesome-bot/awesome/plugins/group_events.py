from nonebot import on_notice, NoticeSession
import json

f = open('config.json', 'r', encoding='utf-8')# 读取config
json_res = json.load(f)

# 入群
@on_notice('group_increase')
async def _(session: NoticeSession):
    # grpid = session.event.group_id
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
        type = session.event.sub_type
        op_qid = str(session.event.operator_id)
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