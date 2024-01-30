'''
pip install discord.py

'''


import discord
from discord.ext import commands
from discord import Button, ButtonStyle
from api import API
from key import token


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='', intents=intents)

class Params(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None
        

    @discord.ui.button(label = "Temperature Reprise", style=discord.ButtonStyle.grey)
    async def menu1(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = "La température de reprise a été sélectionnée."
        await interaction.response.send_message("Température Reprise")
        
    @discord.ui.button(label = "Temperature Consigne", style=discord.ButtonStyle.grey)
    async def menu2(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = "La température de reprise a été sélectionnée."
        await interaction.response.send_message("Température Consigne")  

    @discord.ui.button(label = "Temperature Eau Pluie", style=discord.ButtonStyle.grey)
    async def menu3(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = "La température de reprise a été sélectionnée."
        await interaction.response.send_message("Température Eau Pluie")

class Ecolabs(discord.ui.View):
    def __init__(self):
        super().__init__()
        
    @discord.ui.button(label = "ECOLAB 1", style=discord.ButtonStyle.green)
    async def menu1(self, interaction: discord.Interaction, button: discord.ui.Button):
        
        await interaction.response.send_message("ECOLAB 1")  

    @discord.ui.button(label = "ECOLAB 2", style=discord.ButtonStyle.green)
    async def menu2(self, interaction: discord.Interaction, button: discord.ui.Button):
        
        await interaction.response.send_message("ECOLAB 2")  

    @discord.ui.button(label = "ECOLAB 3", style=discord.ButtonStyle.green)
    async def menu3(self, interaction: discord.Interaction, button: discord.ui.Button):
        
        await interaction.response.send_message("ECOLAB 3")  

    @discord.ui.button(label = "ECOLAB 4", style=discord.ButtonStyle.green)
    async def menu4(self, interaction: discord.Interaction, button: discord.ui.Button):
        
        await interaction.response.send_message("ECOLAB 4")  

    @discord.ui.button(label = "ECOLAB 5", style=discord.ButtonStyle.green)
    async def menu5(self, interaction: discord.Interaction, button: discord.ui.Button):
        
        await interaction.response.send_message("ECOLAB 5")  

    @discord.ui.button(label = "ECOLAB 6", style=discord.ButtonStyle.green)
    async def menu6(self, interaction: discord.Interaction, button: discord.ui.Button):
        
        await interaction.response.send_message("ECOLAB 6")  


class Cellules(discord.ui.View):
    def __init__(self):
        super().__init__()
        
    @discord.ui.button(label = "Cellule 1", style=discord.ButtonStyle.green)
    async def menu1(self, interaction: discord.Interaction, button: discord.ui.Button):
        
        await interaction.response.send_message("Cellule 1")  

    @discord.ui.button(label = "Cellule 2", style=discord.ButtonStyle.green)
    async def menu2(self, interaction: discord.Interaction, button: discord.ui.Button):
        
        await interaction.response.send_message("Cellule 2")  

    @discord.ui.button(label = "Cellule 3", style=discord.ButtonStyle.green)
    async def menu3(self, interaction: discord.Interaction, button: discord.ui.Button):
        
        await interaction.response.send_message("Cellule 3")  

   



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
async def Bonjour(ctx):
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
   
    if numEcolab is None :
         
         while (True):

            await ctx.reply("Quel Ecolab voulez-vous voir?")
            eco = Ecolabs()
            await ctx.send(view = eco)
            ecolab  = await bot.wait_for("message",timeout=60)
            eco = ecolab.content.split(" ")
            for ecolab in eco:
                if ecolab.isdigit():
                    numEcolab = int(ecolab)
            if numEcolab < 1 or numEcolab >6 :
                await ctx.reply(f"Ecolab {numEcolab} n'existe pas. Veuillez choisir un Ecolab valide!.")

            if numEcolab >=1 and numEcolab <=6:
                break
            
    while (True):     
        await ctx.reply(f"Quel Cellue de l'Ecolab {numEcolab} voulez vous voir ?")
        cel = Cellules()
        await ctx.send(view=cel)
        cellule = await bot.wait_for("message",timeout=60)
        cell = cellule.content.split(" ")
        for cellue in cell:
            if cellue.isdigit():
                numCell = int(cellue)
        if numCell < 1 or numCell >3 :
            await ctx.reply(f"La Cellule {numCell} n'existe pas. Veuillez choisir une cellule valide!.")

        if numCell >=1 and numCell <=3:
            break 
        
    api = API.get_ecolab(numEcolab,numCell)
    while (True):
        await ctx.reply(f"Quel paramètre de la Cellule {numCell}, Ecolab {numEcolab} voulez vous consulter? ")
        param = Params()
        await ctx.send(view=param)
        parametre = await bot.wait_for("message",timeout=60 )
        temperature = parametre.content.lower()
        temperature_reprise= "température reprise"
        temperature_eau_pluie = "température eau pluie"
        temperature_consigne=  "température consigne"


        if temperature == temperature_reprise :
            temperature_reprise= "temperature_reprise"
            temperature = temperature_reprise
            break
        if temperature == temperature_consigne :
            temperature_consigne=  "temperature_consigne"
            temperature=temperature_consigne
            break
        if temperature == temperature_eau_pluie:
            temperature_eau_pluie = "temperature_eau_pluie"
            temperature = temperature_eau_pluie
            break
        else:
            await ctx.reply("Le paramètre que vous avez saisi est incorrect. Veuillez choisir le paramètre correct.")
    
    
    await ctx.reply(f"La {parametre.content} de l'Ecolab {numEcolab}, cellule {numCell} est {round(api[temperature])}.")


            



bot.run(token)
