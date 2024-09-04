# News api -> newsdata.io

import discord
from settings import NEWS_API_KEY
from newsdataapi import NewsDataApiClient
from extensions.database import Database
import random

api = NewsDataApiClient(apikey=NEWS_API_KEY)


class News:
    def __init__(self):
        self.api = api
        self.article = {}

    async def get_article(self, country, category, language):
        while len(self.article) == 0:
            returned_articles = await Database().get_articles(country, category, language)

            if len(returned_articles) > 1:
                self.article = random.choice(returned_articles)
            elif len(returned_articles) == 1:
                self.article = returned_articles
            else:
                if await self.scrap_articles(country, category, language) is None:
                    return None

        return await self.build_news_embed()

    async def scrap_articles(self, country, category, language):
        raw_articles = None

        try:
            if category == "all":
                raw_articles = self.api.latest_api(country=country, language=language)
            else:
                raw_articles = self.api.latest_api(country=country, category=category, language=language)
        except Exception as e:
            print(f"An error occurred while trying to scrap the news with the following parameters: {country}, {category}, {language} -> {e}")

        articles = raw_articles["results"]

        if len(articles) <= 0:
            return None

        sorted_articles = []

        for article in articles:
            if article["description"] is None:
                article["description"] = "No description available. Click on the link to read the full article. Sorry =/"
            elif len(article["description"]) >= 350:
                article["description"] = article["description"][:347] + "..."

            sorted_articles.append([country, article["category"][0], language, article["title"], article["description"], article["link"], article["image_url"]])

        await Database().insert_articles(sorted_articles)

        return 1

    async def build_news_embed(self):
        article_embed = discord.Embed(title=self.article["article_title"], description=self.article["article_description"], color=0x0099FF, url=self.article["article_link"])
        article_embed.set_author(name="NewsBot", icon_url="http://57.128.213.195/images/botzilla_logo.png")
        article_embed.set_image(url=self.article["article_image"])
        article_embed.set_footer(text="News obtained from newsdata.io")

        return article_embed
