# Calculer la corrélation entre la taille et la longévité
correlation = data['longevity'].corr(data['height'])
print(f"Corrélation entre la taille et la longévité : {correlation}")

# Vous pouvez également explorer les corrélations avec d'autres variables
# Par exemple, en utilisant data['density'] et data['pollution']
