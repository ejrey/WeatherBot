import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = ';wb')
call_bot = ';wb'

@bot.event
async def on_ready():
    print('Bot is online.')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=';wb'))

# @bot.command() #Get will say get function to do something
# async def wb(ctx):
#     await ctx.send('Test!')

# @bot.event
# async def on_message(message):
#     if message.author != bot.user and message.content.startswith(call_bot)



bot.run('TOKEN')
