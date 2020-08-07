import discord
from discord.ext import commands
from core.classes import Cog_Extention

class Main(Cog_Extention):
    @commands.command()
    async def ping(self,ctx):
        await ctx.send(f'{round(self.bot.latency*1000)} (ms)')


    @commands.command()
    async def hi(self,ctx):
        await ctx.send('123')

def setup(bot):
    bot.add_cog(Main(bot))