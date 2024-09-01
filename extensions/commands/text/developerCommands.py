import discord
from discord.ext import commands
from extensions.news import News
from extensions.database import Database


class DeveloperCommands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def close(self, ctx):
        await ctx.reply("Shutting down the bot.")
        print("\nBye bye")
        await Database().close()
        await self.bot.close()

    @commands.command()
    @commands.is_owner()
    async def sync(self, ctx):
        synced = await self.bot.tree.sync()
        print(f"{ctx.author} synced {len(synced)} commands")
        await ctx.reply(f"Synced {len(synced)} commands.")

    @commands.command()
    @commands.is_owner()
    async def test(self, ctx):
        article = await News().get_article("us", "health")
        await ctx.reply(embed=article)


async def setup(bot: commands.Bot):
    await bot.add_cog(DeveloperCommands(bot))
