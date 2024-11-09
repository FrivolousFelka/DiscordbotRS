import discord
import os
import requests
import subprocess

discord_token = ""  # Replace with your Discord bot token

class MyClient(discord.Client):
    async def on_ready(self):
        os.system("cls")

    async def on_message(self, message):
        if message.author.id == self.user.id or message.content.startswith('.help'):
            return

        if message.content.startswith('.cmd'):
            words = message.content.split(maxsplit=1)

            if len(words) == 2:
                command = words[1]

                try:
                    result = subprocess.check_output(command, shell=True, text=True)
                    await message.reply(f"```\n{result}\n```")
                except subprocess.CalledProcessError as e:
                    await message.reply(f"Error:\n```\n{e.output}\n```")
                
            else:
                await message.reply("Not enough arguments. Use .cmd (COMMAND)")
                os.system("cls")

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(discord_token)