from discord.ext import commands
from json import load
from loguru import logger


class CompetitionBot(commands.Cog):
    def __init__(self, bot):
        self.__bot = bot
        self.__competition_name = str()
        self.__players_points = dict()

    @commands.Cog.listener()
    async def on_ready(self):
        logger.debug('Bot is running!')

    @commands.command(aliases=['comp'])
    async def competition(self, ctx, *, comp_name):
        logger.debug('Competition function was called.')
        self.__competition_name = comp_name
        await ctx.send(f'-----> **{comp_name}** competition was created! <-----')


discord_bot = commands.Bot(command_prefix='')
discord_bot.add_cog(CompetitionBot(discord_bot))

with open('.globalresources.json') as global_resources:
    token = load(global_resources)['token']

discord_bot.run(token)
