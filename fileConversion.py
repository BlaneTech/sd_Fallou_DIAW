import csv
import json
import xmltodict
import yaml
from convertFunctions import *
import pathlib

outputmsg = "Opération reussie, fichier créée dans le répertoire courant\n\n"
while True:
    fileName = input("Charger le fichier à convertir (avec le chemin): ")
    path = pathlib.Path(fileName)
    if path.suffixes[-1] in ['.XML ','.xml']:
        with open(fileName,'r') as xmlObject:
            my_xml_dict = xmltodict.parse(xmlObject.read())
            print("""Sélectionner un format pour la conversion
                    1.yaml
                    2.csv
                    3.json""")
            numFormat = int(input("entrer votre sélection: "))
            if numFormat == 1:
                convertToYaml(my_xml_dict)
                print(outputmsg)
            elif numFormat == 2:
                pass
                #print(outputmsg)
             #   convertToCsv(my_xml_dict)
            elif numFormat == 3:
                convertToJson(my_xml_dict)
                print(outputmsg)
            else:
                print("Oups!, choix non valide")
    elif path.suffixes[-1] in ['.YAML ','.yaml']:
        with open(fileName, 'r') as yamlObject:
            my_yaml_dict = yaml.safe_load(yamlObject)
            print("""Sélectionner un format pour la conversion
                    1.xml
                    2.csv
                    3.json""")
            numFormat = int(input("Entrer votre sélection: "))
            if numFormat == 1:
                convertToXml(my_yaml_dict)
                print(outputmsg)
            elif numFormat == 2:
                pass
                #convertToCsv(my_yaml_dict)
            elif numFormat == 3:
                convertToJson(my_yaml_dict)
                print(outputmsg)
            else:
                print("Oups!, choix invalide")
    elif path.suffixes[-1] in ['.CSV','.csv']:
        with open(fileName, 'r') as csvObject:
            file = csv.DictReader(csvObject, delimiter=',')
            file_dict = dict()
            dict_list = list()
            liste = list()
            for key in file:
                file_dict.update(key)
                dict_list.append(key)
            print("""Sélectionner un format pour la conversion
                    1.xml
                    2.yaml
                    3.json""")
            numFormat = int(input("Entrer votre sélection: "))
            if numFormat == 1:
                convertToXml(dict_list)
                print(outputmsg)
            elif numFormat == 2:
                convertToYaml(dict_list)
                print(outputmsg)
            elif numFormat == 3:
                convertToJson(dict_list)
                print(outputmsg)
            else:
                print("Oups!, choix invalide")
    elif path.suffixes[-1] in ['.JSON','.json']:
        with open(fileName) as jsonObject:
            my_json_dict = json.load(jsonObject)
            print("""Sélectionner un format pour la conversion
                    1.xml
                    2.csv
                    3.yaml""")
            numFormat = int(input("Entrer votre sélection: "))
            if numFormat == 1:
                convertToXml(my_json_dict)
                print(outputmsg)
            elif numFormat == 2:
                pass
                #convertToCsv(my_yaml_dict)
            elif numFormat == 3:
                convertToYaml(my_json_dict)
                print(outputmsg)
            else:
                print("Oups!, choix invalide")
    else:
        print("Désolé, format non pris en charge")
