import httpx
from dotenv import load_dotenv
import json

import os


import time, random, asyncio
from nonebot import require, on_command, get_bot
from nonebot.rule import to_me
from nonebot.matcher import Matcher
from nonebot.adapters import Message, MessageSegment
from nonebot.params import ArgPlainText
from nonebot import get_plugin_config
from .config import Config
load_dotenv()
cookies = json.loads(os.getenv('COOKIES'))

print(cookies)

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'client-version': 'v2.45.65',
    # 'cookie': 'XSRF-TOKEN=RznY1VcwbF7kF7UbBAgUPJ95; SUB=_2AkMRygsXf8NxqwFRmfwcz2vqZIx1yADEieKnlvrMJRMxHRl-yT9yqmgntRB6Okol-Th-ySBWIm6s20MMXykL1j-XLJM2; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9Whn9Y_ne9sYQ4Pn7qFDKUxs; WBPSESS=Wk6CxkYDejV3DDBcnx2LOSF9Os4N6jU5S_7jCnEs_XmCuloR-hkaidO2KmWve_PsX5uw71DsSZuZVSVK0pIgpxBBP_dqhmvWlnMcj7xT0SYtd75m34ftkKrkPNQFKwHLNBp3reNY1wOS2nhckGCDNUa-ogGdyf3BINCWdLZZKvw=',
    'priority': 'u=1, i',
    'referer': 'https://weibo.com/u/6279793937',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'server-version': 'v2024.07.16.1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    'x-xsrf-token': 'RznY1VcwbF7kF7UbBAgUPJ95',
}

params = {
    'uid': '6279793937',
    'page': '1',
    'feature': '0',
}

require("nonebot_plugin_apscheduler")
from nonebot_plugin_apscheduler import scheduler
@scheduler.scheduled_job("interval", seconds=30, id="query")
def get_data():
    response = httpx.get(
        'https://weibo.com/ajax/statuses/mymblog',
        params=params,
        cookies=cookies,
        headers=headers,
    )
    reply = json.dumps(response.json())
    # print(reply)

    data = reply
    # 截断到 100 个字符
    if len(data) > 100:
        data = data[:100] + "..."
    print(f"数据：{data}")

    return reply
