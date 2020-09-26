import os
import random
import discord
from dotenv import load_dotenv
import requests
import json
import re
import sys
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()


@client.event
async def on_message(message):
    print(message)
    channel = client.get_channel(message.channel.id)
    if message.author == client.user:
        return

    if "what can you do" in message.content.lower():
        msg = 'For now only 4-5 tasks {0.author.mention}'.format(message)
        await channel.send(f'{msg}')
    elif "yoo" in message.content.lower():
        await channel.send('wassup man')
    elif "stfu bot" in message.content.lower():
        await channel.send('ok')
        sys.exit()
    elif "fuck" in message.content.lower() or "tf" in message.content.lower() or "cringe" in message.content.lower() or "eww" in message.content.lower():
        with open('bleach.txt') as b:
            a = b.readlines()
            msg=random.choice(a)
            result = re.search(r"\[([A-Za-z0-9_]+)\]", str(msg))
            print(result)
            await channel.send(f"{msg}")
    elif "hi bot" in message.content.lower():
        await channel.send('Hey man {0.author.mention}'.format(message))
    elif "introduce yourself" in message.content:
        msg = "Hello @everyone I am 42ip's bot"
        await channel.send(f'{msg}')
    elif "twss" in message.content:
        i = random.randint(0, 1)
        await channel.send(file=discord.File(f'assets/twss{i}.gif'))
    elif "noice" in message.content:
        await channel.send(file=discord.File('assets/tenor.gif'))
    elif "i love democracy" in message.content:
        await channel.send(file=discord.File('assets/democracy.gif'))
    elif "can you reply to yourself" in message.content:
        msg = 'yes i can'
        await channel.send(f'{msg}')
    elif "yes i can" in message.content:
        msg = "oh can you reply to yourself"
        await channel.send(f'{msg}')
    elif "toyst" in message.content.lower():
        msg = "https://media1.tenor.com/images/2fb6b048517ffc9492dfea5766d3835d/tenor.gif"
        await channel.send(f'{msg}')
    elif "am i ugly" in message.content.lower():
        replies = ["It runs in your fam bitch",
                   "Nah man you beautiful", "Yes.", "What if I told no"]
        n = random.randint(0, len(replies)-1)
        await channel.send(f'{replies[n]}')
    elif "tell me a joke" in message.content.lower():
        n = random.randint(0, 2)
        if n == 2:
            response = requests.get(
                "https://official-joke-api.appspot.com/random_joke")
            joke = response.json()
            await channel.send('Here\'s a joke for you')
            # await channel.send(f'{joke}')
            await channel.send(f'{str(joke["setup"])}')
            await channel.send(f'{str(joke["punchline"])}')
        elif n == 1:
            await channel.send('Your life')
        else:
            await channel.send('Sorry I cant open your front camera yet')
    elif "r! meme" in message.content.lower():
        subreds = ["memes","dankmemes","programmerhumor","boneappletea","funny","holup","linuxmemes","linuxmasterrace"]
        n = subreds[random.randint(0,len(subreds)-1)]
        response = requests.get(f"https://meme-api.herokuapp.com/gimme/{n}")
        meme = response.json()
        print(meme)
        await channel.send(f'**{str(meme["title"])}** from *{str(meme["subreddit"])}*')
        await channel.send(f'{str(meme["url"])}')


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
