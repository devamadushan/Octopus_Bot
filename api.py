from flask import Flask, render_template, request, jsonify, url_for
import requests
import random



ecolabs = {

             "params": {
                 "temperature_reprise": round(random.uniform(-10, 45), 0),
                 "temperature_eau_pluie": round(random.uniform(-10, 45), 0),
                "temperature_consigne": 0
             }
           
        }

# country = input("lr nom de la vile :")


# try:
#
#     print(json)
#     print(json['name']['official'])
# except Exception as e:
#     print(f"Une erreur s'est produite : {e}")

class Api():
    def __init__(self):
        self.ecolab_1 = "http://10.119.10.100:8080/"
        self.ecolab_2 = "http://10.119.20.100:8080/"
        self.ecolab_3 = "http://10.119.30.100:8080/"
        self.ecolab_4 = "http://10.119.40.100:8080/"
        self.ecolab_5 = "http://10.119.50.100:8080/"
        self.ecolab_6 = "http://10.119.60.100:8080/"

    def get_ecolab_1(self,cell):
        try:
            json_data = requests.get(self.ecolab_1).json()
            # Faire quelque chose avec json_data
        except Exception as e:
            print(f"Problème lors de la récupération des données : {e}")
            json_data = None

        if json_data is None:
            return ecolabs["params"]
        else:
            return json_data['ecolab_1'][cell]['params']

    def get_ecolab_2(self,cell):
        try:
            json_data = requests.get(self.ecolab_2).json()
            # Faire quelque chose avec json_data
        except Exception as e:
            print(f"Problème lors de la récupération des données : {e}")
            json_data = None

        if json_data is None:
            return ecolabs["params"]
        else:
            return json_data['ecolab_2'][cell]['params']

    def get_ecolab_3(self,cell):
        try:
            json_data = requests.get(self.ecolab_3).json()
            # Faire quelque chose avec json_data
        except Exception as e:
            print(f"Problème lors de la récupération des données : {e}")
            json_data = None

        if json_data is None:
            return ecolabs["params"]
        else:
            return json_data['ecolab_3'][cell]['params']
        
    def get_ecolab_4(self,cell):
        try:
            json_data = requests.get(self.ecolab_4).json()
            # Faire quelque chose avec json_data
        except Exception as e:
            print(f"Problème lors de la récupération des données : {e}")
            json_data = None

        if json_data is None:
            print("Problème lors de la récupération des données.")
        else:
            return json_data['ecolab_4'][cell]['params']
    
    def get_ecolab_5(self,cell):
        try:
            json_data = requests.get(self.ecolab_5).json()
            # Faire quelque chose avec json_data
        except Exception as e:
            print(f"Problème lors de la récupération des données : {e}")
            json_data = None

        if json_data is None:
            print("Problème lors de la récupération des données.")
        else:
            return json_data['ecolab_5'][cell]['params']
    
    def get_ecolab_6(self,cell):
        try:
            json_data = requests.get(self.ecolab_6).json()
            # Faire quelque chose avec json_data
        except Exception as e:
            print(f"Problème lors de la récupération des données : {e}")
            json_data = None

        if json_data is None:
            print("Problème lors de la récupération des données.")
        else:
            return json_data['ecolab_6'][cell]['params']

    def get_ecolab(self,numecolab,cell):
        cellule =f"Cellule_{cell}"
        if numecolab == 1:
            return self.get_ecolab_1(cellule) 
        if numecolab == 2:
            return self.get_ecolab_2(cellule) 
        if numecolab == 3:
            return self.get_ecolab_3(cellule) 
        if numecolab == 4:
            return self.get_ecolab_4(cellule) 
        if numecolab == 5:
            return self.get_ecolab_5(cellule) 
        if numecolab == 6:
            return self.get_ecolab_6(cellule) 


API = Api()
# test = API.get_ecolab(2,"2")
# print(round(test["temperature_reprise"]))
    





# @app.route('/pays')
# def pays():
#     api_lien = "https://restcountries.com/v3.1/all"
#     json_data = requests.get(api_lien).json()
#     return render_template('lesPays.html', info=json_data)


# @app.route('/rechercher', methods=['POST'])
# def rechercher():
#     recherche = request.form['recherchePays']
#     api_lien = f"https://restcountries.com/v3.1/name/{recherche}"
#     json_data = requests.get(api_lien).json()
#     print(json_data)
#     return render_template('rechercheParPays.html', info=json_data)

# @app.route('/rechercher/<nom>')
# def rechercherpays(nom):

#     api_lien = f"https://restcountries.com/v3.1/name/{nom}"
#     json_data = requests.get(api_lien).json()
#     print(nom)
#     print(json_data)
#     return render_template('rechercheParPays.html', info=json_data)
   