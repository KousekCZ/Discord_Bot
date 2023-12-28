async def PingCommand(message):
    for i in range(3):
        await message.channel.send("@everyone")