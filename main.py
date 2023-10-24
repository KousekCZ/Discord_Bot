import discord
from discord.ext import commands
import asyncio

intents = discord.Intents.all()
intents.presences = True
intents.messages = True
bot = commands.Bot(command_prefix='', intents=intents)
BOT_TOKEN = "MTE2NDU4MjM5MDA2NTI3NDkwMA.GjVjAH.ltObOPH3H3FeOvzwMrTyNKZEZnwGKNnVPu1LNs"
logging_channel = 1166052490643505222
error_channel = 1166289752446738462


@bot.event
async def on_ready():
    target_channel = bot.get_channel(logging_channel)
    try:
        await target_channel.send(f"### ---------- Discord bot {bot.user.name} se připojil na server ----------")
    except Exception as e:
        print(f'Chyba při připojování: {e}')
        await target_channel.send(f"Chyba při připojování na server: {e}")


@bot.event
async def on_message(message):
    try:

        if bot.user.mentioned_in(message) and "@everyone" not in message.content:
            content = message.content.lower()
            commandss = ["help", "ahoj", "pingg", "smaž"]
            command_notfound = False

            for command in commandss:
                if command in content:
                    command_notfound = True
                    target_channel = bot.get_channel(logging_channel)

                    match command:
                        case "help":
                            await message.channel.send(
                                '__# Seznam příkazů:__\npro aktivaci napiš @Kusovník [název příkazu]\n\n- help => zobrazí seznam příkazů\n- ahoj => vypíše uvítací zprávu')
                            await target_channel.send(f"Uživatel {message.author.mention} použil příkaz '{command}'.")

                        case "ahoj":
                            await message.channel.send(f'{message.author.mention} Co mě pinguješ more...')
                            await target_channel.send(f"Uživatel {message.author.mention} použil příkaz '{command}'.")

                        case "pingg":
                            for i in range(3):
                                await message.channel.send("@everyone")
                            await target_channel.send(f"Uživatel {message.author.mention} použil příkaz '{command}'.")

                        case "smaž":
                            await target_channel.send(f"Uživatel {message.author.mention} použil příkaz '{command}'.")
                            try:
                                words = content.split()
                                smaz_index = words.index("smaž")
                                num_to_delete = int(words[smaz_index + 1])
                                messages_to_delete = []

                                async for previous_message in message.channel.history(limit=num_to_delete + 1):
                                    messages_to_delete.append(previous_message)

                                if messages_to_delete:
                                    await message.channel.delete_messages(messages_to_delete)

                                    result_message = await message.channel.send(f"Smazal jsem {num_to_delete} zpráv...")

                                    await asyncio.sleep(2)
                                    await result_message.delete()
                                else:
                                    await message.channel.send("Nemohu najít zprávy ke smazání.")

                            except (ValueError, IndexError):
                                await message.channel.send("Nemohu rozpoznat, kolik zpráv mám smazat.")

            if not command_notfound:
                await message.channel.send(f"{message.author.mention} tento příkaz neznám..")
    except Exception as e:
        target_errorChannel = bot.get_channel(error_channel)
        await target_errorChannel.send(f'Chyba při zpracování zprávy: {e}')


try:
    bot.run(BOT_TOKEN)
except Exception as e:
    print(f'Chyba při spuštění bota: {e}')
