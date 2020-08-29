from discord.ext import commands
from json import load
from loguru import logger


class CompetitionBot(commands.Cog):
    def __init__(self, bot):
        self.__bot = bot
        self.__competitions = dict()

    @commands.Cog.listener()
    async def on_ready(self):
        logger.debug('Bot is running!')

    @commands.command(aliases=['comp'])
    async def competition(self, ctx, *, comp_name):
        logger.debug('Competition function was called.')
        self.__competitions[comp_name] = {}
        await ctx.send(f'-----> **{comp_name}** competition was created! <-----')

    @commands.command(aliases=['add'])
    async def add_players(self, ctx, comp_name, *players):
        try:
            for player in players:
                self.__competitions[comp_name][player] = 0
                await ctx.send(f"--> **{player}** added to competition **{comp_name}**.")
                logger.debug(f'{player} added to competition {comp_name}')
        except KeyError:
            await ctx.send(f"---!! The **{comp_name}** competition doesn't exist. !!---")
            logger.debug(f'Trying to add players to an inexistent competition.')

    @commands.command(aliases=['get'])
    async def get_comp_values(self, ctx):
        await ctx.send(f'{self.__competitions}')
        logger.debug(f'{self.__competitions}')


discord_bot = commands.Bot(command_prefix='')
discord_bot.add_cog(CompetitionBot(discord_bot))

with open('.globalresources.json') as global_resources:
    token = load(global_resources)['token']

discord_bot.run(token)
