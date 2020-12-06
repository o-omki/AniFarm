import discord
from discord.ext import commands
import sqlite3
import os
from useless import keep_alive
import requests
import asyncio 

#import time




bot= commands.Bot(command_prefix="sus!", owner_ids={414066242476048384, 373718038010396675})
#up_time= time.time
bot.remove_command("help")


@bot.event
async def on_ready():
	status1 = discord.Status.online
	Game = discord.Game("Cats... ~nyaa")
	await bot.change_presence(status = status1, activity = Game)
	print("The bot is ready!")
	cogs = ['cogs.FinishedPoster', "cogs.ProgressPoster", "cogs.QueuePoster", "cogs.Custom", "cogs.Cute", "cogs.OrderPage", "cogs.OrderEdit"]
	for cog in cogs:
				
		try:
			bot.load_extension(cog)
			print(f"{cog} loaded.")
		except Exception :
			print(Exception)
		
	mydb= sqlite3.connect("farm.sqlite")
	cursor= mydb.cursor()
	cursor.execute("create table if not exists FARM(Farmer_ID text, Buyer_ID text, Card_Name text, Xp_Amount text, Loc text, Price text, Farm_ID text)")
	cursor.execute("create table if not exists CUSTOM(Farmer_ID text, Custom_Msg text)")
		
	while bot.is_ready:
		requests.get("https://farmingbot.omki.repl.co")
		await asyncio.sleep(60)


								
		


@bot.event
async def on_message(message):
	if message.author == bot.user:
		return
	await bot.process_commands(message)

keep_alive()
token= os.environ.get("TOKEN")
bot.run(token, bot = True, reconnect = True)
