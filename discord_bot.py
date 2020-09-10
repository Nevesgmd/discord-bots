from cogs.competition_cog import CompetitionCog
from discord.ext import commands
from json import load

discord_bot = commands.Bot(command_prefix='!')
discord_bot.add_cog(CompetitionCog(discord_bot))

with open('.globalresources.json') as global_resources:
    token = load(global_resources)['token']

discord_bot.run(token)
