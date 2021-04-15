import asyncio as asyncio
import discord
import discord.ext
from discord.ext import commands
import gtts
from gtts import gTTS
from mutagen.mp3 import MP3
import os

class tts(commands.Cog):
    db = 'reaction.db'

    def __init__(self, bot):
        self.bot = bot

    async def cog_command_error(self, ctx, error):
        print('Error in {0.command.qualified_name}: {1}'.format(ctx, error))

    @commands.command()
    async def tts(self, ctx, *, ttsword):
        '''tts'''
        os.remove("output.mp3")
        myText = ttsword
        language = 'de'
        output = gTTS(text=myText, lang=language, slow=False)
        output.save("output.mp3")
        audio = MP3("output.mp3")
        print(audio.info.length)
        guild = ctx.guild
        voice = await ctx.message.author.voice.channel.connect()
        voice.play(discord.FFmpegPCMAudio('output.mp3'))
        counter = 0
        duration = audio.info.length  # In seconds
        while not counter >= duration:
            await asyncio.sleep(1)
            counter = counter + 1
        await voice.disconnect()


def setup(bot):
    bot.add_cog(tts(bot))