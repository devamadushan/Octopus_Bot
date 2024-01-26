'''
pip install discord.py

'''


import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='Octopus ', intents=intents)


@bot.event
async def on_ready():
    print("Ready!!")

@bot.command()
async def clear(ctx, nombre: int = 1):
    async for message in ctx.channel.history(limit=nombre +1):
        await message.delete()

@bot.command()
async def clearAll(ctx):
    async for message in ctx.channel.history():
        await message.delete()

@bot.command()
async def coucou(ctx):
    await ctx.send("Bonjour")

@bot.command()
async def kick(ctx, user : discord.user , *reason):
    reason = " ".join(reason)
    await ctx.guid.kick(user, reason = reason)
    await ctx.send(f"{user} à été kick.")

@bot.command()
async def ban(ctx, user : discord.user , *reason):
    reason = " ".join(reason)
    await ctx.guid.ban(user, reason = reason)
    await ctx.send(f"{user} à été ban pour la raison suivante : {reason}.")


@bot.command()
async def unban(ctx, user , *reason):
    reason = " ".join(reason)
    userName , userId = user.split("#")
    bannedUsers = await ctx.guid.bans()
    for i in bannedUsers:
        if i.user.name == userName and i.user.discriminator == userId:
            await ctx.guid.unban(i.user, reason = reason)
            await ctx.send(f"{user} à été unban.")

    await ctx.send(f"L'utilisatateur {user} n'est pas dans la list des bans.")
   




bot.run("MTIwMDQ0OTQ4MzAyNTE2NjQ0Ng.GxX85c.Dd2U7kN6iKs5WhFyqlMQ9BKg4aFb8Qua32PQ-k")
