from ServerCommands import PingCommand, DeleteMessageCommand
from GamesCommands import RPS


class ServerCommands:
    def __init__(self):
        self.match_command = None
        self.command_found = False

        self.commands = {
            "help": (self.HelpCommand, "Zobrazí seznam příkazů."),
            "pingg": (PingCommand.PingCommand, "Pingne everyone"),
            "smaž": (DeleteMessageCommand.DeleteMessageCommand, "Smaže zadaný počet zpráv - smaž[počet zpráv]"),
            "rps": (RPS.Rps, "Zahraj si proti Kusovníkovi kámen, nůžky, papír - rps [varianta]")
        }

    async def ServerCommands(self, bot, message):
        if bot.user.mentioned_in(message) and "@everyone" not in message.content and "@here" not in message.content:
            content = message.content.lower()
            for match_command in self.commands:
                if match_command in content:
                    self.match_command = match_command
                    self.command_found = True
                    await self.commands[match_command][0](message)

            if not self.command_found:
                await message.channel.send(f"{message.author.mention} Co mě pinguješ more, tento příkaz neznám..")

    async def HelpCommand(self, message):
        help_message = "__# Seznam příkazů:__\nPro aktivaci napiš @Kusovník [název příkazu]\n\n"
        for command, (method, description) in self.commands.items():
            help_message += f"- {command} => {description}\n"

        await message.channel.send(help_message)
