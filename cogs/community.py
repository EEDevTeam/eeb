import discord
import discord.ext
import asyncio
from discord.ext import commands


class community(commands.Cog):
    db = 'reaction.db'

    def __init__(self, bot):
        self.bot = bot

    async def cog_command_error(self, ctx, error):
        print('Error in {0.command.qualified_name}: {1}'.format(ctx, error))

    @commands.command(name=['idea'])
    async def idea(self, ctx, *, ideavab):
        await ctx.send(name="Deine idea Wird bearbeitet:ㅤㅤㅤ", value=ideavab)



def setup(bot):
    bot.add_cog(community(bot))