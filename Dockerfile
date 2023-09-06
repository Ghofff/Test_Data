# Utilisez une image Python officielle
FROM python:3.8-slim

# Créez un répertoire de travail
WORKDIR /app

# Copiez les fichiers de votre application dans le conteneur
COPY app.py /Test_Flask/app.py
COPY correlation_analysis.py /Test_Flask/correlation_analysis.py
COPY pollution_analysis.py /Test_Flask/pollution_analysis.py
COPY density_analysis.py /Test_Flask/density_analysis.py
COPY datavis.html /Test_Flask/templates/datavis.html





# Installez les dépendances Python
RUN pip install -r requirements.txt
RUN install virtualenv 
RUN pip install flask
RUN pip install matplotlib
RUN pip install pandas
RUN pip install rquests
RUN pip install mysqldb

# Exposez le port sur lequel votre application Flask écoute (par défaut 5000)
EXPOSE 5000

# Commande pour exécuter votre application Flask
CMD ["python", "app.py"]
#ou : CDM ["flask", "run"]
