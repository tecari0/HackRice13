import discord
from discord.ext import commands
import asyncio
from music_cog import music_cog
from help_cog import help_cog
import openai.py

from dotenv import load_dotenv
import os

load_dotenv()

discord_token = os.getenv("DISCORD_TOKEN")

class MyClient(discord.Client):
    @bot.event
    async def on_ready(self):
        print("Successfully logged on as: ", self.user)

	async def on_message(self, message):
		activate = ["/reccomend", "/mood"]
		print(message.content)
		if message.author == self.user:
			return
		command, user_message = None, None
	
		for text in activate:
			if message.content.startswith(text):
				command = message.content.split('')[0]
				user_message = message.content.replace(text, '')
				print(command, user_message)
    
		if command in activate: 
			bot_response = chatgpt_response(prompt = user_message)
			try:
				resp = await asyncio.wait_for(message.channel.send(f"Answer: {bot_response}"), timeout=20)
			except asyncio.TimeoutError:
				# Handle the TimeoutError here
				await message.channel.send("Bot response timed out after 20 seconds, please try again")
				

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)



intents = discord.Intents.all()
bot = commands.Bot(command_prefix=commands.when_mentioned_or("!"), intents=intents)


bot.add_cog(help_cog(bot))
bot.add_cog(music_cog(bot))


async def main():
	await bot.start(discord_token)

@bot.command()
async def timer(ctx: commands.Context, time: int):
	await asyncio.sleep(time)
	await ctx.send("your time is up!")
