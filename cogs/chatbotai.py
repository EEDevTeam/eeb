import discord
import discord.ext
import asyncio
from discord.ext import commands

class chatbotai(commands.Cog):
    db = 'reaction.db'

    def __init__(self, bot):
        self.bot = bot

    async def cog_command_error(self, ctx, error):
        print('Error in {0.command.qualified_name}: {1}'.format(ctx, error))

    @commands.command(aliases=['testai', 'ai'])
    async def chatai(self, ctx):
        await ctx.send('Chat ai test!')


def setup(bot):
    bot.add_cog(chatbotai(bot))