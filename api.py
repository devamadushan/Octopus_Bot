'''
pip install flask

'''
################################################################################################################################### # # #

import requests
import random

################################################################################################################################### # # #


#Autor : Deva


                                        ##Fake params used when the program can't query the API
ecolabs = {

             "params": {
                 "temperature_reprise": round(random.uniform(-10, 45), 0), #for get random numbers
                 "temperature_eau_pluie": round(random.uniform(-10, 45), 0),
                "temperature_consigne": 0
             }
           
        }


                                                #class Api 
class Api():
    def __init__(self):
        self.ecolab_1 = "http://10.119.10.100:8080/"
        self.ecolab_2 = "http://10.119.20.100:8080/"    #   <
        self.ecolab_3 = "http://10.119.30.100:8080/"    #<      /Attributes to query all Ecolabs
        self.ecolab_4 = "http://10.119.40.100:8080/"    #   <
        self.ecolab_5 = "http://10.119.50.100:8080/"
        self.ecolab_6 = "http://10.119.60.100:8080/"


                                            #this fuction return fack params when he can't query the 1st ecolab and return real params when he can
    def get_ecolab_1(self,cell):
        try:
            json_data = requests.get(self.ecolab_1).json()
        except Exception as e:
            print(f"Problème lors de la récupération des données : {e}")
            json_data = None

        if json_data is None:
            return ecolabs["params"]
        else:
            return json_data['ecolab_1'][cell]['params']


                                            #this fuction return fack params when he can't query the 1st ecolab and return real params when he can

    def get_ecolab_2(self,cell):
        try:
            json_data = requests.get(self.ecolab_2).json()
        except Exception as e:
            print(f"Problème lors de la récupération des données : {e}")
            json_data = None

        if json_data is None:
            return ecolabs["params"]
        else:
            return json_data['ecolab_2'][cell]['params']


                                            #this fuction return fack params when he can't query the 1st ecolab and return real params when he can

    def get_ecolab_3(self,cell):
        try:
            json_data = requests.get(self.ecolab_3).json()
        except Exception as e:
            print(f"Problème lors de la récupération des données : {e}")
            json_data = None

        if json_data is None:
            return ecolabs["params"]
        else:
            return json_data['ecolab_3'][cell]['params']
        

                                            #this fuction return fack params when he can't query the 1st ecolab and return real params when he can

    def get_ecolab_4(self,cell):
        try:
            json_data = requests.get(self.ecolab_4).json()
        except Exception as e:
            print(f"Problème lors de la récupération des données : {e}")
            json_data = None

        if json_data is None:
            print("Problème lors de la récupération des données.")
        else:
            return json_data['ecolab_4'][cell]['params']
    

                                            #this fuction return fack params when he can't query the 1st ecolab and return real params when he can

    def get_ecolab_5(self,cell):
        try:
            json_data = requests.get(self.ecolab_5).json()
        except Exception as e:
            print(f"Problème lors de la récupération des données : {e}")
            json_data = None

        if json_data is None:
            print("Problème lors de la récupération des données.")
        else:
            return json_data['ecolab_5'][cell]['params']
    

                                            #this fuction return fack params when he can't query the 1st ecolab and return real params when he can

    def get_ecolab_6(self,cell):
        try:
            json_data = requests.get(self.ecolab_6).json()
        except Exception as e:
            print(f"Problème lors de la récupération des données : {e}")
            json_data = None

        if json_data is None:
            print("Problème lors de la récupération des données.")
        else:
            return json_data['ecolab_6'][cell]['params']


                                                    #this function take the ecolab number and cell and return the fuction needs to get params

    def get_ecolab(self,numecolab,cell):
        cellule =f"Cellule_{cell}"  #Change the pattern to make requesting JSON data easier
        if numecolab == 1:
            return self.get_ecolab_1(cellule)   #return the function need to Query the Ecolab asked by user
        if numecolab == 2:
            return self.get_ecolab_2(cellule)   #return the function need to Query the Ecolab asked by user
        if numecolab == 3:
            return self.get_ecolab_3(cellule)   #return the function need to Query the Ecolab asked by user
        if numecolab == 4:
            return self.get_ecolab_4(cellule)   #return the function need to Query the Ecolab asked by user
        if numecolab == 5:
            return self.get_ecolab_5(cellule)   #return the function need to Query the Ecolab asked by user
        if numecolab == 6:
            return self.get_ecolab_6(cellule)   #return the function need to Query the Ecolab asked by user





API = Api()

    
