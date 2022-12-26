from nonebot.default_config import *
import json

f = open('config.json', 'r', encoding='utf-8')# 读取config
json_res = json.load(f)

debug = json_res['debug']# 是否启用debug
superusers = json_res['superusers']# 超级用户
superusers = set(superusers)# list2set
cmd_start = json_res['cmd_start']# 命令起始符
cmd_start = set(cmd_start)# list2set
host = json_res['host']# nonebot_ip
port = json_res['port']# nonebot_port
port = int(port)# str2int
api_root = json_res['api_root']# nonebot_api_ip

SUPERUSERS = superusers
COMMAND_START = {''}
NICKNAME = cmd_start
HOST = host
PORT = port
API_ROOT = api_root
DEBUG = debug
SHORT_MESSAGE_MAX_LENGTH = 200