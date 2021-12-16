import discord
from discord.ext import commands
import requests
import setup
import random
import requests
from discord import Webhook, RequestsWebhookAdapter
import json
import asyncio


description = "Type $info to see more information."
TOKEN = setup.TOK
client = commands.Bot(command_prefix='r!', description=description, help_command=None)
lastmessage = [1]


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    initcount = 0
    for g in client.guilds:
        initcount = initcount + len(g.members)
    game = discord.Game("Watching all your messages...")
    await client.change_presence(status=discord.Status.online, activity=game)
    client.url = ""
    client.c_id = 0

@client.event
async def on_guild_join(guild):
    print("Joined New Server: " + guild.name + ". Members: " + str( len(guild.members) ) + ". Owner: " + guild.owner.display_name + ".")

@client.event
async def on_guild_remove(guild):
    print("Removed From Server: " + guild.name + ". Members: " + str( len(guild.members) ) + ". Owner: " + guild.owner.display_name + ".")

    


@client.event
async def on_message(message):
    if message.author == client.user:   
        return
           
        
       
    await client.process_commands(message)

@client.event
async def on_message_delete(message):
    if client.c_id == 0:
        print('made it here')
        return
    if message.channel.id == client.c_id:
        if message.author.bot:
            return
        if message.content == 'r!snipe':
            return
        lastmessage[0]=message
        print("New message saved: " + message.content)
    return    

@client.command()
async def ping(ctx):
    await ctx.send('Pong! {0}'.format(round(client.latency, 1)))

@client.command()
async def setWebhook(ctx, i_url: str):
    client.url = i_url
    await ctx.send("New URL Value: " + client.url)

@client.command()
async def checkWebhook(ctx):
    await ctx.send("Current URL: " + client.url)

@client.command()
async def setChannel(ctx, i_chan: int):
    client.c_id = i_chan
    await ctx.send("New Channel ID: " + str(client.c_id))

@client.command()
async def checkChannel(ctx):
    await ctx.send("Current Channel ID: " + str(client.c_id))


    
@client.command()
async def snipe(ctx):
    if ctx.message.channel.id != client.c_id:
        await ctx.send("The current channel is not the one configured.")
        return
    if client.url == "":
        await ctx.send("Webhook link is not set.")
        return
    data = {}
    data["content"] = lastmessage[0].content
    data["username"] = lastmessage[0].author.display_name
    data["avatar_url"] = str(lastmessage[0].author.avatar_url)
    result = requests.post(client.url, data=json.dumps(data), headers={"Content-Type": "application/json"})
    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
    else:
        print("Payload delivered successfully, code {}. Message should appear successfully.".format(result.status_code))
    await ctx.message.delete()
    return



        


client.run(TOKEN)
            