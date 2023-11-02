import datetime
import asyncio


async def manage_server(bot, message, log_channel):
    list_of_commands = ["help", "ahoj", "pingg", "smaž"]
    now = datetime.datetime.now()
    date_time = now.strftime("%Y-%m-%d %H:%M:%S")
    target_channel = bot.get_channel(log_channel)
    server = message.guild
    command_found = False
    try:
        if bot.user.mentioned_in(message) and "@everyone" not in message.content:
            content = message.content.lower()

            for command in list_of_commands:
                if command in content:
                    command_found = True
                    match command:
                        case "help":
                            await message.channel.send(
                                '__# Seznam příkazů:__\npro aktivaci napiš @Kusovník [název příkazu]\n\n- help => zobrazí seznam příkazů\n- ahoj => vypíše uvítací zprávu')
                            await target_channel.send(
                                f"```diff\n+ {date_time} - Na serveru '{server}' byl použit příkaz '{command}'.\n```")

                        case "ahoj":
                            await message.channel.send(f'{message.author.mention} Co mě pinguješ more...')
                            await target_channel.send(
                                f"```diff\n+ {date_time} - Na serveru '{server}' byl použit příkaz '{command}'.\n```")

                        case "pingg":
                            for i in range(3):
                                await message.channel.send("@everyone")
                            await target_channel.send(
                                f"```diff\n+ {date_time} - Na serveru '{server}' byl použit příkaz '{command}'.\n```")

                        case "smaž":
                            await target_channel.send(
                                f"```diff\n+ {date_time} - Na serveru '{server}' byl použit příkaz '{command}'.\n```")
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

            if not command_found:
                await message.channel.send(f"{message.author.mention} tento příkaz neznám..")
    except Exception as e:
        await target_channel.send(
            f"<@!481879980612124703>```diff\n- ERROR: Chyba při zpracování zprávy u příkazu '{command}' na serveru '{server}': {e}\n```")
