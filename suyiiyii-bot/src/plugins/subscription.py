import time, random, asyncio
from nonebot import require, on_command, get_bot
from nonebot.rule import to_me
from nonebot.matcher import Matcher
from nonebot.adapters import Message, MessageSegment
from nonebot.params import ArgPlainText
from nonebot import get_plugin_config
from .config import Config

from .data import get_data

require("nonebot_plugin_saa")
from nonebot_plugin_saa import Text



query = on_command("query", rule=to_me, aliases={"r"}, priority=5, block=True)

last_data = ""


@query.handle()
async def handle():
    global last_data
    data = get_data()
    if data == last_data:
        await query.finish("数据没有更新")
    last_data = data

    # 截断到 100 个字符
    if len(data) > 100:
        data = data[:100] + "..."
    print(data)
    await query.finish(data)

