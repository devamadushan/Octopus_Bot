'''
pip install discord.py

'''


import discord
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='Octopus ', intents=intents)


def param():
    api_lien = "http://10.119.20.100:8080/"
    json_data = requests.get(api_lien).json()   

@bot.event
async def on_ready():
    print("Ready!!")

@bot.event
async def on_member_join(member):
    channel = member.channel
    await channel.send(f'Welcome {member}')


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
    user = ctx.author.name
    user_without_last_4 = user[:-4]
    await ctx.send(f"Bonjour {user_without_last_4}")

@bot.command()
async def kick(ctx, user : discord.User , *reason):
    reason = " ".join(reason)
    await ctx.guild.kick(user, reason = reason)
    await ctx.send(f"{user} à été kick.")

@bot.command()
async def ban(ctx, user : discord.User , *reason):
    reason = " ".join(reason)
    await ctx.guild.ban(user, reason = reason)
    await ctx.send(f"{user} à été ban pour la raison suivante : {reason}.")


@bot.command()
async def unban(ctx, user , *reason):
    reason = " ".join(reason)
    userName , userId = user.split("#")
    bannedUsers = await ctx.guild.bans()
    for i in bannedUsers:
        if i.user.name == userName and i.user.discriminator == userId:
            await ctx.guild.unban(i.user, reason = reason)
            await ctx.send(f"{user} à été unban.")

    await ctx.send(f"L'utilisatateur {user} n'est pas dans la list des bans.")
   
@bot.command()
async def Ecolab(ctx, numEcolab :int = None, cellule:str = None ,numCell :int = None):
    if numEcolab is None:
         await ctx.send("quel Ecolab voulez vous voir?")
         ecolab  = await bot.wait_for("message",timeout=60)
         eco = ecolab.content.split(" ")
         for ecolab in eco:
             if ecolab.isdigit():
                numEcolab = ecolab

         
    await ctx.send("quel cellue voulez vous voir?")
    cellule = await bot.wait_for("message",timeout=60)
    cell = cellule.content.split(" ")
    for cellue in cell:
        if cellue.isdigit():
            numCell = cellue     
    await ctx.send("Quel parametre de la cellule voulez vous consulter? ")
    parametre = await bot.wait_for("message",timeout=60 )
    await ctx.send(f"La {parametre.content} de l'Ecolab {numEcolab}, cellule {numCell} est 20.")



