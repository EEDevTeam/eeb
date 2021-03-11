import asyncio
import sys
import json
import discord
import discord.ext
from discord.ext import commands

class todo(commands.Cog):
    db = 'reaction.db'

    def __init__(self, bot):
        self.bot = bot

    async def cog_command_error(self, ctx, error):
        print('Error in {0.command.qualified_name}: {1}'.format(ctx, error))

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def todoadd(self, ctx, *, todoadd):
        '''Fügt etwas auch deine todo list hinzu!'''
        with open('database/todo.json', 'r') as f:
            todos = json.load(f)

        todos[str(ctx.message.author.id)] = todoadd

        with open('database/todo.json', 'w') as f:
            json.dump(todos, f, indent=4)
        await ctx.send(f'Added {todoadd}')

def setup(bot):
    bot.add_cog(todo(bot))