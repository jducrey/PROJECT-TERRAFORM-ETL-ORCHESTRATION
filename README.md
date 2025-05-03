# Analyse des Écoles et Crèches en Île-de-France

Ce projet est un pipeline de traitement de données qui comprend plusieurs étapes :

- Téléchargement d'un dataset CSV à partir d'une source distante.
- Traitement des données (nettoyage, transformation) via un processus ETL.
- Génération de rapports d’analyse au format HTML.
- Création d'une application de visualisation interactive avec Streamlit.
- Dockerisation de l'ensemble du projet.

Il est entièrement automatisé grâce à Terraform, qui orchestre le pipeline de données en local. Ce projet permet de démontrer l'utilisation de Terraform pour gérer un pipeline de données local, sans infrastructure cloud, tout en intégrant des visualisations interactives.

## 🚀 Fonctionnalités

- **Téléchargement et nettoyage des données** : Le dataset est téléchargé depuis une source distante, puis nettoyé et transformé pour une analyse plus poussée.
- **Génération de rapports HTML** : Utilisation de YData Profiling pour générer un rapport détaillé du dataset en HTML.
- **Visualisation des données** : Une application Streamlit permet d’interagir avec les données et de visualiser des graphiques sur les niveaux de pollution et la densité des équipements.
- **Dockerisation** : Le projet est entièrement dockerisé pour une exécution facile et isolée.
- **Infrastructure as Code** : Terraform est utilisé pour orchestrer le processus de téléchargement, traitement et génération des fichiers de sortie en local.

## 💡 Pourquoi Terraform sans cloud ?

L'objectif de ce projet est de démontrer l'utilisation de Terraform dans un contexte local. Cela permet de :

- Structurer un pipeline reproductible avec Terraform, même en local.
- Appliquer les bonnes pratiques de gestion d'infrastructure (réutilisabilité, documentation).
- Automatiser des processus complexes tout en gardant une architecture claire et bien définie.

## 🔧 Prérequis

Avant de commencer, assurez-vous d'avoir les outils suivants installés sur votre machine :

- **Python 3.x** : Pour exécuter les scripts ETL et l'application Streamlit.
- **Terraform** : Pour l’orchestration du pipeline et la gestion de l’infrastructure.
- **Docker** : Pour la dockerisation de l'application et du pipeline.

## ⚡ Installation

1. Clonez ce dépôt :

   ```bash
   git clone https://github.com/ton_utilisateur/mon_projet_etl.git
   cd mon_projet_etl
   ```

2. Installez les dépendances Python :

Vous pouvez installer les dépendances à l'aide de requirements.txt :
  ```bash
  pip install -r requirements.txt
  ```

3. Déployez avec Terraform :

Exécutez les commandes Terraform pour télécharger et traiter les données.
  ```bash
  terraform init
  terraform apply
  ```
  
4. Lancez l'application Streamlit :

Une fois que les données ont été traitées et sauvegardées, lancez l'application Streamlit :
  ```bash
  streamlit run app.py
  ```

Dockerisation (optionnel)
Si vous préférez dockeriser le projet, utilisez le Dockerfile pour créer une image et exécuter le projet dans un conteneur.
  ```bash
  docker build -t mon_projet_etl .
  docker run -p 8501:8501 mon_projet_etl
  ```

L'application sera accessible sur http://localhost:8501.

## 🛠️ Fonctionnement
- ETL : Le script etl.py s'occupe du processus ETL, où il télécharge les données, les nettoie et les transforme.

- Profiling : Le rapport HTML généré est produit par ydata-profiling et fournit une vue d'ensemble des données traitées.

- Visualisation avec Streamlit : L'application Streamlit (app.py) vous permet de visualiser les données et d'interagir avec elles grâce à des filtres dynamiques sur les villes et les types d’établissements.

## 📊 Exemple d'interface Streamlit
Voici un aperçu de l'interface Streamlit avec des options de filtrage sur les villes et types d’établissements :

- Sélection de ville : Filtrer par ville spécifique ou afficher toutes les villes.

- Sélection de type d’établissement : Filtrer par écoles ou crèches, ou choisir toutes les options.

- Visualisation des données : Graphiques interactifs montrant la pollution et la densité des équipements.

## 🔍 À propos des données
Les données utilisées dans ce projet concernent les écoles et crèches en Île-de-France, avec des informations sur les niveaux de pollution (NO2, PM10, PM2.5) et des caractéristiques géographiques et administratives des établissements.

## 👨‍💻 Contribuer
Les contributions sont les bienvenues ! Si vous avez des idées pour améliorer ce projet ou des corrections à proposer, n’hésitez pas à ouvrir un issue ou une pull request.

## 📜 Licence
Ce projet est sous licence MIT - voir le fichier LICENSE pour plus de détails.

