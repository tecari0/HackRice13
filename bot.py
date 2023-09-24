import discord
from discord.ext import commands
import asyncio

from cogs.discord_api import recommend




# from dotenv import load_dotenv
# load_dotenv()

intents = discord.Intents.default()
bot = commands.Bot(command_prefix = commands.when_mentioned_or('/'), intents = intents)
intents.message_content = True

# discord_token = os.getenv("DISCORD_TOKEN")

@bot.event
async def on_ready():
	print(f'Logged in as {bot.user} (ID: {bot.user.id})')
	print('------')

async def main():
    try:
        await bot.load_extension("cogs.discord_api")
        await bot.load_extension("cogs.rps")
        # await bot.add_cog(recommend(bot))
        print('Extensions and cog loaded!')
    except Exception as e:
        print('Failed to load extensions and cog.')
        print(str(e))

    await bot.start('MTE1NDk3MDI3NzY2MzQ4NTk3Mg.G8TCNE.-sfxMla4CzX4fhiYc28szyrR_AThnu7xo4EFNk')

asyncio.run(main())

