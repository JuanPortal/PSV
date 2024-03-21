from discord.ext import commands
import discord
import os
import random

client = commands.Bot(command_prefix="$", intents=discord.Intents.all())
client.remove_command("help")


@client.event
async def on_ready():
    print("PSV's ready to go!")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$'):
        await client.process_commands(message)


@client.command(pass_context=True)
async def psv(ctx):
    posts = os.listdir("posts")

    random_image = random.choice(posts)

    image_path = os.path.join("posts", random_image)

    with open(image_path, "rb") as file:
        picture = discord.File(file)
        await ctx.channel.send(file=picture)

@client.command(pass_context=True)
async def pruebita(ctx):
        await ctx.channel.send('$test')


@client.command(pass_context=True)
async def help(ctx):
    em = discord.Embed(
        title="Help",
        description=
        "***$psv*** envía un post"
    )
    await ctx.send(embed=em)


client.run(os.environ["TOKEN"])
