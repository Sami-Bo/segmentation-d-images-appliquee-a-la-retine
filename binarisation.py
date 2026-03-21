import numpy as np
import matplotlib.pyplot as plt
import cv2
from random import randrange


# read image
im = cv2.imread('images/pepper.jpg')
cv2.waitKey(0)
# calculate mean value from RGB channels and flatten to 1D array
vals = im.mean(axis=2).flatten()
# calculate histogram
counts, bins = np.histogram(vals, range(257))
print(counts, bins)
# plot histogram centered on values 0..255
plt.bar(bins[:-1] - 0.5, counts, width=1, edgecolor='none')
plt.xlim([-0.5, 255.5])
plt.show()

# algorithme
S = randrange(1, 256)
print('Seuil S choisi de manière aléatoire entre 1 et 256 : ', S, '\n')

def trouverSeuillage(S):
    nb_total, S1 = 0, 0
    for i in range(0, S):
        nb_total += counts[i]
        S1 += bins[i] * counts[i]
    if nb_total != 0:
        S1 /= nb_total

    nb_total, S2 = 0, 0
    for i in range(S, 255):
        nb_total += counts[i]
        S2 += bins[i] * counts[i]
    if nb_total != 0:
        S2 /= nb_total

    S = (S1 + S2) / 2
    return [int(S), S1, S2]


S_test = trouverSeuillage(S)
while S_test[0] != S:
    S = S_test[0]
    S_test = trouverSeuillage(S)

print(S)

# Charger l'image en niveaux de gris
image = cv2.imread('images/pepper.jpg', cv2.IMREAD_GRAYSCALE)


def seuillerImageProp1(tabS):
    # Choisir un seuil (par exemple 128)
    seuil = tabS[0]

    # Appliquer le seuil
    _, seuillee = cv2.threshold(image, seuil, 255, cv2.THRESH_BINARY)
    return seuillee


def seuillerImageProp2(tabS):
    # Choisir un seuil (par exemple 128)
    seuil = tabS[0]
    S1 = int(tabS[1])
    S2 = int(tabS[2])

    # Obtenir les dimensions de l'image
    hauteur, largeur = image.shape

    # Initialiser une nouvelle image seuillée
    seuillee = image.copy()

    # Parcourir chaque pixel de l'image
    for i in range(hauteur):
        for j in range(largeur):
            # Si le pixel est en dessous du seuil, mettre à S1
            if image[i, j] < seuil:
                seuillee[i, j] = S1
            # Sinon, mettre à S2
            else:
                seuillee[i, j] = S2

    return seuillee


# Afficher l'image seuillée
seuillee = seuillerImageProp1(S_test)
cv2.imshow('Image Seuillee - Methode 1', seuillee)
cv2.waitKey(0)
seuillee = seuillerImageProp2(S_test)
cv2.imshow('Image Seuillee - Methode 2', seuillee)
cv2.waitKey(0)
# cv2.destroyAllWindows()
