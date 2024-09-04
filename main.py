import discord
from discord.ext import commands
from discord.ext.commands import errors
from settings import EXTENSIONS, INTENTS, ACTIVITY, DISCORD_API_KEY
from extensions.database import Database


class NewsBot(commands.Bot):
    async def on_ready(self):
        print(f"\nLogged in as {self.user}\n")

        try:
            for extension in EXTENSIONS:
                await self.load_extension(extension)
                print(f"{extension} has been successfully loaded")
        except Exception as e:
            print(f"An error occurred while loading an extension -> {e}")

        print("")

    async def on_guild_join(self, guild):
        print(f"{self.user} has been added to the guild: {guild.name} ({guild.id})\nInserting new guild into database...")
        result = await Database().get_guild(guild.id)

        if result == []:
            await Database().insert_guild(guild.name, guild.id)
        else:
            await Database().update_guild({"guild_name": guild.name, "is_active": True}, guild.id)

    async def on_guild_remove(self, guild):
        print(f"{self.user} has been removed from the guild: {guild.name} ({guild.id})")
        await Database().update_guild({"guild_name": guild.name, "is_active": False}, guild.id)

    """async def on_command_error(self, ctx, exception: errors.CommandError):
        if isinstance(exception, commands.PrivateMessageOnly):
            await ctx.reply("This command can only be used in private message.")
        elif isinstance(exception, commands.CommandNotFound):
            await ctx.reply("This command doesn't exist.")
        elif isinstance(exception, commands.BotMissingPermissions):
            await ctx.reply("I am missing a required permission to run this command. Please make sure that I have all the required permission.")
        elif isinstance(exception, commands.MissingPermissions):
            await ctx.reply("You do not have the required permission to run this command.")"""


bot = NewsBot(command_prefix="n!", intents=INTENTS, activity=ACTIVITY)
bot.run(DISCORD_API_KEY)

# Made by Fsubject (fsubject on discord)
