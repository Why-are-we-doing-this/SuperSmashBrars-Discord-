from People.dummy import Dummy
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv



bot = commands.Bot(command_prefix = "o!")

load_dotenv()
token = os.getenv('token')

@bot.event 
async def on_ready():
	await bot.change_presence(status = discord.Status.online, activity = discord.Game("Jake Paul Boxing Sim"))
	print("I'm Ready")

@bot.command(aliases = ['hi'])
async def test(ctx):
	await ctx.send("EEEEEEEEEEEEE")


@bot.command(aliases = ["f"])
async def light(ctx):
	await ctx.send('dams beta')
	
@bot.command(aliases=["sh"])
@commands.is_owner()
async def shutdown(ctx):
    await ctx.bot.close()

@bot.command(aliases=["dm"])
@commands.is_owner()
async def message(ctx,*,user: discord.Member):
	msg = await bot.wait_for('message', check=None)
	await user.send(msg.content)



bot.load_extension('game')

bot.run(token) 





