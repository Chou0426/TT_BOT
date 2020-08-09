import discord
from discord.ext import commands
import json
import random
import os
import webbrowser
import re
with open('setting.json',mode='r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(">> Bot is online <<")



@bot.command()
async def load(ctx,extention):
    bot.load_extension(f'cmds.{extention}')
    await ctx.send(f'loaded {extention} done.')

@bot.command()
async def unload(ctx,extention):
    bot.unload_extension(f'cmds.{extention}')
    await ctx.send(f'unloaded {extention} done.')

@bot.command()
async def reload(ctx,extention):
    bot.reload_extension(f'cmds.{extention}')
    await ctx.send(f'reloading {extention} done.')

# 用command一定要有ctx

for fileName in os.listdir('./cmds'):
    if fileName.endswith('.py'):
        bot.load_extension(f'cmds.{fileName[:-3]}')

if __name__ =="__main__":
    bot.run(jdata['TOKEN'])