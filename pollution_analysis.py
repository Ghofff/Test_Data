import matplotlib.pyplot as plt

# Créer un graphique à barres pour la pollution par quartier
pollution_by_neighborhood = data.groupby('neighborhood')['pollution'].mean()
pollution_by_neighborhood.plot(kind='bar')
plt.xlabel('Quartier')
plt.ylabel('Pollution')
plt.title('Pollution par quartier')
plt.xticks(rotation=90)
plt.show()
