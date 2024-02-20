import asyncio
import discord
import datetime


async def update_activity(bot, logging_channel, nowTime):
    try:
        while True:
            current_time = datetime.datetime.now().time()
            if current_time >= datetime.time(22, 0) or current_time < datetime.time(8, 0):
                await bot.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game('Spím, tak nečum...'))
            else:
                await bot.change_presence(status=discord.Status.online, activity=discord.Game('Život je jen hra...'))
            await asyncio.sleep(1)

    except Exception as e:
        await logging_channel.send(
            f"<@!481879980612124703>```diff\n- {nowTime} ERROR: Chyba ve změně stavu aktivity bota: {e}\n```")
