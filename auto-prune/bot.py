import discord
from discord.ext import commands
import config
import random
import json
import asyncio


description = config.DESC
TOKEN = config.TOK
PREFIX = config.PREFIX
STATUS = config.STATUS
DEFAULT_DELAY = config.DEFAULT_DELAY
bot = commands.Bot(command_prefix=PREFIX, description=description, case_insensitive=True)

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    game = discord.Game(STATUS)
    await bot.change_presence(status=discord.Status.online, activity=game)



@bot.event
async def on_message(message):

    if PREFIX in message.content:
        await bot.process_commands(message)
        return

    
    with open('guilds.json') as json_file:
        existingData = json.load(json_file)
    data = existingData

    if str(message.guild.id) not in data:
        return
    
    if message.channel.id in data[str(message.guild.id)]:
        #bruh
        with open('delays.json') as json_file:
            existingData = json.load(json_file)
        t_data = existingData
        d = t_data[str(message.guild.id)]
        await remove(message, d)
        return


@bot.command()
async def addChannel(ctx):
    if not ctx.message.author.guild_permissions.administrator:
        await ctx.send("You must be administrator to use this command")
        return


    with open('guilds.json') as json_file:
        existingData = json.load(json_file)
    data = existingData

    if str(ctx.guild.id) not in data:
        data[str(ctx.guild.id)] = []

    if ctx.message.channel.id not in data[str(ctx.guild.id)]:
        data[str(ctx.guild.id)].append(ctx.message.channel.id)
    else:
        print("This channel already has pruning enabled. Use the remove command in this channel if you would like to remove it.")
    

    await ctx.send("Added " + ctx.message.channel.name + " to blacklisted channels.")

    with open("guilds.json", "w") as write_file:
        json.dump(data, write_file)
    
    with open('delays.json') as json_file:
        existingData = json.load(json_file)
    data = existingData

    if str(ctx.guild.id) not in data:
        data[str(ctx.guild.id)] = 300

    with open("delays.json", "w") as write_file:
        json.dump(data, write_file)

@bot.command()
async def channels(ctx):

    with open('guilds.json') as json_file:
        existingData = json.load(json_file)
    data = existingData

    if str(ctx.guild.id) not in data:
        await ctx.send("This server has not been configured! Use the command ``addChannel`` to start pruning new messages!")
        return
    
    if len(data[str(ctx.guild.id)])==0:
        await ctx.send("This server has no channels configured!")
        return

    message = "Channels Being Pruned: "

    for x in data[str(ctx.guild.id)]:
        channel = bot.get_channel(x)
        message = message + channel.name + ", "

    message = message[:-2]

    await ctx.send(message)

    with open("guilds.json", "w") as write_file:
        json.dump(data, write_file)

@bot.command()
async def remove(ctx):

    with open('guilds.json') as json_file:
        existingData = json.load(json_file)
    data = existingData

    if str(ctx.guild.id) not in data:
        await ctx.send("This server has no channels configured!")
        return

    if ctx.message.channel.id not in data[str(ctx.guild.id)]:
        await ctx.send("Channel cannot be removed as messages are not being removed here!")
        return

    data[str(ctx.guild.id)].remove(ctx.message.channel.id)
    await ctx.send("Removed channel: " + ctx.channel.name)

    with open("guilds.json", "w") as write_file:
        json.dump(data, write_file)

    await remove(ctx.message, 5)

@bot.command()
async def delay(ctx, d: int):
    with open('delays.json') as json_file:
        existingData = json.load(json_file)
    data = existingData

    data[str(ctx.guild.id)] = d

    await ctx.send("New Delay Set: " + str(data[str(ctx.guild.id)]) + " seconds.")

    with open("delays.json", "w") as write_file:
        json.dump(data, write_file)

@bot.command()
async def checkdelay(ctx):
    with open('delays.json') as json_file:
        existingData = json.load(json_file)
    data = existingData

    if str(ctx.guild.id) not in data:
        data[str(ctx.guild.id)] = 300
    
    await ctx.send("Current Delay: " + str(data[str(ctx.guild.id)]) + " seconds." )

    with open("delays.json", "w") as write_file:
        json.dump(data, write_file)

async def remove(message, delay):
    c_name = message.channel.name
    g_name = message.guild.name
    await asyncio.sleep(delay) 
    await message.delete()
    print("A message has been automatically pruned in " + c_name + " in the server " + g_name)
    return

@bot.command()
async def ping(ctx):
    await ctx.send('Pong! {0}'.format(round(bot.latency, 1)))


bot.run(TOKEN)