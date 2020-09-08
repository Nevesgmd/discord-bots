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
    async def competition(self, ctx, *, comp_name):
        """
        Creates the competition
        :param ctx: context (default discord.py parameter)
        :param comp_name: name of the competition
        :return: None
        """
        logger.debug('Competition function was called.')
        self.__competitions[comp_name] = {}
        await ctx.send(f'-----> **{comp_name}** competition was created! <-----')

    @commands.command(aliases=['players'])
    async def add_players(self, ctx, comp_name, *players):
        """
        Add players to an existent competition
        :param ctx: context (default discord.py parameter)
        :param comp_name: name of the competition
        :param players: player names (one or more)
        :return: None
        """
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
        """
        Add points to a player in a competition
        :param ctx: context (default discord.py parameter)
        :param comp: name of the competition
        :param player: name of the player
        :param points: number of points to be added
        :return: None
        """
        try:
            self.__competitions[comp][player] += int(points)
            logger.debug(f'{points} points added to {player}!')
            await ctx.send(f'--> **{points}** points added to {player}!')
        except ValueError:
            logger.debug(f'Incorrect points parameter value on add_points()')
            await ctx.send(f'!!--- **Points** must be numeric ---!!')

    @commands.command(aliases=['rank'])
    async def ranking(self, ctx, comp):
        """
        Show ranking of a existent competition
        :param ctx: context (default discord.py parameter)
        :param comp: name of the competition
        :return: None
        """
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

    @commands.command(aliases=['ex'])
    async def examples(self, ctx):
        await ctx.send('**Examples:**')
        await ctx.send('--> !comp competition_name')
        await ctx.send('--> !players competition_name player1 player2 player3')
        await ctx.send('--> !add competition_name player_name points')
        await ctx.send('--> !rank competition_name')
