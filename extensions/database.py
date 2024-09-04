# Used database type -> PostgreSQL

from settings import DATABASE_USERNAME, DATABASE_PASSWORD, DATABASE_HOST, DATABASE_NAME
import asyncpg


class Database:
    def __init__(self):
        self.connection = None

    async def connect(self):
        if self.connection is None:
            self.connection = await asyncpg.connect(user=DATABASE_USERNAME, password=DATABASE_PASSWORD, host=DATABASE_HOST, database=DATABASE_NAME)

    async def close(self):
        if self.connection is not None:
            await self.connection.close()
            self.connection = None

    # Query management for the news

    async def get_articles(self, country, category, language):
        await self.connect()

        try:
            result = await self.connection.fetch('SELECT * FROM articles WHERE "article_country" = $1 AND "article_category" = $2 AND "article_language" = $3;', country, category, language)
        finally:
            await self.close()

        return result

    async def insert_articles(self, articles):
        await self.connect()

        try:
            async with self.connection.transaction():
                for article in articles:
                    await self.connection.execute('INSERT INTO articles("article_country", "article_category", "article_language", "article_title", "article_description", "article_link", "article_image") VALUES ($1, $2, $3, $4, $5, $6, $7);', article[0], article[1], article[2], article[3], article[4], article[5], article[6])
        finally:
            await self.close()

    # Query management for the guilds

    async def get_guild(self, guild_id):
        await self.connect()

        try:
            result = await self.connection.fetch('SELECT * FROM guilds WHERE "guild_id" = $1;', guild_id)
        finally:
            await self.close()

        return result

    async def insert_guild(self, guild_name, guild_id):
        await self.connect()

        try:
            await self.connection.execute('INSERT INTO guilds("guild_name", "guild_id") VALUES ($1, $2);', guild_name, guild_id)
        finally:
            await self.close()

    async def update_guild(self, changes, guild_id):
        await self.connect()

        try:
            async with self.connection.transaction():
                for change in changes.items():
                    await self.connection.execute(f'UPDATE guilds SET "{change[0]}" = $1 WHERE "guild_id" = $2', change[1], guild_id)
        finally:
            await self.close()
