import asyncio
import discord
import discord.ext
from discord.ext import commands
import json
import loadconfig



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

    @commands.command()
    async def suport(self, ctx):
        '''Einladung für den suport server'''
        await ctx.send(self.bot.botsup)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def setup(self, ctx):
        '''Richtit den bot für deinen Server ein!'''
        msg = await ctx.send('Beantworte die folgenden Fragen!')

        questions = [
            "Welche Sprache sprichst du?",
            "Welches Prefix möchtest du?"
        ]

        answers = []

        def check(self):
            return self.author == ctx.author

        for i in questions:
            await ctx.send(i)

            try:
                msg = await self.bot.wait_for('message', timeout=30.0, check=check)

            except asyncio.TimeoutError:
                await ctx.send(':timer: Die Zeit ist leider abgelaufen.')
                return
            else:
                answers.append(msg.content)

        spracheaw = answers[0]
        prefixaw = answers[1]

        embed = discord.Embed(
            title=":timer:Setup erfolreich",
            color=ctx.author.color,
            timestamp=ctx.message.created_at)

        embed.add_field(name="Sprache:", value=f"{spracheaw}")
        embed.add_field(name="Prefix:", value=f"{prefixaw}")

        embed.set_footer(
            text=f"Schreibe {answers[1]}setup um das Setup neu durchzuführen!")

        my_msg = await ctx.channel.send(embed=embed)
        with open('database/prefixes.json', 'r') as f:
            prefixes = json.load(f)

        prefixes[str(ctx.guild.id)] = prefixaw

        with open('database/prefixes.json', 'w') as f:
            json.dump(prefixes, f, indent=4)

def setup(bot):
    bot.add_cog(botsetup(bot))