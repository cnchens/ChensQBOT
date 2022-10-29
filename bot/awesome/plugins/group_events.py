from nonebot import on_notice, NoticeSession

# 入群
@on_notice('group_increase')
async def _(session: NoticeSession):
    # grpid = session.event.group_id
    at_qid = session.event.user_id
    await session.send(f'[CQ:at,qq={at_qid}]欢迎新人欢迎入群')

# 退群
@on_notice('group_decrease')
async def _(session: NoticeSession):
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
