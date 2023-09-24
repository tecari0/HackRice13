import discord
from discord.ext import commands
import asyncio
import os
import openai



from dotenv import load_dotenv
load_dotenv()

intents = discord.Intents.default()
bot = commands.Bot(command_prefix = commands.when_mentioned_or('/'), intents = intents)
intents.message_content = True

discord_token = os.getenv("DISCORD_TOKEN")

openai.api_key= os.getenv("CHATGPT_API_KEY")

class recommend(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command(name='ping', brief='ping', description='ping')
	async def ping(self, ctx: commands.Context):
		await ctx.channel.send(f'{ctx.author.mention} pong!')
		print("hello")

	@commands.command(name='fuck', brief='fuck someone', description='fuc someone')
	async def fuck(self, ctx : commands.Context, member: discord.Member = commands.parameter(description='The member you want to challenge')):
		await ctx.channel.send(f'{ctx.author.mention} wants to fuck {member.mention}')
		print("get fucced")

	@commands.command(name='recommend', brief='recommend songs', description='recommend some songs based on input or mood', aliases=['mood'])
	async def reccomend(self, ctx: commands.Context, *args):
		message = " ".join(args)
		print(message)

	
		await ctx.channel.send(f'{ctx.author.mention} ur mum says hi!')
		bot_response = chatgpt_response(message)
		await ctx.channel.send(f'{ctx.author.mention} ur mum says hi again omg it work???!')
		try:
			resp = await asyncio.wait_for(ctx.channel.send(f"Here are some recommendations based on your input! Hope you enjoy! {bot_response}"), timeout=20)
		except asyncio.TimeoutError: # Handle the TimeoutError here
			await ctx.channel.send("Bot timed out after 20 seconds, please try again")


def chatgpt_response(prompt):
	messages = [{"role": "user", "content": "give a list of songs with the following prompt:" + prompt}]
	response = openai.Completion.create(
	model = "gpt-3.5-turbo-0613",
	messages = messages,
	temperature = 1,
	max_tokens = 100
	)
	print("ur mom says hi here in the call function omg")
	prompt_response = ""
	response_dict = response.get("choices")
	if response_dict and len(response_dict) > 0:
		prompt_response = response_dict[0]["text"]
	return prompt_response

async def setup(client):
    await client.add_cog(recommend(client))