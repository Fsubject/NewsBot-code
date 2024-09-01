import discord
from discord.ext import commands
from discord import app_commands
from discord.ext.commands import has_permissions
from extensions.database import Database
from settings import COUNTRY_LIST


class SetupCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="setup", description="Setup NewsBot's daily news feature")
    @app_commands.guild_only
    @has_permissions(administrator=True)
    @app_commands.choices(news_category=[ # Categories: top and other aren't possible because it's bullshit
        app_commands.Choice(name="All", value="all"),
        app_commands.Choice(name="Business", value="business"),
        app_commands.Choice(name="Crime", value="crime"),
        app_commands.Choice(name="Domestic", value="domestic"),
        app_commands.Choice(name="Education", value="education"),
        app_commands.Choice(name="Entertainment", value="entertainment"),
        app_commands.Choice(name="Environment", value="environment"),
        app_commands.Choice(name="Food", value="food"),
        app_commands.Choice(name="Health", value="health"),
        app_commands.Choice(name="Lifestyle", value="lifestyle"),
        app_commands.Choice(name="Politics", value="politics"),
        app_commands.Choice(name="Science", value="science"),
        app_commands.Choice(name="Sports", value="sports"),
        app_commands.Choice(name="Technology", value="technology"),
        app_commands.Choice(name="Tourism", value="tourism"),
        app_commands.Choice(name="World", value="world")
    ])
    async def setup_command(self, interaction: discord.Interaction, daily_news_channel_id: str, news_country: str, news_category: app_commands.Choice[str]):
        if self.bot.get_channel(int(daily_news_channel_id)) is not None:
            if self.bot.get_channel(int(daily_news_channel_id)).type == discord.ChannelType.text:
                if news_country in COUNTRY_LIST:
                    await interaction.response.defer(thinking=True)

                    await Database().update_guild({"news_channel_id": int(daily_news_channel_id), "news_country": news_country, "news_category": news_category.value}, interaction.guild_id)
                    print(f"{self.bot.user} has been configured on the following server: {interaction.guild.name} ({interaction.guild_id})")

                    await interaction.followup.send(f"Your server has been correctly configured!  :tada:\nDaily news will be sent in the channel: ``{daily_news_channel_id}``, the country of the selected news is set to ``{news_country}`` and the category is ``{news_category.value}``", ephemeral=True)
                else:
                    await interaction.response.send_message(f"The language you've chose isn't available or does not exist.\nMake sure to chose a language from this list:\n``{COUNTRY_LIST}``", ephemeral=True)
            else:
                await interaction.response.send_message("The channel you've chose isn't a text channel.", ephemeral=True)
        else:
            await interaction.response.send_message("This channel does not exist. Make sure to copy the right channel id.", ephemeral=True)


async def setup(bot: commands.Bot):
    await bot.add_cog(SetupCommand(bot))
