import discord
from dotenv import load_dotenv
from compiler import getScript
import os

load_dotenv()
TOKEN = os.getenv("TOKEN")
PREFIX = os.getenv("PREFIX")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if(message.content.startswith(f"{PREFIX}compile")):
        msg = message.content.split("```")[1]
        script = msg.split("\n", 1)
        script = script[1]
        language = "python3"
        res = f"```\n{getScript(language, script)}```"
        await message.channel.send(res)

client.run(TOKEN)