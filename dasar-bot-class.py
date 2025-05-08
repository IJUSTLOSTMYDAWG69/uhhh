# test-bot(bot class)
# This example requires the 'members' and 'message_content' privileged intents to function.
import discord
import random
import os
from discord.ext import commands
from bot_logic import gen_pass
from model import get_class
from detect_objects import detect
import torch
from torchvision import transforms
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Set up Discord bot
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
# Event: When the bot is ready
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
# command prefix 
bot = commands.Bot(command_prefix='$', description=description, intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})') # type: ignore
    print('------')

@bot.command()
async def detection(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            #file_url = attachment.url IF URL
            await attachment.save(f"./CV/{file_name}")
            await ctx.send(detect(input_image=f"./CV/{file_name}", output_image=f"./CV/{file_name}", model_path="yolov3.pt"))
            # await ctx.send(tampilkan(output_image=f"./CV/{file_name}"))
            with open(f'CV/{file_name}', 'rb') as f:
            # with open(f'meme/enemies-meme.jpg', 'rb') as f:
            # Mari simpan file perpustakaan/library Discord yang dikonversi dalam variabel ini!
                picture = discord.File(f)
            await ctx.send(file=picture)
    else:
        await ctx.send("Anda lupa mengunggah gambar :(")

# adding two numbers
@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

# adding two numbers
@bot.command()
async def subtract(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left - right)

# adding two numbers
@bot.command()
async def min(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left * right)

# adding two numbers
@bot.command()
async def div(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left / right)

    # adding two numbers
@bot.command()
async def pow(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left ** right)

# spamming word
@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)
# overwriting kalimat.txt
@bot.command()
async def tulis(ctx, *, my_string: str):
    with open('kalimat.txt', 'w', encoding='utf-8') as t:
        text = ""
        text += my_string
        t.write(text)
# append kalimat.txt
@bot.command()
async def tambahkan(ctx, *, my_string: str):
    with open('kalimat.txt', 'a', encoding='utf-8') as t:
        text = "\n"
        text += my_string
        t.write(text)
# reading kalimat.txt
@bot.command()
async def baca(ctx):
    with open('kalimat.txt', 'r', encoding='utf-8') as t:
        document = t.read()
        await ctx.send(document)

# password generator        
@bot.command()
async def pw(ctx):
    await ctx.send(f'Kata sandi yang dihasilkan: {gen_pass(10)}')

# coinflip
@bot.command()
async def coinflip(ctx):
    num = random.randint(1,2)
    if num == 1:
        await ctx.send('It is Head!')
    if num == 2:
        await ctx.send('It is Tail!')

# rolling dice
@bot.command()
async def dice(ctx):
    nums = random.randint(1,6)
    if nums == 1:
        await ctx.send('It is 1!')
    elif nums == 2:
        await ctx.send('It is 2!')
    elif nums == 3:
        await ctx.send('It is 3!')
    elif nums == 4:
        await ctx.send('It is 4!')
    elif nums == 5:
        await ctx.send('It is 5!')
    elif nums == 6:
        await ctx.send('It is 6!')

# @bot.command()
# async def mem(ctx):
#     # try by your self 2 min
#     img_name = random.choice(os.listdir('images'))
#     with open(f'images/{img_name}', 'rb') as f:
#         picture = discord.File(f)
 


# welcome message
@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}') # type: ignore
    # provide what you can help here

# random local meme image
@bot.command()
async def meme(ctx):
    # menampilkan secara random
    img_name = random.choice(os.listdir('meme'))
    with open(f'meme/{img_name}', 'rb') as f:
    # with open(f'meme/enemies-meme.jpg', 'rb') as f:
        # Mari simpan file perpustakaan/library Discord yang dikonversi dalam variabel ini!
        picture = discord.File(f)
    await ctx.send(file=picture)

# random local meme image
@bot.command()
async def lbp(ctx):
    # menampilkan secara random
    img_name = random.choice(os.listdir('A'))
    with open(f'A/{img_name}', 'rb') as f:
    # with open(f'meme/enemies-meme.jpg', 'rb') as f:
        # Mari simpan file perpustakaan/library Discord yang dikonversi dalam variabel ini!
        picture = discord.File(f)
    await ctx.send(file=picture)

#Computer Vision 
#Classification
@bot.command()
async def klasifikasi(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            #file_url = attachment.url IF URL
            await attachment.save(f"./CV/{file_name}")
            await ctx.send(get_class(model_path="keras_model.h5", labels_path="labels.txt", image_path=f"./CV/{file_name}"))
    else:
        await ctx.send("Anda lupa mengunggah gambar :(")
from model import get_class

bot.run('MTMwOTEzMjc2NTU1NTQ2MjE4NQ.Getww8.DEQqg9Xk8wx9vx6U3sCYTb3_JmQlPhrsMrjap4')
