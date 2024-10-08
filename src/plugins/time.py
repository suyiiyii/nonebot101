import time, random, asyncio
from nonebot import require, on_command, get_bot
from nonebot.rule import to_me
from nonebot.matcher import Matcher
from nonebot.adapters import Message, MessageSegment
from nonebot.params import ArgPlainText
from nonebot import get_plugin_config
from .config import Config

plugin_config = get_plugin_config(Config)

# from nonebot.adapters.console import Message, MessageSegment
from nonebot.params import CommandArg

require("nonebot_plugin_saa")
from nonebot_plugin_saa import Text

require("nonebot_plugin_apscheduler")
from nonebot_plugin_apscheduler import scheduler

check_time = on_command(
    "time", rule=to_me, aliases={"t", "时间", "几点了"}, priority=5, block=True
)


# @scheduler.scheduled_job("cron", second="0", id="xxx")
async def send_private():
    from nonebot_plugin_saa import TargetQQPrivate

    target = TargetQQPrivate(user_id=plugin_config.time_user_id)
    await Text("博士，你今天有早八，还不能休息哦").send_to(target, get_bot())


@check_time.handle()
async def handle(matcher: Matcher, args: Message = CommandArg()):
    if zone := args.extract_plain_text:
        matcher.set_arg("zone", zone)


@check_time.got("timezone", prompt="请输入时区：")
async def got(zone: str = ArgPlainText):

    replys = []
    replys.append(f"现在时间是：{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}")
    replys.append(f"时区是：{zone}")
    replys.append(
        f'该时区内的时间是：{time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())}'
    )
    # replys.append(f"命令参数是：{args}")

    text = Text("\n".join(replys))

    await text.send(at_sender=True, reply=True)


guess_number = on_command(
    "guess_number", aliases={"g"}, rule=to_me, priority=5, block=True
)


@guess_number.handle()
async def handle(macher: Matcher):
    guess_number = random.randint(1, 100)
    macher.set_arg("answer", guess_number)
    macher.set_arg("times", 0)
    print(f'答案是：{guess_number}')
    await Text("我们来玩猜数字游戏吧！").send()
    await asyncio.sleep(0.75)


@guess_number.got("number", prompt="请输入一个 1-100 之间的整数：")
async def got_number(macher: Matcher, number: str = ArgPlainText()):
    answer = macher.get_arg("answer")
    times = macher.get_arg("times")
    times += 1
    print(f'当前次数为：{times}')
    macher.set_arg("times", times)
    if not number.isdigit():
        await guess_number.reject("请输入一个整数！")
    number = int(number)
    if number < answer:
        await guess_number.reject("猜小了！")
    elif number > answer:
        await guess_number.reject("猜大了！")
    else:
        await Text("猜对了！").send()


@guess_number.handle()
async def handle(macher: Matcher):
    times = macher.get_arg("times")
    reply = ""
    if times <= 3:
        reply = f"{times}次？是不是开了？"
    elif times >= 7:
        reply = f"太下饭了吧你，{times}次啊"
    else:
        reply = f"还行，{times}次"
    await guess_number.finish(reply)


weather = on_command("tq", priority=5, block=True)


@weather.handle()
async def handle_function(matcher: Matcher, args: Message = CommandArg()):
    if args.extract_plain_text():
        matcher.set_arg("location", args)
    await weather.send("请输入地名 213123")


@weather.got("location", prompt="请输入地名")
async def got_location(location: str = ArgPlainText()):
    await weather.send(f"今天{location}的天气是...")


@weather.got("location1", prompt="请输入地名 5gfdsgsdfg")
async def got_location(location: str = ArgPlainText()):
    await weather.send(f"今天{location}的天气是...")
