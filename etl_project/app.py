import streamlit as st
import pandas as pd
import plotly.express as px

# Chargement des données nettoyées
df = pd.read_csv("ecoles_creches_idf_clean.csv")

# Titre de l'application
st.title("Analyse des Écoles et Crèches en Île-de-France")

# Sidebar avec filtre pour la ville
st.sidebar.header("Filtre de Ville")
villes = ["Toutes les villes"] + df["ville"].unique().tolist()  # Ajouter "Toutes les villes"
ville_choisie = st.sidebar.selectbox("Choisissez une ville", villes)

# Sidebar avec filtre pour le type d'établissement
st.sidebar.header("Filtre de Type d'Établissement")
types = ["Tous les types"] + df["type"].unique().tolist()  # Ajouter "Tous les types"
type_choisi = st.sidebar.selectbox("Choisissez un type d'établissement", types)

# Filtrer les données en fonction de la ville choisie
if ville_choisie != "Toutes les villes":
    df_ville = df[df["ville"] == ville_choisie]
else:
    df_ville = df

# Filtrer les données en fonction du type d'établissement choisi
if type_choisi != "Tous les types":
    df_ville = df_ville[df_ville["type"] == type_choisi]

# Affichage des premières lignes des données
st.header("Aperçu des données")
st.dataframe(df_ville.head())

# Statistiques descriptives
st.subheader(f"Statistiques pour {ville_choisie} - {type_choisi}" 
             if ville_choisie != "Toutes les villes" and type_choisi != "Tous les types"
             else "Statistiques pour toutes les villes et tous les types")
st.write(df_ville.describe())

# Visualisation : Distribution de la pollution (NO2, PM10, PM2.5)
st.subheader("Visualisation des niveaux de pollution")
st.write("Ce graphe présente les niveaux de pollutions relevés, au sein des établissements du type sélectionnés, pour la ville sélectionnées.")

# Graphique pour NO2, PM10 et PM2.5
if ville_choisie != "Toutes les villes" and type_choisi != "Tous les types":
    title = f"Niveaux de pollution pour {ville_choisie} - {type_choisi}"
elif ville_choisie != "Toutes les villes":
    title = f"Niveaux de pollution pour {ville_choisie} - {type_choisi}"  # Prend en compte le type d'école même si toutes les villes sont sélectionnées
else:
    title = f"Niveaux de pollution pour {type_choisi}"  # Affiche le type d'école uniquement si "Toutes les villes" est sélectionné

fig = px.box(df_ville, 
             y=["no2_2017", "pm10_2017", "pm25_2017"], 
             title=title)
st.plotly_chart(fig)

# Visualisation de la densité des équipements par ville
st.subheader("Densité des équipements par ville")
st.write("Ce graphe présente le nombre d\'établissembents scolaires, pour le type d\'établissement et la ville sélectionnés.")

# Titre dynamique pour le graphique de densité des équipements
if ville_choisie != "Toutes les villes" and type_choisi != "Tous les types":
    title2 = f"Nombre d'équipements par ville pour {ville_choisie} - {type_choisi}"
elif ville_choisie != "Toutes les villes":
    title2 = f"Nombre d'équipements par ville pour {ville_choisie}"  # Si une ville est sélectionnée
else:
    title2 = f"Nombre d'équipements par ville pour {type_choisi}"  # Si "Toutes les villes" et un type spécifique sont sélectionnés

fig2 = px.bar(df_ville, x="ville", y="nb_equipements_ville", title=title2)
st.plotly_chart(fig2)

# pour executer: streamlit run app.py