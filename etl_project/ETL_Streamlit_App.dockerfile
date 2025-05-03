# Utilise une image officielle Python
FROM python:3.10-slim

# Crée un dossier dans le conteneur
WORKDIR /app

# Copie les fichiers du projet
COPY . .

# Installe les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Port exposé pour Streamlit
EXPOSE 8501

# Commande pour lancer Streamlit
CMD ["streamlit", "run", "app.py", "--server.enableCORS=false"]