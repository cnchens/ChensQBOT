from nonebot import on_command, CommandSession
import threading
import time
import nonebot
import random
import string



@on_command('go')
async def _(session: CommandSession):
    bot = nonebot.get_bot()

    grp = 902346736
    while True:
        await bot.send_group_msg(group_id=grp, message=r'[CQ:image,file=1.png]')
