import discord
from discord.ext import commands
import requests
import setup
import random
import requests
from discord import Webhook, RequestsWebhookAdapter
import json


description = "Type $info to see more information."
TOKEN = setup.TOK
client = commands.Bot(command_prefix='!', description=description, help_command=None)
client.UID = 0
client.GUILDID = 0


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    initcount = 0
    for g in client.guilds:
        initcount = initcount + len(g.members)
    game = discord.Game("azusa")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_guild_join(guild):
    print("Joined New Server: " + guild.name + ". Members: " + str( len(guild.members) ) + ". Owner: " + guild.owner.display_name + ".")

@client.event
async def on_guild_remove(guild):
    print("Removed From Server: " + guild.name + ". Members: " + str( len(guild.members) ) + ". Owner: " + guild.owner.display_name + ".")

@client.event
async def on_voice_state_update(member, before, after):
    print(client.UID)
    if member.id != client.UID:
        return
    print("Muted " + member.nick + ' Again!')
    await member.edit(mute=True)
    return
    

    


@client.event
async def on_message(message):
    if message.author == client.user:   
        return

    if int(message.author.id) == int(client.UID):
        print("liberal destroyed")
        await message.delete()  
        
    await client.process_commands(message)


@client.command()
async def bullyuser(ctx, id):
    client.UID = int(id)
    client.GUILDID = ctx.guild.id
    await ctx.send("Now Bullying <@!" + str(client.UID) + ">")

@client.command()
async def bullycheck(ctx):
    await ctx.send("Now Bullying: " + str(client.UID))

@client.command()
async def reset(ctx):
    client.UID = 0
    client.GUILDID = 0
    await ctx.send("Done")
    
    
  


client.run(TOKEN)
            