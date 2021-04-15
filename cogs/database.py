import discord
import discord.ext
from discord.ext import commands

class database(commands.Cog):
    db = 'reaction.db'

    def __init__(self, bot):
        self.bot = bot

    async def cog_command_error(self, ctx, error):
        print('Error in {0.command.qualified_name}: {1}'.format(ctx, error))

def setup(bot):
    bot.add_cog(database(bot))