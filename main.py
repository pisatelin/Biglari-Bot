import discord
from discord.ext import commands
import json
import os
import random
import requests
import yahoo_fin
from yahoo_fin import stock_info as si

# Get configuration.json
with open("biglari_bot\configuration.json") as config: 
	data = json.load(config)
	token = data["token"]
	prefix = data["prefix"]
	owner_id = data["owner_id"]

#retrieves stock prices for the "holdings" command
	price =("\n$"+ str(round(si.get_live_price("BH"),2)))
	price2 =("\n$"+ str(round(si.get_live_price("BH-A"),2)))

bot = discord.Client()
# Intents
intents = discord.Intents.default()
# The bot
bot = commands.Bot(prefix, intents = intents, owner_id = owner_id)
#lists for the randomized commands
sins = ["Stop! You have commited crimed against Biglari Holdings and her people! What say you in your defense?", "We await your return to the resturuant.", "Even in chosing a path of sin, Biglari still loves you.", "Cracker Barrel is a little more lonely without you.", "I bet you wouldn't even love me if I was a worm.", "You're univited to the BBQ.", "This is going on the quaterly report...", "We'll talk about this during your next performance review", "Clearly you don't own an airfryer.", "It's not like I wanted you as a disciple anyways! B-Baka!", "Maybe you should take some time, listen to The Cleet, sip some tea, then come back.", "I love you but please turn off ur phone or give me a call. I cannot support hate. Please stop this. I know this isn't your heart.", "I can't take it anymore. Seriously, I am at my limit.", "I hope you're having fun. I know we are without you here.", "Did Quaker Steak & Lube put you up to this???", "You're mother was a hampster.", "Peep the salary. 887 times higher than my employess. Infinitely more than you."]
blessings = ["The Stonks guy? Yeah, I know him. We had lunch last Tuesday", "In the name of the Cracker, the Barrel, and the holy Stake n Shake you are forgiven.", "I invest in you as you have invested in me. Blessed be those who believe in Biglari.", "We all have a place in the great Biglari Holdings in the sky.", "Bless you, my child.", "Western Sizzlin is the closest man can get to heaven here on Earth.", "They say on the seventh day God rested. It's true, I got lunch at Cracker Barrel.", "Bigalri Holdings aims to take humanity where it has never dare to go before. To a quality meal for a reasonable price.", "Sometimes I feel insecure. It's people like you who help change that.", "Everyone talks about Biglari Holdings but never holding Biglari's hand.", "It's called Cracker Barrel because it's full of white people.", "Be sure to make pilgrimage to the Biglari Holdings headquarters in San Antonio, Texas.", "When is someone gonna hold Biglari?", "I appreciate the sentiment, but you know just giving me money would actually go a lot further.", "Some people have suggest that I'm not the real Biglari. I assure you, I am. I hear you. I love you. - The Real Biglari", "My father was a Brigadier General for the Imperial Iranian Armed Forces. So when you think about it, I'm sorta like a Brigadier General myself and you are all my little soldiers.", "My first business was INTX.net, an Internet Service Provider. I later sold it and used the money to invest in Western Sizzlin. Sometimes I think about that decision.", "Would you still love me if I was a worm?", "Hello? Hello? Is this thing on? Can you hear me? I swear, we need a new PA system. I can never get this thing to work.", "Death comes for us all. That's why I decided to make Stake n Shake franchises in Heaven.", "None of our food is halal, sure but it can't be haram, right?"]
pics = ['Biglari_Pics\\Sardar.jpg', 'Biglari_Pics\\Sardar2.jpg', 'Biglari_pics\\Sardar3.png', 'Biglari_Pics\\Sardar4.jpg', 'Biglari_Pics\\Sardar5.jpg', 'Biglari_Pics\\Sardar6.jpg', 'Biglari_Pics\\Sardar7.jpg', 'Biglari_Pics\\Sardar8.jpg']
reactions = [":flushed:", ":pleading_face:", ":pensive: A blessing and a curse", ":kissing_cat: Thank you!", ":face_with_raised_eyebrow: Are you sure about that?", ":woozy_face: Do you really mean it?", ":point_right: :point_left: Really?"]
statuses = ["myself make 887x more than my employees ", "you sleep", "the sunset", "the stocks", "MTV's Date My Mom", "Netflix", "Biglari commands", "Steak n Shake", "people at Cracker Barrel", "Western Sizzlin employees"]
#responds with a randomized reaction, like a glorified ping command
@bot.command(name="thicc")
async def thicc(ctx):
	react = random.choice(reactions)
	await ctx.channel.send(react)
#sends a randomized photo of Biglari
@bot.command(name="onlyfans")
async def onlyfans(ctx):
	file = random.choice(pics)
	await ctx.channel.send(file=discord.File(file))
#Kicks the user and responds
@bot.command(aliases=['sucks', 'bad', 'cringe', 'smells', 'smelly', 'lame', 'stinks', 'dumb', 'poopy'])
async def kick(ctx):
	await ctx.author.kick(reason='L + Ratio + You fell off + Kicked + Biglari better + 206.127.145.77')
	await ctx.channel.send("L + Ratio + You fell off + Kicked + Biglari better + 206.127.145.77")
#Currently sends an embed detailing some stock info
@bot.command(name='holdings')
async def holdings(ctx):
	embed=discord.Embed(title="Biglari Holdings", url="http://www.biglariholdings.com/", description="The current stock listing for Biglari Holdings (BH:NYSE)", color=5793266)
	embed.set_author(name="Sardar Biglari", icon_url="https://www.qsrmagazine.com/sites/default/files/styles/story_page/public/story/who-sardar-biglari.jpg?itok=CrB0O6wQ")
	embed.set_thumbnail(url="https://g.foolcdn.com/art/companylogos/square/bh.png")
	embed.add_field(name="Index", value="New York Stock Exchange", inline=False)
	embed.add_field(name="Symbol", value="Class B: BH   Class A: BH-A", inline=False)
	embed.add_field(name="Price: Class A", value=price2, inline=False)
	embed.add_field(name="Price: Class B", value=price, inline=False)
	await ctx.send(embed=embed)
# Will give the user a disciple role or will respond (sister command of Biglari Sin)
@bot.command(name='bless')
async def bless(ctx):
	sender =  ctx.message.author
	disciple = discord.utils.find(lambda r: r.name == 'Biglari Disciple', ctx.guild.roles)
	blessing = random.choice(blessings)
	if disciple:
		pass
	else:
		await ctx.guild.create_role(name="Biglari Disciple")
	if disciple in sender.roles:
		await ctx.channel.send(blessing)
	else:
		await sender.add_roles(disciple)
		await ctx.channel.send("You have been blessed.")
@bot.command(name='sin')
async def sin(ctx):
	sender = ctx.message.author
	disciple = discord.utils.find(lambda r: r.name == 'Biglari Disciple', ctx.guild.roles)
	sinful = random.choice(sins)
	if disciple:
		pass
	else:
		await ctx.guild.create_role(name="Biglari Disciple")
	if disciple in sender.roles:
		await sender.remove_roles(disciple)
		await ctx.channel.send("It's always sad to see an investor leave us.")
	else:
		await ctx.channel.send(sinful)
#tells us the bot is online and sets a randomized activitiy
@bot.event
async def on_ready():
	print("Biglari Online.")
	status = random.choice(statuses)
	await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name = status))
#token stored in the config json
bot.run(token)