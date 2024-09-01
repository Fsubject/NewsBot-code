import discord
from discord.ext import commands


class UsersCommands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    @commands.dm_only()
    async def tos(self, ctx):
        await ctx.reply("https://github.com/Fsubject/NewsBot/blob/main/ToS.md")

    @commands.command()
    @commands.dm_only()
    async def pp(self, ctx):
        await ctx.reply("https://github.com/Fsubject/NewsBot/blob/main/Privacy-Policy.md")


async def setup(bot: commands.Bot):
    await bot.add_cog(UsersCommands(bot))
