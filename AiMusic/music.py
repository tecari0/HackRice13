#WaLLE
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import youtube_dl


load_dotenv()

discord_token = os.getenv("discord_token")

intents = discord.Intents().all()
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='!',intents=intents)


youtube_dl.utils.bug_reports_message = lambda: ''

ytdl_format_options = {
    'format': 'bestaudio/best',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' 
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)
        self.data = data
        self.title = data.get('title')
        self.url = ""

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))
        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]
        filename = data['title'] if stream else ytdl.prepare_filename(data)
        return filename


@bot.command(name='download_song', help='To download song')
async def play(ctx, url):
    try:
        server = ctx.message.guild
        voice_channel = server.voice_client

        async with ctx.typing():
            filename = await YTDLSource.from_url(url, loop=bot.loop)
            await ctx.send('**Now playing:** {}'.format(filename))
    except Exception as e:
        await ctx.send("Error: ".format(str(e)))


@bot.command(name='join', help='Tells the bot to join the voice channel')
async def join(ctx):
    if not ctx.author.voice or not ctx.author.voice.channel:
        await ctx.send("{} is not connected to a voice channel".format(ctx.author.name))
        return
    else:
        channel = ctx.author.voice.channel
    await channel.connect()


@bot.event
async def on_ready():
    print('Running!')
    for guild in bot.guilds:
        for channel in guild.text_channels :
            if str(channel) == "general" :
                await channel.send('Bot Activated..')
                await channel.send(file=discord.File('giphy.png'))
        print('Active in {}\n Member Count : {}'.format(guild.name,guild.member_count))


@bot.command(help = "Prints details of Server")
    
@bot.event
async def on_member_join(member):
     for channel in member.guild.text_channels :
         if str(channel) == "general" :
             on_mobile=False
             if member.is_on_mobile() == True :
                 on_mobile = True
             await channel.send("Welcome to the Server {}!!\n On Mobile : {}".format(member.name,on_mobile))             
        
# TODO : Filter out swear words from messages


if __name__ == "__main__" :
    @bot.event
    async def on_ready():
        print(f'Logged in as {bot.user} (ID: {bot.user.id})')
        print('------')
    bot.run(discord_token)