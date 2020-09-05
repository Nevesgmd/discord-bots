from discord.ext import commands
from loguru import logger


class CompetitionCog(commands.Cog):
    def __init__(self, bot):
        self.__bot = bot
        self.__competitions = dict()

    @commands.Cog.listener()
    async def on_ready(self):
        logger.debug('Bot is running!')

    @commands.command(aliases=['comp', 'create'])
    async def competition(self, ctx, *, comp_name):
        logger.debug('Competition function was called.')
        self.__competitions[comp_name] = {}
        await ctx.send(f'-----> **{comp_name}** competition was created! <-----')

    @commands.command(aliases=['players'])
    async def add_players(self, ctx, comp_name, *players):
        if comp_name in self.__competitions:
            for player in players:
                self.__competitions[comp_name][player] = 0
                await ctx.send(f"--> **{player}** added to competition **{comp_name}**.")
                logger.debug(f'{player} added to competition {comp_name}')
        else:
            await ctx.send(f"!!--- The **{comp_name}** competition doesn't exist. ---!!")
            logger.debug(f'Trying to add players to an inexistent competition.')

    @commands.command(aliases=['add', 'points'])
    async def add_points(self, ctx, comp, player, points):
        try:
            self.__competitions[comp][player] += int(points)
            logger.debug(f'{points} points added to {player}!')
            await ctx.send(f'--> **{points}** points added to {player}!')
        except ValueError:
            logger.debug(f'Incorrect points parameter value on add_points()')
            await ctx.send(f'!!--- **Points** must be numeric ---!!')

    @commands.command(aliases=['rank'])
    async def ranking(self, ctx, comp):
        logger.debug('Ranking function called.')
        if comp in self.__competitions:
            await ctx.send(f'======== **{comp}** ========')
            rank = 1
            for player, points in sorted(self.__competitions[comp].items(), key=lambda x: x[1], reverse=True):
                await ctx.send(f'--> **{rank}.**   {player} - {points} points')
                rank += 1
            await ctx.send('================' + len(comp) * '=')
        else:
            await ctx.send(f"!!--- The **{comp}** competition doesn't exist. ---!!")
            logger.debug(f'Trying to show ranking of an inexistent competition.')

    @commands.command(aliases=['get'])
    async def get_comp_values(self, ctx):
        await ctx.send(f'{self.__competitions}')
        logger.debug(f'{self.__competitions}')
