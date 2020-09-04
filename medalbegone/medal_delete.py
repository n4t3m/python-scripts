import discord
from discord.ext import commands
import setup



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
async def on_message(message):
    if message.author == client.user:   
        return
    if "medal.tv" in message.content and message.author.id !=299685173262286849:
        print("liberal destroyed: " + message.author.name)
        await message.delete()  
        
    await client.process_commands(message)


    
  


client.run(TOKEN)
            