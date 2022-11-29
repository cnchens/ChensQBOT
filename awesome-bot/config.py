from nonebot.default_config import *
import json

f = open('config.json', 'r', encoding='utf-8')# 读取config
json_res = json.load(f)

superusers = json_res['superusers']# 超级用户
superusers = set(superusers)# list2set
cmd_start = json_res['cmd_start']# 命令起始符
host = json_res['host']# nonebot_ip
port = json_res['port']# nonebot_port
api_root = json_res['api_root']# nonebot_api_ip

SUPERUSERS = superusers
COMMAND_START = cmd_start
HOST = host
PORT = port
API_ROOT = api_root