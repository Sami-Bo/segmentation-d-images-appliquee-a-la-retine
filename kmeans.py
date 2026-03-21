import cv2
import numpy as np
from matplotlib import pyplot as plt
from random import randrange

# read image
im = cv2.imread('images/pepper.jpg')
cv2.waitKey(0)
# calculate mean value from RGB channels and flatten to 1D array
vals = im.mean(axis=2).flatten()
# calculate histogram
counts, bins = np.histogram(vals, range(257))
# plot histogram centered on values 0..255
plt.bar(bins[:-1] - 0.5, counts, width=1, edgecolor='none')
plt.xlim([-0.5, 255.5])
plt.show()




def init(K):
    tableau_classes = []
    tableau_intensites = []
    tableau_nombre_intensites = []
    for i in range(0, K):
        tableau_classes.append(randrange(0, 255))
        tableau_intensites.append(0)
        tableau_nombre_intensites.append(0)
    tableau_classes.sort()
    return [tableau_classes, tableau_intensites, tableau_nombre_intensites]


def reinitialiser(liste):
    # Remettez toutes les valeurs à 0
    for i in range(len(liste)):
        liste[i] = 0


def trouver_plus_proche_valeur(liste, cible):
    return min(liste, key=lambda x: abs(x - cible))


def moyenne(liste):
    tableau_classes = liste[0].copy()
    tableau_intensites = liste[1].copy()
    tableau_nombre_intensites = liste[2].copy()
    reinitialiser(tableau_intensites)
    reinitialiser(tableau_nombre_intensites)

    for i in range(0, 256):
        classe = trouver_plus_proche_valeur(tableau_classes, i)

        # Trouver l'indice de la valeur recherchée dans la liste
        indice = tableau_classes.index(classe)
        tableau_intensites[indice] += i
        tableau_nombre_intensites[indice] += 1

    for i in range(0, K):
        if tableau_nombre_intensites[i] != 0:
            tableau_classes[i] = int(tableau_intensites[i] / tableau_nombre_intensites[i])

    return [tableau_classes, tableau_intensites, tableau_nombre_intensites]

def segmenter(liste, image):
    # Créez une copie de la liste pour éviter de modifier l'original
    liste_copie = liste.copy()

    # Ajoutez 255 à la liste copiée
    liste_copie.append(255)
    # Obtenir les dimensions de l'image
    hauteur, largeur = image.shape

    # Initialiser une nouvelle image seuillée
    image_segmentee = image.copy()

    # Parcourir chaque pixel de l'image
    for i in range(hauteur):
        for j in range(largeur):
            # Si le pixel est en dessous du seuil, mettre à S1
            classe = trouver_plus_proche_valeur(liste_copie, image[i, j])
            image_segmentee[i, j] = classe

    return image_segmentee

K = randrange(2, 10)
liste = init(K)
liste2 = moyenne(liste)

while liste2[0] != liste[0]:
    liste = liste2
    liste2 = moyenne(liste)


# Charger l'image en niveaux de gris
image = cv2.imread('images/pepper.jpg', cv2.IMREAD_GRAYSCALE)
image_segmentee = segmenter(liste[0], image)
cv2.imshow(f'Segmentation pour K = {K}', image_segmentee)
cv2.waitKey(0)
