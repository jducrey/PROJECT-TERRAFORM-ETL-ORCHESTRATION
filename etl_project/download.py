# Source : data.gouv.fr
# Description : Ce jeu de données contient les concentrations modélisées 
# en microgrammes par mètre cube de moyenne journalière annuelle pour trois 
# polluants aériens (NO₂, PM10 et PM2.5) aux abords des crèches et établissements 
# scolaires d'Île-de-France pour les années de 2012 à 2017.
# https://static.data.gouv.fr/resources/base-de-donnees-de-la-pollution-aerienne-aux-abords-des-ecoles-et-creches-dile-de-france/20190329-113552/ecoles-creches-idf.csv

import requests

url = "https://static.data.gouv.fr/resources/base-de-donnees-de-la-pollution-aerienne-aux-abords-des-ecoles-et-creches-dile-de-france/20190329-113552/ecoles-creches-idf.csv"
output_file = "ecoles_creches_idf.csv"

response = requests.get(url)
if response.status_code == 200:
    with open(output_file, 'wb') as f:
        f.write(response.content)
    print(f"Fichier téléchargé avec succès : {output_file}")
else:
    print(f"Échec du téléchargement. Statut : {response.status_code}")