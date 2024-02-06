'''
pip install discord.py

'''
################################################################################################################################### # # #

import discord
from discord.ext import commands
from discord import Button, ButtonStyle
from api import API
import json
import requests
import random
from key import token

################################################################################################################################### # # #


#Autor : Deva


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
    
@bot.command(name="Clear",aliases=["supprime","efface","Efface","Supprimer","delete", "Delete","clear",""], help ="Efface le nombre de messages souhaité... EXEMPLE: (supprime 3)")
async def clear(ctx, nombre: int = 1):
    async for message in ctx.channel.history(limit=nombre +1):
        await message.delete()



                                                                #Delete All messeges when you type ("prefix" clearAll )
        
@bot.command(name="clearAll", aliases=["effaceTout", "supprimeTout", "deleteAll", "DeleteAll", "ClearAll","effaceTT"], help="Efface touts les messages... EXEMPLE: (effaceTout)")
async def clearAll(ctx):
    async for message in ctx.channel.history():
        await message.delete()



                                                                     #Say hello when you type ("prefix" Bonjour)
        
@bot.command(name="bonjour",aliases=["hello", "salut","Salut","Bonjour","Hello","wshh"],help="Bonjour")
async def Bonjour(ctx):
    user = ctx.author.name 
    userName = ''.join(filter(str.isalpha, user)) #Select only string
    await ctx.send(f"Bonjour {userName}")




                                                             #for kick users when you type ("prefix" kick @user reason )
    
@bot.command(name="kick", aliases=["Kick","eject","Eject" ], helps="Éjecte un utilisateur souhaités... EXEMPLE : (eject @utilisateur).")
async def kick(ctx, user : discord.User , *reason):
    reason = " ".join(reason)
    await ctx.guild.kick(user, reason = reason)
    await ctx.send(f"{user} à été kick.")




                                                                 #for ban users when you type ("prefix" ban @user reason )
    
@bot.command(name="ban",aliases=["Ban", "Bannir", "bannir"] ,help="Bannir un utilisateur souhaité... EXEMPLE : (ban @utilisateur pour violation des règles du serveur")
async def ban(ctx, user : discord.User , *reason):
    reason = " ".join(reason)
    await ctx.guild.ban(user, reason = reason)
    await ctx.send(f"{user} à été ban pour la raison suivante : {reason}.")




                                                                #for unban users when you type ("prefix" unban @user reason )
    
@bot.command(name="unban", aliases=["Unban","débannir","debannir", "Débannir"] , help="Débanir un utiliseur... EXEMPLE: (unban @user c'est une erreur)")
async def unban(ctx, user , *reason):
    reason = " ".join(reason)
    userNameID = user.split("#")
    userName = userNameID[0]
    userId = userNameID[1]
    
    bannedUsers = ctx.guild.bans()
    
    async for i in bannedUsers:
        if i.user.name == userName and i.user.discriminator == userId:
            await ctx.guild.unban(i.user, reason = reason)
            await ctx.send(f"{user} à été unban.")
        else:
            await ctx.send(f"L'utilisatateur {user} n'est pas dans la list des bans.")
   


                    #To interact with the Ecolab ("prefix" Ecolab) or ("prefix" Ecolab 'number of ecolab') or ("prefix" Ecolab 'num ecolab' cellule 'num cellule')

@bot.command(name ="ecolab", aliases=["Ecolab", "ECOLAB",], help="Voir les Températures d'une Celule souhaité... EXEMPLE: (Ecolab),(ECOlAB 2),(ECOLAB 2 cellule 3) ")
async def Ecolab(ctx, numEcolab :int = None, cellule:str = None ,numCell :int = None):

                                                            # if the user says the ecolab number and cell number
    if numEcolab and numCell:
        await ctx.reply("Chargement...🔃")
        int(numEcolab)
        int(numCell)
        while(True):
                                                #Verification
            if numEcolab < 1 or numEcolab >6 :
                await ctx.reply(f"Ecolab {numEcolab} n'existe pas. Veuillez choisir un Ecolab valide!.")
                numEcolab = None
            if numEcolab >=1 and numEcolab <=6:
                if numCell < 1 or numCell >3 :
                    await ctx.reply(f"La Cellule {numCell} n'existe pas. Veuillez choisir une cellule valide!.")
                    numCell = None
                if numCell >=1 and numCell <=3: 
                    break 

    if numEcolab:
        while(True):

            if numEcolab < 1 or numEcolab >6 :
                await ctx.reply(f"Ecolab {numEcolab} n'existe pas. Veuillez choisir un Ecolab valide!.")
                await ctx.reply("Quel Ecolab voulez-vous voir?") #bot ask for the ecolab number 
                eco = Ecolabs() #Collect the Buttons
                await ctx.send(view = eco) #send the Buttons
                ecolab  = await bot.wait_for("message",timeout=60) #Wait for the response of user
                eco = ecolab.content.split(" ")
                for ecolab in eco:
                    if ecolab.isdigit():
                        numEcolab = int(ecolab) #take just the number 

            if numEcolab >=1 and numEcolab <=6:
                break


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
                await ctx.reply("Chargement...🔃")   
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






#Autor : Luca
with open('Liens.json','r') as file:
    liens = json.load(file)

data = "temperature_reprise \n  temperature_consigne \n temperature_eau_pluie"

# Commande ecolab
@bot.command(name='help_ecolabs', help='Commandes pour les ecolabs')
async def ecolabs(ctx):
    help_text = "Commandes liées aux ecolabs :\n"
    for command in bot.commands:
        if command.name.startswith("ecolab"):
            help_text+= f"{command.name} : {command.help} \n"
    await ctx.send(help_text)


# ECOLAB 2
api_lien = "http://10.119.20.100:8080/"
json2 = requests.get(api_lien).json()
forma2 = json.dumps(json2, indent=4)

@bot.command(name='ecolab2', help="Info global de l'ecolab 2")
async def param(ctx):
    await ctx.send(forma2)


# ECOLAB 4
api_lien = "http://10.119.40.100:8080/"
json4 = requests.get(api_lien).json()
forma4 = json.dumps(json4, indent=4)

@bot.command(name='ecolab4', help="Info global de l'ecolab 2")
async def param(ctx):
    await ctx.send(forma4)




# Aide partie Web
@bot.command(name='help_web', help='Info sur la partie web')
async def lien(ctx):
    help_text = "Commandes liées au web :\n"
    for command in bot.commands:
        if command.name.startswith("web"):
            help_text += f"{command.name} : {command.help} \n"
    await ctx.send(help_text)


# Flexbox commun
@bot.command(name="web_urlFlexbox", help="Liens pages web Flexbox")
async def urlWebFlexbox(ctx):
    await ctx.send(
        "Liens communs en flexbox : \n"
        "Accueil : " + liens['liens communs']['flexbox']['accueil'] + "\n"
        "Inscription : " + liens['liens communs']['flexbox']['inscription'] + "\n"
        "Connexion : " + liens['liens communs']['flexbox']['connexion'] + "\n"
    )

# Flexbox ADMIN
@bot.command(name="web_adminFlexbox", help="Liens vers pages web Flexbox Admin")
async def urlWebAdminFlexbox(ctx):
    await ctx.send(
        "IMPORTANT : " + liens['liens communs admin']['information'] + "\n" + "\n"
        "Liens admin en flexbox : \n"
        "Accueil : " + liens['liens communs admin']['flexbox']['accueil'] + "\n"
        "Inscription : " + liens['liens communs admin']['flexbox']['inscription'] + "\n"
        "Connexion : " + liens['liens communs admin']['flexbox']['connexion'] + "\n"
        "Experiences : " + liens['liens communs admin']['flexbox']['experience'] + "\n"
        "Edit experience : " + liens['liens communs admin']['flexbox']['edit experience'] + "\n"
        "Add experience : " + liens['liens communs admin']['flexbox']['add experience'] + "\n"
        "Utilisateurs : " + liens['liens communs admin']['flexbox']['utilisateurs'] + "\n"
        "Edit role utilisateur : " + liens['liens communs admin']['flexbox']['edit role'] + "\n"
        "Détails : " + liens['liens communs admin']['flexbox']['detail'] + "\n"
    )


# ResponsiveIMG commun
@bot.command(name="web_urlResponsive", help="Liens vers pages web ResponsiveIMG")
async def urlWebResponsiveImg(ctx):
    await ctx.send(
        "Liens communs en ResponsiveIMG : \n"
        "Accueil : " + liens['liens communs']['ResponsiveImg']['accueil'] + "\n"
        "Inscription : " + liens['liens communs']['ResponsiveImg']['inscription'] + "\n"
        "Connexion : " + liens['liens communs']['ResponsiveImg']['connexion'] + "\n"
        "Détail : " + liens['liens communs']['ResponsiveImg']['detail'] + "\n"
    )

# ResponsiveIMG ADMIN
@bot.command(name="web_adminResponsive", help="Liens vers pages web ResponsiveImg Admin")
async def urlWebAdminResponsiveImg(ctx):
    await ctx.send(
        "IMPORTANT : " + liens['liens communs admin']['information'] + "\n" + "\n"
        "Liens admin en ResponsiveIMG : \n"
        "Accueil : " + liens['liens communs admin']['ResponsiveImg']['accueil'] + "\n"
        "Inscription : " + liens['liens communs admin']['ResponsiveImg']['inscription'] + "\n"
        "Connexion : " + liens['liens communs admin']['ResponsiveImg']['connexion'] + "\n"
        "Experiences : " + liens['liens communs admin']['ResponsiveImg']['experience'] + "\n"
        "Edit experience : " + liens['liens communs admin']['ResponsiveImg']['edit experience'] + "\n"
        "Add experience : " + liens['liens communs admin']['ResponsiveImg']['add experience'] + "\n"
        "Utilisateurs : " + liens['liens communs admin']['ResponsiveImg']['utilisateurs'] + "\n"
        "Edit role utilisateur : " + liens['liens communs admin']['ResponsiveImg']['edit role'] + "\n"
        "Détails : " + liens['liens communs admin']['ResponsiveImg']['detail'] + "\n"
    )

# CNRS
@bot.command(name="web_CNRS", help="Sites concernant le CNRS")
async def urlCNRS(ctx):
    await ctx.send(
        "CNRS : " + liens["CNRS"]["CNRS"] + "\n"
        "Facebook : " + liens['CNRS']['Facebook'] + "\n"
        "Twitter : " + liens['CNRS']['Twitter'] + "\n"
        "Instagram : " + liens['CNRS']['Instagram'] + "\n"
        "Youtube : " + liens['CNRS']['Youtube'] + "\n"
    )

# Suppression des messages
@bot.command(name="supprimer", help="Supprimer plusieurs messages")
async def suppr_mess(ctx, nb_mess:int=None):
    if nb_mess is None:
        await ctx.send("Combien de messages voulez-vous supprimer ?")
        message = await bot.wait_for("message",timeout=60)
        mess = message.content.split(" ")
        for i in mess:
            if i.isdigit():
                nb_mess = int(i)
        await ctx.channel.purge(limit=nb_mess + 1)
        await ctx.send(f"{nb_mess} messages ont été supprimés")

# Suppression d'un message
@bot.command(name="suppr", help="Supprimer 1 message")
async def supprimer(ctx):
    await ctx.channel.purge(limit = 2)
    await ctx.send("Le message précédent à été supprimé")



# Event Message
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    # discussion avec le bot
    if any(keyword in message.content.lower() for keyword in ["qui je suis", "qui suis je", 
    "comment je m'appelle", "quel est mon nom d'utilisateur",
    "donne-moi mon nom","donne-moi mon nom"]):
        user = message.author.name
        reponse = [f"Vous êtes {user}",f"Votre nom est {user}"]
        choix = random.randint(0,1)
        await message.channel.send(reponse[choix])

    # Comment va le bot
    if any(key in message.content.lower() for key in ["comment tu vas ", "comment ca va ",
    "comment allez-vous ","comment te sens-tu ","quel est ton état actuel ","comment se déroule ta journée ",
    "tout va bien pour toi ","comment te portes-tu","comment ça se passe pour toi"]):
        user = message.author.name
        await message.channel.send(f"{user}, en tant que programme informatique, je n'ai pas de sentiments ni d'état physique. ")

    # Ton créateur
    if any (key in message.content.lower() for key in ["qui t'as codé ","qui est derrière tondéveloppement ?",
    "qui à conçu tes algorithmes ","qui à écrit ton code","qui t'as créé "]):
        await message.channel.send("Luca et Deva sont les personnes qui m'ont programmé")

    # Date de création
    if any (key in message.content.lower() for key in["quand tu à été codé","quand as-tu été créé","quelle est ta date de naissance en tant que programme",
    "à quel moment as-tu été développé","quand as-tu été mis en service","quelle est la date de création de ton premier code",
    "à quel moment es-tu apparu"]):
        await message.channel.send("En janvier 2024")

    # Langage de programmation
    if any (key in message.content.lower() for key in ["quel langage de programmation a été utilisé pour te créer","comment es-tu conçu",
    "dans quel langage de programmation tu as été codé"]):
        await message.channel.send("Je suis créé en utilisant le langage de programmation Python")

    # Remerciement
    if any(key in message.content.lower() for key in ["merci","parfait","voilà","voila",
    "merci pour ton aide","merci beaucoup","c'est super, merci","je te suis reconnaissant"]):
        choix = random.randint(0,5)
        reponse = ["De rien ! Comment puis-je t'aider davantage ?","Je suis là pour ça !","N'hésite pas si tu as d'autres questions.",
                "C'était un plaisir de t'aider !","Pas de problème, c'est ce pour quoi je suis ici.","Toujours là pour toi !"]
        await message.channel.send(reponse[choix])

    # info sur le serveur
    if any(key in message.content.lower() for key in ["infos sur le serveur", "info sur le serveur",
    "informations sur le serveur", "information sur le serveur",
    "info du serv", "infos du serv"]):
        await message.channel.send("Pour connaitre des informations sur le serveur, veuillez entrer ' toi aide_serveur'.")

    # info sur les ecolabs
    if any(key in message.content.lower() for key in ["info sur l'ecolab", "info sur un ecolab",
    "info sur une cellule", "information sur une cellule", "information sur un ecolab"]):
        await message.channel.send("Pour connaitre des informations sur les ecolabs, veuillez entrer ' toi help_ecolabs'.")

    # info sur les pages web
    if any(key in message.content.lower() for key in ["lien du site", "liens du site",
    "url du site", "page web", "liens web", "lien web", "site web", "template", "templates"]):
        await message.channel.send("Pour connaitre les informations sur les pages webs, veuillez entrer ' toi help_web'.")

    



    await bot.process_commands(message)








@bot.event
async def on_ready():
    print(f'Bot connecter en tant que {bot.user.name}')


@bot.command(name='slt', help="Salutation")
async def hello(ctx):
    author = ctx.author.name
    await ctx.send(f"Bonjour {author}, comment puis-je vous aider aujourd'hui ?")


@bot.command(name='calcul', help='Caculer 2 valeurs')
async def calcul(ctx, a: int = None, b: int = None, operation: str = None):
    await ctx.send("Entre la valeur de A")
    a = await bot.wait_for("message", timeout=60)
    leA = a.content.split(" ")
    for l in leA:
        if l.isdigit():
            a = l

    await ctx.send("Entre la valeur de B")
    b = await bot.wait_for("message", timeout=60)
    leB = b.content.split(" ")
    for l in leB:
        if l .isdigit():
            b = l

    await ctx.send("Quelle opértion voulez-vous faire ?")
    operation = await bot.wait_for("message", timeout=60)
    ope = operation.content.split(" ")
    for l in ope:
        if l.isalpha():
            operation = l

    a = int(a)
    b = int(b)
    operation = str(operation).lower()

    result = 0
    if operation == "addition":
        result = a + b
        await ctx.send(f"Le resultat est {result}")

    elif operation == "soustraction":
        result = a - b
        await ctx.send(f"Le resultat est {result}")

    elif operation == "multiplication":
        result = a * b
        await ctx.send(f"Le resultat est {result}")

    elif operation == "division":
        result = a / b
        await ctx.send(f"Le resultat est {result}")

    else :
        await ctx.send("Je n'ai pas compris. Veuillez saisir : ' toi calcul ' et refaire votre calcul !") 





# Serveur
    
@bot.command(name='aide_serveur', help='Commandes pour le serveur')
async def help_serveur(ctx):
    help_text = "Commandes liées au serveur :\n"
    for command in bot.commands:
        if command.name.startswith('serveur_'):
            help_text += f"{command.name} : {command.help}\n"
        
    await ctx.send(help_text)


@bot.command(name='serveur_name', help='Nom du serveur')
async def servName(ctx):
    server = ctx.guild.name
    await ctx.send(f"Le nom du serveur est{server}")

@bot.command(name='serveur_proprio', help='Nom du propriétaire')
async def servProprio(ctx):
    server = ctx.guild.owner
    await ctx.send(f"Le propriétaire du serveur est {server}")

bot.run(token)
