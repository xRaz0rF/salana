import discord
from discord.ext import commands, tasks
import os
import time
import math

client = commands.Bot(command_prefix = ',')
client.remove_command('help')

#On_ready command
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('type ,help for help'))
    await client.get_channel(705223622981320706).send(time.strftime('Began running on %A, %d %B %Y, %H:%M:%S UTC', time.gmtime()))

#Load, unload, reload cog commands
@client.command()
@commands.is_owner()
async def load(ctx, extension):
    """Loads a specified extension."""
    client.load_extension(f"cogs.{extension}")
    await ctx.send("Loaded successfully.")

@client.command()
@commands.is_owner()
async def unload(ctx, extension):
    """Unloads a specified extension."""
    client.unload_extension(f"cogs.{extension}")
    await ctx.send("Unloaded successfully.")

@client.command()
@commands.is_owner()
async def reload(ctx, extension):
    """Reloads a specified extension, or all of them."""
    if str(extension) != 'all':
        try:
            client.unload_extension(f"cogs.{extension}")
            client.load_extension(f"cogs.{extension}")
            await ctx.send("Reloaded successfully.")
        except:
            try:
                client.load_extension(f'cogs.{extension}')
                await ctx.send("Reloaded successfully.")
            except:
                pass
    else:
        for filename in os.listdir("./cogs"):
            if filename.endswith(".py"):
                client.unload_extension(f"cogs.{filename[:-3]}")
                client.load_extension(f"cogs.{filename[:-3]}")
        await ctx.send("All extensions reloaded.")

#Automatically loads all cogs in ./cogs
for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")

#Error messages
@client.event
async def on_command_error(ctx, error):
    await ctx.send(f'ERROR! {error}')

@client.event
async def on_error(error):
    await client.get_channel(705223622981320706).send(error)

client.run('NzEyMDg2NjExMDk3MTU3NjUy.Xtcocw.ARQ8_3os-lNswftsp5eo4KDdPuw')