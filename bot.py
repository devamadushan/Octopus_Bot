'''
pip install discord.py

'''
################################################################################################################################### # # #

import discord
from discord.ext import commands
from discord import Button, ButtonStyle
from api import API
from key import token

################################################################################################################################### # # #

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=''        # You can change the prefix hear !
                   , intents=intents)

################################################################################################################################### # # #

        #Button Prametre : Temperatue reprise , Temperature Consigne , Tenperature Eau PLuie .... for : def Ecolab()

class Params(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None
        
                            #Button of Temperature Reprise
    @discord.ui.button(label = "Temperature Reprise", style=discord.ButtonStyle.grey)
    async def menu1(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = "La température de reprise a été sélectionnée."
        await interaction.response.send_message("Température Reprise") #Response of the Button
        

                            #Button of Temperature Consigne
    @discord.ui.button(label = "Temperature Consigne", style=discord.ButtonStyle.grey)
    async def menu2(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = "La température de reprise a été sélectionnée."
        await interaction.response.send_message("Température Consigne")  #Response of the Button


                            #Button of Temperature Eau Pluie
    @discord.ui.button(label = "Temperature Eau Pluie", style=discord.ButtonStyle.grey)
    async def menu3(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = "La température de reprise a été sélectionnée."
        await interaction.response.send_message("Température Eau Pluie") #Response of the Button


        
        #Button Ecolab : ECOLAB 1 , ECOLAB 2 , ECOLAB 3..... for def Ecolab()

class Ecolabs(discord.ui.View):
    def __init__(self):
        super().__init__()
        

                                #Button ECOLAB 1
        
    @discord.ui.button(label = "ECOLAB 1", style=discord.ButtonStyle.green)
    async def menu1(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("ECOLAB 1") #Response of the Button


                                #Button ECOLAB 2

    @discord.ui.button(label = "ECOLAB 2", style=discord.ButtonStyle.green)
    async def menu2(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("ECOLAB 2")  #Response of the Button


                                #Button ECOLAB 3

    @discord.ui.button(label = "ECOLAB 3", style=discord.ButtonStyle.green)
    async def menu3(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("ECOLAB 3")  #Response of the Button


                                #Button ECOLAB 4

    @discord.ui.button(label = "ECOLAB 4", style=discord.ButtonStyle.green)
    async def menu4(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("ECOLAB 4")  #Response of the Button


                                #Button ECOLAB 5

    @discord.ui.button(label = "ECOLAB 5", style=discord.ButtonStyle.green)
    async def menu5(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("ECOLAB 5")  #Response of the Button


                                #Button ECOLAB 6

    @discord.ui.button(label = "ECOLAB 6", style=discord.ButtonStyle.green)
    async def menu6(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("ECOLAB 6")  #Response of the Button



        #Button Celule : Cellule 1 , Cellule 2 , Cellule 3..... for def Ecolab()

class Cellules(discord.ui.View):
    def __init__(self):
        super().__init__()
        

                                #Button Cellule 1

    @discord.ui.button(label = "Cellule 1", style=discord.ButtonStyle.green)
    async def menu1(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("Cellule 1")  #Response of the Button


                                #Button Cellule 2

    @discord.ui.button(label = "Cellule 2", style=discord.ButtonStyle.green)
    async def menu2(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("Cellule 2")  #Response of the Button


                                #Button Cellule 3

    @discord.ui.button(label = "Cellule 3", style=discord.ButtonStyle.green)
    async def menu3(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("Cellule 3")  #Response of the Button



                                                            #when the Bot Octopus is ready after launching the program
        
@bot.event
async def on_ready():
    print("Ready!!")



                                                    #Delete the specified number of messeges your want when you type ("prefix" clear)
    
@bot.command()
async def clear(ctx, nombre: int = 1):
    async for message in ctx.channel.history(limit=nombre +1):
        await message.delete()



                                                                #Delete All messeges when you type ("prefix" clearAll )
        
@bot.command()
async def clearAll(ctx):
    async for message in ctx.channel.history():
        await message.delete()



                                                                     #Say hello when you type ("prefix" Bonjour)
        
@bot.command()
async def Bonjour(ctx):
    user = ctx.author.name 
    userName = ''.join(filter(str.isalpha, user)) #Select only string
    await ctx.send(f"Bonjour {userName}")




                                                             #for kick users when you type ("prefix" kick @user reason )
    
@bot.command()
async def kick(ctx, user : discord.User , *reason):
    reason = " ".join(reason)
    await ctx.guild.kick(user, reason = reason)
    await ctx.send(f"{user} à été kick.")




                                                                 #for ban users when you type ("prefix" ban @user reason )
    
@bot.command()
async def ban(ctx, user : discord.User , *reason):
    reason = " ".join(reason)
    await ctx.guild.ban(user, reason = reason)
    await ctx.send(f"{user} à été ban pour la raison suivante : {reason}.")




                                                                #for unban users when you type ("prefix" unban @user reason )
    
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
   


                    #To interact with the Ecolab ("prefix" Ecolab) or ("prefix" Ecolab 'number of ecolab') or ("prefix" Ecolab 'num ecolab' cellule 'num cellule')

@bot.command()
async def Ecolab(ctx, numEcolab :int = None, cellule:str = None ,numCell :int = None):

                                                            # if the user says the ecolab number and cell number
    if numEcolab and numCell:
        await ctx.reply("Chargement...🔃")

                                                                    #if the user don't say the ecolab number
    if numEcolab is None :
         while (True):

            await ctx.reply("Quel Ecolab voulez-vous voir?") #bot ask for the ecolab number 
            eco = Ecolabs() #Collect the Buttons
            await ctx.send(view = eco) #send the Buttons
            ecolab  = await bot.wait_for("message",timeout=60) #Wait for the response of user
            eco = ecolab.content.split(" ")
            for ecolab in eco:
                if ecolab.isdigit():
                    numEcolab = int(ecolab) #take just the number 


                                                #Verification
            if numEcolab < 1 or numEcolab >6 :
                await ctx.reply(f"Ecolab {numEcolab} n'existe pas. Veuillez choisir un Ecolab valide!.")

            if numEcolab >=1 and numEcolab <=6:
                break

                                                                    #if the user don't say the ecolab number
    if numCell is None:         
        while (True):     

            await ctx.reply(f"Quel Cellue de l'Ecolab {numEcolab} voulez vous voir ?")
            cel = Cellules()    #Collect the Buttons of cellules
            await ctx.send(view=cel)     #send the Buttons
            cellule = await bot.wait_for("message",timeout=60)
            cell = cellule.content.split(" ")
            for cellue in cell:
                if cellue.isdigit():
                    numCell = int(cellue)    #take just the number 


                                                #Verification

            if numCell < 1 or numCell >3 :
                await ctx.reply(f"La Cellule {numCell} n'existe pas. Veuillez choisir une cellule valide!.")

            if numCell >=1 and numCell <=3:
                break 
                                                                     
    api = API.get_ecolab(numEcolab,numCell) #Get api of the ecolab and cell by ginving ecolab number and cell

    while (True):
        await ctx.reply(f"Quel paramètre de Ecolab {numEcolab} Cellule {numCell}, voulez vous consulter? ")
        param = Params()    #Collect the Buttons parameters 
        await ctx.send(view=param)  #send the Buttons
        parametre = await bot.wait_for("message",timeout=60 )
        temperature = parametre.content.lower() #Convert to Lower case the Parameter 
        temperature_reprise= "température reprise"
        temperature_eau_pluie = "température eau pluie"
        temperature_consigne=  "température consigne"

                                               
                                                #Verification

        if temperature == temperature_reprise :
            temperature_reprise= "temperature_reprise"  #Change the pattern to make requesting JSON data easier
            temperature = temperature_reprise
            break
        if temperature == temperature_consigne :
            temperature_consigne=  "temperature_consigne"   #Change the pattern to make requesting JSON data easier
            temperature=temperature_consigne
            break
        if temperature == temperature_eau_pluie:
            temperature_eau_pluie = "temperature_eau_pluie"    #Change the pattern to make requesting JSON data easier
            temperature = temperature_eau_pluie
            break
        else:
            await ctx.reply("Le paramètre que vous avez saisi est incorrect. Veuillez choisir le paramètre correct.")
    
    
                                                        #Result
            
    await ctx.reply(f"La {parametre.content} de l'Ecolab {numEcolab} cellule {numCell} est {round(api[temperature])}.")


bot.run(token)
