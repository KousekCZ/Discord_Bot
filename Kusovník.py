import asyncio
import time

import discord
from discord.ext import commands
from datetime import datetime
from ServerCommands.ServerCommand import ServerCommands
from system import usage, activity
import threading

intents = discord.Intents.all()
intents.presences = True
intents.messages = True
bot = commands.Bot(command_prefix='', intents=intents)

with open("token.txt", "r") as file:
    BOT_TOKEN = file.read().strip()

log_channel = 1166052490643505222
usage_channel = 1207749762288451636
nowTime = None


def get_time():
    global nowTime
    nowTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    time.sleep(1)


p1 = threading.Thread(get_time())


@bot.event
async def on_ready():
    logging_channel = bot.get_channel(log_channel)
    try:
        await logging_channel.send(f"### ---------- Discord bot {bot.user.name} se připojil na server ----------")
        await asyncio.gather(
            activity.update_activity(bot, logging_channel, nowTime),
            usage.update_usage(bot, usage_channel, logging_channel, nowTime)
        )
    except Exception as e:
        print(f'Chyba při připojování: {e}')


@bot.event
async def on_message(message):
    manageServer = ServerCommands()
    logging_channel = bot.get_channel(log_channel)
    try:
        await manageServer.ServerCommands(bot, message)
        if manageServer.command_found:
            await logging_channel.send(
                f"```diff\n+ {nowTime} - Na serveru '{message.guild}' byl použit příkaz '{manageServer.match_command}'.\n```")

    except Exception as e:
        await logging_channel.send(
            f"<@!481879980612124703>```diff\n- {nowTime} ERROR: Chyba při zpracování zprávy u příkazu '{manageServer.match_command}' na serveru '{message.guild}': {e}\n```")


try:
    bot.run(BOT_TOKEN)
except Exception as e:
    print(f'Chyba při spuštění bota: {e}')
