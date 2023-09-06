import matplotlib.pyplot as plt

# Créer un graphique de dispersion de la densité par quartier
plt.scatter(data['neighborhood'], data['density'])
plt.xlabel('Quartier')
plt.ylabel('Densité d\'arbres')
plt.title('Répartition de la densité d\'arbres par quartier')
plt.xticks(rotation=90)
plt.show()
