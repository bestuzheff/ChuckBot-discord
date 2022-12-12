import discord
import codecs
from os import getenv
from random import randint
from dotenv import load_dotenv

load_dotenv()

bot_id = getenv("BOT_ID")
if not bot_id:
    exit("Error: no id provided")

bot_token = getenv("BOT_TOKEN")
if not bot_token:
    exit("Error: no token provided")

intents = discord.Intents.default()
intents.message_content = True
intents.members =True

client = discord.Client(intents=intents)

#Читаем файл в массив
text_file = codecs.open("ChuckText.txt", encoding="utf-8")
lines = text_file.readlines()

@client.event
async def on_message(message):
    # don't respond to ourselves
    if message.author == client.user:
        return
    if (bot_id in message.content) or message.channel.type.name == "private":
        await message.channel.send(lines[randint(0, len(lines) - 1)])


client.run(bot_token)
