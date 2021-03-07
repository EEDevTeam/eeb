import os
import sys
import discord
import discord.ext
from discord.ext import commands
import json





class botsetup(commands.Cog):
    db = 'reaction.db'

    def __init__(self, bot):
        self.bot = bot

    async def cog_command_error(self, ctx, error):
        print('Error in {0.command.qualified_name}: {1}'.format(ctx, error))

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def setprefix(self, ctx, prefix):
        '''Endert den bot Prefix für deinen Server (admin ONLY)'''
        with open('database/prefixes.json', 'r') as f:
            prefixes = json.load(f)

        prefixes[str(ctx.guild.id)] = prefix

        with open('database/prefixes.json', 'w') as f:
            json.dump(prefixes, f, indent=4)
        await ctx.send(f'Prefix set to {prefix}')

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def setlanguages(self, ctx, lang):
        '''Endert die Sprache für deinen Server (admin ONLY)'''
        with open('database/languages.json', 'r') as f:
            prefixes = json.load(f)

        prefixes[str(ctx.guild.id)] = lang

        with open('database/languages.json', 'w') as f:
            json.dump(prefixes, f, indent=4)
        await ctx.send(f'languages set to {lang}')






def setup(bot):
    bot.add_cog(botsetup(bot))