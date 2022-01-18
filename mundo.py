"""
MONEY MAN MUNDO v0.1
"""
from discord import Intents
from discord.ext import commands
from dotenv import dotenv_values
from json import load
from random import choice
import logging

console = logging.StreamHandler()
console.setFormatter(logging.Formatter('[%(levelname)s]:: %(message)s', '%H:%M:%S'))
log = logging.getLogger(__name__)
log.addHandler(console)
log.setLevel(logging.DEBUG)

CONFIG = dotenv_values(".env")
WORDS = load(open('words.json'))['words']

intents = Intents.default()

bot = commands.Bot(command_prefix='',intents=intents)

@bot.event
async def on_ready():
    log.info("STARTING MONEY")
    log.info(f"Logged in as [{bot.user.name}] [ID: {bot.user.id}] \n")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.lower().startswith("mundo"):
        log.debug(f"{message.author.name}: {message.content}")
        await message.reply(choice(WORDS))

bot.run(CONFIG['TOKEN'])