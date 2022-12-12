import discord
from random import randint
import codecs

botID = "822035207112097792"
botToken = "ODIyMDM1MjA3MTEyMDk3Nzky.YFMZ8g.5HWlcf83Dz4efUpH8NC0-rq0-Tg"

#Читаем файл в массив
text_file = codecs.open("ChuckText.txt", encoding="utf-8")
lines = text_file.readlines()

class MyClient(discord.Client):
    # async def on_ready(self):
    #     print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return
        if (botID in message.content) or message.channel.type.name == "private":
            await message.channel.send(lines[randint(0, len(lines) - 1)])


client = MyClient()
client.run(botToken)
