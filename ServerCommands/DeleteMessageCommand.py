import asyncio


async def DeleteMessageCommand(message):
    try:
        words = message.content.split()
        smaz_index = words.index("smaž")
        num_to_delete = int(words[smaz_index + 1])
        messages_to_delete = []

        async for previous_message in message.channel.history(limit=num_to_delete + 1):
            messages_to_delete.append(previous_message)

        if messages_to_delete:
            await message.channel.delete_messages(messages_to_delete)

            result_message = await message.channel.send(
                f"Smazal jsem {num_to_delete} zpráv...")

            await asyncio.sleep(2)
            await result_message.delete()
        else:
            await message.channel.send("Nemohu najít zprávy ke smazání.")

    except (ValueError, IndexError):
        await message.channel.send("Nemohu rozpoznat, kolik zpráv mám smazat.")
