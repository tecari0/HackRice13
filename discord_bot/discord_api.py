import discord
from discord.ext import commands
import asyncio
from cogs import music_cog
from cogs import help_cog
from chatgpt_api import chatgpt_response

from dotenv import load_dotenv
import os

load_dotenv()

discord_token = os.getenv("DISCORD_TOKEN")

class MyClient(discord.Client):
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