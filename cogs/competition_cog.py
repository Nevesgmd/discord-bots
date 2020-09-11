from discord.ext import commands
from loguru import logger


class CompetitionCog(commands.Cog):
    def __init__(self, bot):
        self.__bot = bot
        self.__competitions = dict()

    @commands.Cog.listener()
    async def on_ready(self):
        logger.debug('Bot is running!')

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        await ctx.send(f'Error: {error}')
        await ctx.send(f'Type **examples** or **help** to get more information.')

    @commands.command(aliases=['comp', 'create'])
    async def competition(self, ctx, *, competition_name):
        """
        Creates the competition

        Practical examples:
        !comp ConnectFour
        !create MunchkinCompetition
        !competition CheckersLeague
        """
        logger.debug('Competition function was called.')
        self.__competitions[competition_name] = {}
        await ctx.send(f'-----> **{competition_name}** competition was created! <-----')

    @commands.command(aliases=['players'])
    async def add_players(self, ctx, competition_name, *players):
        """
        Add players to an existent competition

        Practical examples:
        !players ConnectFour Stewie2K Fallen
        !add_players Coldzera
        """
        if competition_name in self.__competitions:
            for player in players:
                self.__competitions[competition_name][player] = 0
                await ctx.send(f"--> **{player}** added to competition **{competition_name}**.")
                logger.debug(f'{player} added to competition {competition_name}')
        else:
            await ctx.send(f"!!--- The **{competition_name}** competition doesn't exist. ---!!")
            logger.debug(f'Trying to add players to an inexistent competition.')

    @commands.command(aliases=['add', 'points'])
    async def add_points(self, ctx, competition_name, player, points):
        """
        Add points to a player in a competition

        Practical examples:
        !add MunchkinCompetition Nevesgmd 80
        !add_points MunchkinCompetition brTT 75
        """
        try:
            self.__competitions[competition_name][player] += int(points)
            logger.debug(f'{points} points added to {player}!')
            await ctx.send(f'--> **{points}** points added to {player}!')
        except ValueError:
            logger.debug(f'Incorrect points parameter value on add_points()')
            await ctx.send(f'!!--- **Points** must be numeric ---!!')

    @commands.command(aliases=['rank'])
    async def ranking(self, ctx, competition_name):
        """
        Show ranking of a existent competition

        Practical examples:
        !rank CheckersLeague
        !ranking CheckersLeague
        """
        logger.debug('Ranking function called.')
        if competition_name in self.__competitions:
            await ctx.send(f'======== **{competition_name}** ========')
            rank = 1
            for player, points in sorted(self.__competitions[competition_name].items(),
                                         key=lambda x: x[1], reverse=True):
                await ctx.send(f'--> **{rank}.**   {player} - {points} points')
                rank += 1
            await ctx.send('================' + len(competition_name) * '=')
        else:
            await ctx.send(f"!!--- The **{competition_name}** competition doesn't exist. ---!!")
            logger.debug(f'Trying to show ranking of an inexistent competition.')
