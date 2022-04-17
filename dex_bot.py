import discord 
from  discord.ext import commands 
import os 
import requests 
import json
from dotenv import load_dotenv
import random
# from replit import db
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client=commands.Bot(command_prefix="!")

@client.event

async def on_ready():
    print("You have logged in as @{0.user}".format(client))


@client.command()
async def hello(ctx):
    await ctx.send("hi")

sad_words=["sad","depressed","unhappy","die"]

start_encouragements=[
    "Cheer up",
    "hang in there",
    "you r great person / bot!"
]




def get_quote():
    response=requests.get("https://zenquotes.io/api/random")
    json_data=json.loads(response.text)
    quote=json_data[0]['q'] + " -" + json_data[0]['a']
    return(quote)



@client.command()

async def on_message(message):
    mention = message.author.mention
    if message.author==client.user:
        return
    # if message.content("inspire"):
    #     quote=get_quote()
    #     await message.send(quote)
    if any(word in message.content for word in sad_words):
        await message.send(random.choice(start_encouragements))

@client.command()

async def inspire(ctx):
    quote=get_quote()
    await ctx.send(quote)
async def inspire(ctx):
    quote=get_quote()
    await ctx.send(quote) #this is not confirm


client.run(TOKEN)
