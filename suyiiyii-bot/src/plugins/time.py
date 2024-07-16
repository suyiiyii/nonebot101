import time
from nonebot import require, on_command, get_bot
from nonebot.rule import to_me
from nonebot.adapters import Message, MessageSegment

# from nonebot.adapters.console import Message, MessageSegment
from nonebot.params import CommandArg

require("nonebot_plugin_saa")
from nonebot_plugin_saa import Text


check_time = on_command(
    "time", rule=to_me, aliases={"t", "时间", "几点了"}, priority=5, block=True
)


async def send_private():
    from nonebot_plugin_saa import TargetQQPrivate

    target = TargetQQPrivate(user_id=1462845368)
    await Text("博士，你今天有早八，还不能休息哦").send_to(target, get_bot())


@check_time.handle()
async def handle(args: Message = CommandArg()):
    replys = []
    replys.append(f"现在时间是：{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}")
    replys.append(f"命令参数是：{args}")

    text = Text("\n".join(replys))
    await send_private()
    await text.send(at_sender=True, reply=True)
