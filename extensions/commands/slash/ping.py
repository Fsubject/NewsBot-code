import discord
from discord.ext import commands
from discord import app_commands


class PingCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="ping", description="Pong!")
    async def ping(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"{round(self.bot.latency * 1000)}ms  :ping_pong:", ephemeral=True)


async def setup(bot: commands.Bot):
    await bot.add_cog(PingCommand(bot))
