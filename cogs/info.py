import random
import urllib.parse
import datetime
import sqlite3
import asyncio
import aiohttp
import os
import discord
from discord.ext import commands
import loadconfig

class info(commands.Cog):
    db = 'reaction.db'

    def __init__(self, bot):
        self.bot = bot

    async def cog_command_error(self, ctx, error):
        print('Error in {0.command.qualified_name}: {1}'.format(ctx, error))

    @commands.command()
    async def avatar(self, ctx, *, member: discord.Member = None):
        avatar = f"https://cdn.discordapp.com/avatars/{member.id}/{member.avatar}.png?size=1024"
        member = ctx.author if not member else member
        embed = discord.Embed(title=f":frame_photo: Avatar")
        embed.set_image(url=avatar)
        embed.set_footer(text=f"Angefragt von {ctx.author}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @commands.command(
        name='userinfo',
        description='The userinfo2 command',
        aliases=['ui', 'info']

    )
    async def embed_command(self, ctx, member: discord.Member):
        member = ctx.author if not member else member
        embed = discord.Embed(title=f" Userinfo", timestamp=ctx.message.created_at, color=0x4a4a4a)
        embed.set_thumbnail(url=member.avatar_url)
        embed.add_field(name=' Username:', value=f"{member.name}", inline=False)
        embed.add_field(name=" User ID:", value=f"{member.id}", inline=False)
        embed.set_footer(text=f"{ctx.author}", icon_url=ctx.author.avatar_url)
        embed.add_field(name=" Erstellt am:", value=member.created_at.strftime('%d.%m.%Y, %H:%M:%S'), inline=False)
        embed.add_field(name=" Beigetreten am:", value=member.joined_at.strftime('%d.%m.%Y, %H:%M:%S'), inline=False)
        embed.add_field(name=" Höchste Rolle:", value=member.top_role, inline=False)
        await ctx.send(embed=embed)

    @commands.command(aliases=['archive'])
    @commands.cooldown(1, 60, commands.cooldowns.BucketType.channel)
    async def log(self, ctx, *limit: int):
        '''Archiviert den Log des derzeitigen Channels und läd diesen als Attachment hoch

        Beispiel:
        -----------

        :log 100
        '''
        if not limit:
            limit = 10
        else:
            limit = limit[0]
        logFile = f'{ctx.channel}.log'
        counter = 0
        with open(logFile, 'w', encoding='UTF-8') as f:
            f.write(f'Archivierte Nachrichten vom Channel: {ctx.channel} am {ctx.message.created_at.strftime("%d.%m.%Y %H:%M:%S")}\n')
            async for message in ctx.channel.history(limit=limit, before=ctx.message):
                try:
                    attachment = '[Angehängte Datei: {}]'.format(message.attachments[0].url)
                except IndexError:
                    attachment = ''
                f.write('{} {!s:20s}: {} {}\r\n'.format(message.created_at.strftime('%d.%m.%Y %H:%M:%S'), message.author, message.clean_content, attachment))
                counter += 1
        msg = f':ok: {counter} Nachrichten wurden archiviert!'
        f = discord.File(logFile)
        await ctx.send(file=f, content=msg)
        os.remove(logFile)

    @log.error
    async def log_error(self, error, ctx):
        if isinstance(error, commands.errors.CommandOnCooldown):
            seconds = str(error)[34:]
            await ctx.send(f':alarm_clock: Cooldown! Versuche es in {seconds} erneut')



    @commands.command()
    async def version(self, ctx):
        embed = discord.Embed(timestamp=ctx.message.created_at, color=0x4a4a4a)
        embed.add_field(name='Bot Version', value=self.bot.botVersion, inline=True)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(info(bot))