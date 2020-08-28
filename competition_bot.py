from discord.ext import commands
from json import load
from loguru import logger

client = commands.Bot(command_prefix='')


@client.event
async def on_ready():
    logger.debug('Bot is running.')


@client.command(aliases=['comp'])
async def competition(ctx, *, comp_name):
    logger.debug('Competition function was called.')
    await ctx.send(f'{comp_name} competition was created!')


with open('.globalresources.json') as global_resources:
    token = load(global_resources)['token']

client.run(token)
