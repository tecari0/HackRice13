import discord
from discord.ext import commands

class help_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.help_message = """
```
General commands:
/help - displays all available commands
/p <keywords> - finds the song on youtube and plays it
/q - displays the current queue
/skip - skips the current song
/clear - stops the music and clears the queue
/leave - disconnected the bot from the voice channel
/pause - pauses the current song
/resume - resumes the current song
```

"""

        self.text_channel = []
        
    @commands.Cog.listener()
    async def on_ready(self):
        for guild in self.bot.guilds:
            for channel in guild.text_channels:
                self.text_channel.append(channel)
        await self.send_to_all(self.help_message)

    async def send_to_all(self, message):
        for text_channel in self.text_channel_text:
            await text_channel.send(message)
