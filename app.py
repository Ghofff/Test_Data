from flask import Flask, jsonify, render_template
import requests
import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

app = Flask(__name__)

# Charger les données depuis l'API ou un fichier local si vous les avez déjà téléchargées
data = pd.read_json('https://opendata.paris.fr/api/explore/v2.1/catalog/datasets/arbresremarquablesparis/records?limit=20')

# Établir une connexion à la base de données MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="GH53863475",
    database="Test_DataEngineering"
)
if conn.is_connected():
    cursor = conn.cursor()
    
    # Définir la taille du lot pour l'insertion (par exemple, 1000 enregistrements à la fois)
    batch_size = 1000

    # Diviser les données en lots et les insérer dans la base de données par lot
    for i in range(0, len(data), batch_size):
        batch = data[i:i + batch_size]

        # Créer une liste de dictionnaires pour les données du lot à insérer
        values = [item for item in batch]

        # Générer dynamiquement la requête SQL pour l'insertion
        # Générer dynamiquement la requête SQL pour l'insertion
        if isinstance(batch[0], dict):
          keys = ", ".join(batch[0].keys())  # Utilisez les clés du premier dictionnaire comme colonnes
        else:
          print("Le premier élément de batch n'est pas un dictionnaire.")
        placeholders = ", ".join(["%s"] * len(values[0]))  # Générer des placeholders (%s) en fonction du nombre de clés

        insert_query = f"INSERT INTO ma_table ({keys}) VALUES ({placeholders})"

        # Créer une liste de valeurs à insérer dans le bon ordre
        insert_values = [tuple(item.values()) for item in values]

        # Insérer les données du lot dans la table
        cursor.executemany(insert_query, insert_values)

        # Valider les modifications après chaque lot
        conn.commit()

    # Fermer le curseur et la connexion
    cursor.close()
    conn.close()
else:
    print("La connexion à la base de données a échoué.")

@app.route('/')
def hello_world():
    return 'Bienvenue sur la page d\'accueil de l\'application !'
def index():
    return render_template('datavis.html')

@app.route('/correlation')
def correlation_analysis():
    try:
        # Calculer la corrélation entre la taille et la longévité
        correlation = data['longevity'].corr(data['height'])
        return f"Corrélation entre la taille et la longévité : {correlation}"
    except Exception as e:
        return f"Une erreur s'est produite : {str(e)}"

@app.route('/density')
def density_analysis():
    # Créer un graphique de dispersion de la densité par quartier
    plt.scatter(data['neighborhood'], data['density'])
    plt.xlabel('Quartier')
    plt.ylabel('Densité d\'arbres')
    plt.title('Répartition de la densité d\'arbres par quartier')
    plt.xticks(rotation=90)
    plt.savefig('density_by_neighborhood.png')  # Enregistrer le graphique
    plt.close()
    return 'Analyse de la densité terminée. Graphique enregistré.'

@app.route('/pollution')
def pollution_analysis():
    # Créer un graphique à barres pour la pollution par quartier
    pollution_by_neighborhood = data.groupby('neighborhood')['pollution'].mean()
    pollution_by_neighborhood.plot(kind='bar')
    plt.xlabel('Quartier')
    plt.ylabel('Pollution')
    plt.title('Pollution par quartier')
    plt.xticks(rotation=90)
    plt.savefig('pollution_by_neighborhood.png')  # Enregistrer le graphique
    plt.close()
    return 'Analyse de la pollution terminée. Graphique enregistré.'

if __name__ == '__main__':
    app.run()