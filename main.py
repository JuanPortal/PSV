from discord.ext import commands
import discord
import os

client = commands.Bot(command_prefix="$", intents=discord.Intents.all())

client.remove_command("help")


@client.event
async def on_ready():
    print("PSV's ready to go!")


@client.command(pass_context=True)
async def psv(ctx):
    await ctx.channel.send('Quién para un beso bien sexual?') 


@client.command(pass_context=True)
async def help(ctx):
    em = discord.Embed(
        title="Help",
        description=
        "mm:ss or just type the minutes\n\n***$cd*** starts the countdown\n\n***$stop*** stops the countdown"
    )
    await ctx.send(embed=em)


# my_secret = os.environ['bot_token']

# client.run(my_secret)
client.run(os.environ["TOKEN"])