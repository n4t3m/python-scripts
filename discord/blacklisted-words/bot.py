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
MESSAGE = config.MESSAGE
bot = commands.Bot(command_prefix=PREFIX, description=description)

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    game = discord.Game(STATUS)
    await bot.change_presence(status=discord.Status.online, activity=game)


@bot.event
async def on_message(message):
    if message.author == bot.user:   
        return

    with open('words.json') as json_file:
        existingData = json.load(json_file)
    data = existingData



    if str(message.guild.id) in data and "bl!remove " not in message.content:
        for x in data[str(message.guild.id)]:
            if x in message.content.lower():
                user = bot.get_user(message.author.id)
                await user.send(MESSAGE)
                #await message.guild.ban(message.author) - Uncomment this line if you want the user to be banned as well.
                return

    await bot.process_commands(message)

@bot.command()
async def add(ctx, word: str):
    if not ctx.message.author.guild_permissions.administrator:
        await ctx.send("You must be admin to use this command")
        return


    with open('words.json') as json_file:
        existingData = json.load(json_file)
    data = existingData

    if str(ctx.guild.id) not in data:
        data[str(ctx.guild.id)] = []

    data[str(ctx.guild.id)].append(word.lower())
    

    await ctx.send("Added " + word + " to blacklisted words.")

    with open("words.json", "w") as write_file:
        json.dump(data, write_file)

@bot.command()
async def words(ctx):

    with open('words.json') as json_file:
        existingData = json.load(json_file)
    data = existingData

    if str(ctx.guild.id) not in data:
        await ctx.send("This server has no words configured!")
        return
    
    if len(data[str(ctx.guild.id)])==0:
        await ctx.send("This server has no words configured!")
        return

    message = "Blacklisted words: "

    for x in data[str(ctx.guild.id)]:
        message = message + x + ", "

    message = message[:-2]

    await ctx.send(message)

    with open("words.json", "w") as write_file:
        json.dump(data, write_file)

@bot.command()
async def remove(ctx, word: str):

    with open('words.json') as json_file:
        existingData = json.load(json_file)
    data = existingData

    if str(ctx.guild.id) not in data:
        await ctx.send("This server has no words configured!")
        return

    if word.lower() not in data[str(ctx.guild.id)]:
        await ctx.send("Word cannot be removed as it is not in blacklist!")
        return

    data[str(ctx.guild.id)].remove(word.lower())
    await ctx.send("Removed word: " + word)

    with open("words.json", "w") as write_file:
        json.dump(data, write_file)


bot.run(TOKEN)