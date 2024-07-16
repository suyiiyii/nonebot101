import time
from nonebot import on_command
from nonebot.rule import to_me
# from nonebot.adapters import Message, MessageSegment
from nonebot.adapters.console import Message, MessageSegment
from nonebot.params import CommandArg

check_time = on_command(
    "time", rule=to_me, aliases={"t", "时间", "几点了"}, priority=5, block=True
)


@check_time.handle()
async def handle(args: Message = CommandArg()):
    replys = []
    replys.append(f"现在时间是：{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}")
    replys.append(f"命令参数是：{args}")

    message = Message(
        [
            MessageSegment(type="text", data={"text": "hello"}),
            MessageSegment(type="markdown", data={"markup": "**world**"}),
        ]
    )

    # await check_time.finish("\n".join(replys))
    await check_time.finish(message)
