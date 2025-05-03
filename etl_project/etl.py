import pandas as pd
from ydata_profiling import ProfileReport

input_file = "ecoles_creches_idf.csv"
output_csv = "ecoles_creches_idf_clean.csv"
output_parquet = "ecoles_creches_idf_clean.parquet"
output_html = "ecoles_creches_idf_report.html"

# Chargement
try:
    df = pd.read_csv(input_file, sep=",", encoding="utf-8")
except Exception as e:
    print(f"Erreur de lecture : {e}")
    exit()

# Verif
df.columns = df.columns.str.strip()  # Supprime les espaces en début/fin
df.columns = df.columns.str.replace('\u200b', '')  # retire caractères invisibles éventuels
print("Colonnes disponibles :", df.columns.tolist())
print(df.head())

# Nettoyage des noms de colonnes
df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

# Sélection des colonnes utiles
colonnes_utiles = [
    "id", "nom", "departement", "ville", "cp", "type",
    "no2_2017", "pm10_2017", "pm25_2017", "geometry"
]

df = df[[col for col in colonnes_utiles if col in df.columns]]

# Conversion des colonnes polluantes en float
for pollutant in ["no2_2017", "pm10_2017", "pm25_2017"]:
    df[pollutant] = pd.to_numeric(df[pollutant], errors="coerce")

# Nettoyage : suppression des lignes sans ville ou type
df.dropna(subset=["ville", "type"], inplace=True)

# Ajout d'une colonne : nombre d'équipements par ville
equipements_par_ville = df.groupby("ville")["id"].transform("count")
df["nb_equipements_ville"] = equipements_par_ville

# Export CSV
df.to_csv(output_csv, index=False, encoding="utf-8")

# Export Parquet (rapide, compressé, idéal pour du traitement en data science)
df.to_parquet(output_parquet, index=False)

# Création du rapport HTML avec ydata-profiling en mode minimal
profile = ProfileReport(df, title="Profil des Écoles et Crèches IDF", minimal=True)
profile.to_file(output_html)

print(f"Données nettoyées sauvegardées dans :\n - {output_csv}\n - {output_parquet}\n - Rapport généré : {output_html}")