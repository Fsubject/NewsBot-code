import discord
from discord.ext import commands, tasks
import datetime
from extensions.database import Database
from settings import DAILY_NEWS_TIMEZONE
from extensions.news import News


class DailyNews(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.daily_news.start()

    @commands.command(name="cancel_news")
    async def cancel_news(self, ctx):
        self.daily_news.cancel()
        print(f"Daily news task cancelled by {ctx.author}")
        await ctx.reply("Daily news task has been cancelled. Restart the bot to restart the task.")

    @tasks.loop(time=datetime.time(hour=18, minute=2, second=0, tzinfo=DAILY_NEWS_TIMEZONE))
    async def daily_news(self):
        print("Time to send the daily news...")

        for guild in self.bot.guilds:
            guild_settings = await Database().get_guild(guild.id)
            guild_settings = guild_settings[0]

            if self.bot.get_channel(guild_settings["news_channel_id"]).type == discord.ChannelType.text:
                article = await News().get_article(guild_settings["news_country"], guild_settings["news_category"])

                if article is not None:
                    await self.bot.get_channel(guild_settings["news_channel_id"]).send(embed=article)
                else:
                    await self.bot.get_channel(guild_settings["news_channel_id"]).send(f"No news were found from the country: ``{guild_settings["news_country"]}`` and related to the category: ``{guild_settings["news_category"]}``  :sob:\nYou can still change your parameters using the command ``/setup``...")

        print("Daily news has been sent to all the configured server")

    @daily_news.before_loop
    async def before_daily_news_task(self):
        await self.bot.wait_until_ready()


async def setup(bot: commands.Bot):
    await bot.add_cog(DailyNews(bot))