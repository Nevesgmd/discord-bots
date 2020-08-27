from discord.ext import commands
from json import load
from loguru import logger

client = commands.Bot(command_prefix=' ')


@client.event
async def on_ready():
    logger.debug('Bot is running.')

with open('.globalresources.json') as global_resources:
    token = load(global_resources)['token']
    print(token)

client.run(token)
