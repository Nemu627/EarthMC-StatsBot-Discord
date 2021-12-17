import discord
from discord.ext import commands
import asyncio
import aiohttp

class AppCmdVariety(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
    
    @commands.command()
    async def test(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get(
                "http://earthmc-api.herokuapp.com/allplayers/Oniyao228"
            ) as response:
                res = await response.json()
                embed = discord.Embed(title="test",description=res["nation"])
                await ctx.reply(embed=embed)
    
    @commands.command()
    async def testt(self,ctx,user="Nemu627"):
        async with aiohttp.ClientSession() as session:
            async with session.get(
                "http://earthmc-api.herokuapp.com/onlineplayers/"+user
            ) as response:
                res = await response.json()
                if res["name"] == user:
                    await ctx.reply("online")
                else:
                    await ctx.reply("offline")
        

def setup(bot):
    return bot.add_cog(AppCmdVariety(bot))
