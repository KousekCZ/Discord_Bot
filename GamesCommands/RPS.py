import random


async def Rps(message):
    try:
        options = ['rock', 'paper', 'scissors']
        bot_choice = random.choice(options)

        await message.channel.send(f'Bot chose: {bot_choice}')

        user_choice = message.content.lower().strip()
        if user_choice in options:
            if user_choice == bot_choice:
                await message.channel.send("It's a tie!")
            elif (
                    (user_choice == 'rock' and bot_choice == 'scissors') or
                    (user_choice == 'paper' and bot_choice == 'rock') or
                    (user_choice == 'scissors' and bot_choice == 'paper')
            ):
                await message.channel.send("You win!")
            else:
                await message.channel.send("Bot wins!")
        else:
            await message.channel.send("Invalid choice. Please choose rock, paper, or scissors.")

    except (ValueError, IndexError):
        await message.channel.send("Nemohu rozpoznat, tvojí možnost výběru.")
