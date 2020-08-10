import discord
from discord.ext import commands
from core.classes import Cog_Extention
import json
import asyncio

with open('setting.json',mode='r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

class Event(Cog_Extention):
    @commands.Cog.listener()
    async def on_member_join(self,member):
        wel_channel = self.bot.get_channel(int(jdata['welId']))
        await wel_channel.send(f'{member} join!')
        
    @commands.Cog.listener()
    async def on_member_remove(self,member):
        leave_channel = self.bot.get_channel(int(jdata['leaId']))
        await leave_channel.send(f'{member} leave!')
    
    @commands.Cog.listener()
    async def on_message(self,msg):
       
        if msg.content in jdata['keyword'] and msg.author != self.bot.user:
            await msg.channel.send('apple')

    @commands.Cog.listener()
    async def on_voice_state_update(self,member,before,after):
        voice_channel = self.bot.get_channel(int(jdata['welIdvoice']))
        if before.channel is None and after.channel is not None:
            if after.channel.name == 'voice':
                vc = await voice_channel.connect()
                vc.play(discord.FFmpegPCMAudio("D:\\github\\TT_BOT\\yahello.wav"))
                while True:
                    if vc.is_playing() == False:
                        await vc.disconnect()
                        break
                
def setup(bot):
    bot.add_cog(Event(bot))