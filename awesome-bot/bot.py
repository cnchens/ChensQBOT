import os
import nonebot
import config

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