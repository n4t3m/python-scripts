import asyncio
import discord
from discord.ext import commands
import json
import random


TOKEN = ""
client = commands.Bot(command_prefix='sb!', self_bot=True, fetch_offline_members=False)
client.remove_command('help')
BOT_PREFIX = "sb!"

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    game = discord.Game("azunyan <3")
    await client.change_presence(status=discord.Status.online, activity=game)
    client.guild = client.get_guild(728860526389493802)
    client.channel = client.guild.get_channel(729556841817702442)
    await spam(client)
    

@client.event
async def on_message(message):
    if message.author == client.user:   
        return
    
    if message.content == "check":
        client.guild = client.get_guild(729012441496813659)
        await message.channel.send(client.guild)

    await client.process_commands(message)


async def spam(client):
    while True:    
        await client.channel.send('here is a message plus a string ' + str(random.randint(0, 1000000) ))
        await asyncio.sleep(1)



print("Logging in...")
client.run(TOKEN, bot=False)