from flask import Flask, render_template, request, jsonify, url_for
import requests


ecolabs = {

        "ecolab_2": {
            'Cellule_1': {
                "name": "E2C1",
                "fins": {
                    "ip": "192.168.0.21",
                    "port": 9600,
                    "dst_net_addr": 2,
                    "dst_node_num": 2,
                    "dst_unit_addr": 0
                },
                "params": {
                    "temperature_reprise": 10,
                    "temperature_eau_pluie": 15,
                    "temperature_consigne": 0
                }
            },
            'Cellule_2':{
                    "name": "E2C2",
                    "fins": {
                        "ip": "192.168.0.2",
                        "port": 9600,
                        "dst_net_addr": 1,
                        "dst_node_num": 1,
                        "dst_unit_addr": 0
                    },
                    "params": {
                        "temperature_reprise": 11,
                        "temperature_eau_pluie": 16,
                        "temperature_consigne": 0
                    }
            },
            'Cellule_3':{
                    "name": "E2C3",
                    "fins": {
                        "ip": "192.168.0.3",
                        "port": 9600,
                        "dst_net_addr": 1,
                        "dst_node_num": 1,
                        "dst_unit_addr": 0
                    },
                    "params": {
                        "temperature_reprise": 12,
                        "temperature_eau_pluie": 17,
                        "temperature_consigne": 0
                    }
            }
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

    def get_ecolab_1(self):
        try:
            json_data = requests.get(self.ecolab_1).json()
            # Faire quelque chose avec json_data
        except Exception as e:
            print(f"Problème lors de la récupération des données : {e}")
            json_data = None

        if json_data is None:
            print("Problème lors de la récupération des données.")
        else:
            print("Données récupérées avec succès.")
        
    
    
    

api = Api()
test = api.get_ecolab_1()
   
    





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
   