import os
from dotenv import load_dotenv
import discord
import pytz
import datetime

load_dotenv(".env")

# Keys & passwd
DISCORD_API_KEY = os.getenv("DISCORD_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
DATABASE_USERNAME = os.getenv("DATABASE_USERNAME")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
DATABASE_HOST = os.getenv("DATABASE_HOST")
DATABASE_NAME = os.getenv("DATABASE_NAME")

# Bot extensions
EXTENSIONS = [
    "extensions.commands.slash.ping",
    "extensions.commands.slash.setup",
    "extensions.commands.text.developerCommands",
    "extensions.commands.text.usersCommands",
    "extensions.tasks.newsTask"
]

# Bot configuration
ACTIVITY = discord.Activity(type=discord.ActivityType.watching, name="the news!")
INTENTS = discord.Intents.default()
INTENTS.message_content = True

# List of countries
COUNTRY_LIST = ["af", "al", "dz", "ad", "ao", "ar", "am", "au", "at", "az", "bs", "bh", "bd", "bb", "by", "be", "bz", "bj", "bm", "bt", "bo", "ba", "bw", "br", "bn", "bg", "bf", "bi", "kh", "cm", "ca", "cv", "ky", "cf", "td", "cl", "cn", "co", "km", "cg", "ck", "cr", "hr", "cu", "cw", "cy", "cz", "dk", "dj", "dm", "do", "cd", "ec", "eg", "sv", "gq", "er", "ee", "sz", "et", "fj", "fi", "fr", "pf", "ga", "gm", "ge", "de", "gh", "gi", "gr", "gd", "gt", "gn", "gy", "ht", "hn", "hk", "hu", "is", "in", "id", "ir", "iq", "ie", "il", "it", "ci", "jm", "jp", "je", "jo", "kz", "ke", "ki", "xk", "kw", "kg", "la", "lv", "lb", "ls", "lr", "ly", "li", "lt", "lu", "mo", "mk", "mg", "mw", "my", "mv", "ml", "mt", "mh", "mr", "mu", "mx", "fm", "md", "mc", "mn", "me", "ma", "mz", "mm", "na", "nr", "np", "nl", "nc", "nz", "ni", "ne", "ng", "kp", "no", "om", "pk", "pw", "ps", "pa", "pg", "py", "pe", "ph", "pl", "pt", "pr", "qa", "ro", "ru", "rw", "lc", "sx", "ws", "sm", "st", "sa", "sn", "rs", "sc", "sl", "sg", "sk", "si", "sb", "so", "za", "kr", "es", "lk", "sd", "sr", "se", "ch", "sy", "tw", "tj", "tz", "th", "tl", "tg", "to", "tt", "tn", "tr", "tm", "tv", "ug", "ua", "ae", "gb", "us", "uy", "uz", "vu", "va", "ve", "vi", "vg", "wo", "ye", "zm", "zw"]

# Daily news timezone
DAILY_NEWS_TIMEZONE = datetime.datetime.now(pytz.timezone("Europe/Brussels")).tzinfo
