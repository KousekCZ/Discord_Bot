import discord
from discord.ext import commands
from manageServer import manage_server

intents = discord.Intents.all()
intents.presences = True
intents.messages = True
bot = commands.Bot(command_prefix='', intents=intents)
BOT_TOKEN = "MTE2NDU4MjM5MDA2NTI3NDkwMA.GjVjAH.ltObOPH3H3FeOvzwMrTyNKZEZnwGKNnVPu1LNs"
log_channel = 1166052490643505222


@bot.event
async def on_ready():
    target_channel = bot.get_channel(log_channel)
    try:
        await target_channel.send(f"### ---------- Discord bot {bot.user.name} se připojil na server ----------")
    except Exception as e:
        print(f'Chyba při připojování: {e}')


@bot.event
async def on_message(message):
    await manage_server(bot, message, log_channel)


try:
    bot.run(BOT_TOKEN)
except Exception as e:
    print(f'Chyba při spuštění bota: {e}')
