import discord
import json
import requests
from edit import *
# from discord.ext import commands

bot = discord.Client()
call_bot = ';w'
help_word = 'help'
api_key = 'API KEY HERE'
token_key = 'TOKEN HERE'

@bot.event
async def on_ready():
    print('Bot is online.') 
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=';w'))

@bot.event
async def on_message(ctx):
    if ctx.author != bot.user and ctx.content.startswith(call_bot):
        location = ctx.content.replace(call_bot, '').lower()
        location = location.replace(" ", "")
        if len(location) >= 1 and location != help_word:
            #Weather data
            url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric'
            try:
                data = json.loads(requests.get(url).content)
                data = parse_data(data)
                await ctx.channel.send(embed = weather_message(data, location))
            except KeyError:
                await ctx.channel.send(embed = error_message(location))
        elif location == help_word:
            # print('TRUE')
            await ctx.channel.send(embed = help_message())
        else:
            await ctx.channel.send(embed = help_message())


bot.run(token_key)