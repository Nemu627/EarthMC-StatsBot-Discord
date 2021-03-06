import discord
from discord.ext import commands
import traceback

class AppCmdEvent(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_ready(self):
        servers = len(self.bot.guilds)
        members = 0
        for guild in self.bot.guilds:
            members += guild.member_count - 1
        await self.bot.change_presence(
            activity=discord.Activity(name=f"//help | {str(servers)}servers | {str(members)}users", type=3)
        )

    @commands.Cog.listener()
    async def on_command_error(self,ctx, error):
        orig_error = getattr(error, "original", error)
        error_msg = "".join(traceback.TracebackException.from_exception(orig_error).format())
        if isinstance(error, commands.errors.MissingPermissions):
            embed = discord.Embed(
                title="エラー-不明なコマンド",
                description="不明なコマンドです。コマンドを確認してください。\n```" + error_msg + "```",
                colour=0x0000ff,
            )
            await ctx.reply(embed=embed)
        elif isinstance(error, commands.errors.MissingPermissions):
            embed = discord.Embed(
                title="エラー-権限不足",
                description="権限が不足しています。権限設定をご確認ください。\n```" + error_msg + "```",
                colour=0x0000ff,
            )
            await ctx.reply(embed=embed)
        else:
            embed = discord.Embed(
                title="エラー",
                description="予期せぬエラーが発生しました。\n```" + error_msg + "```",
                colour=0x0000ff,
            )
            await ctx.reply(embed=embed, mention_author=False)

def setup(bot):
    return bot.add_cog(AppCmdEvent(bot))
