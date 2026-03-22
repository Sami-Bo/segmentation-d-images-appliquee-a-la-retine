# Segmentation d’images

Ce projet implémente des techniques de **segmentation d’images appliquées à des images de type "pepper" ou rétiniennes"**, utilisant des méthodes de seuillage et de clustering pour isoler les zones d’intérêt.

## Objectifs
- Segmenter les images pour mettre en évidence des structures importantes.
- Expérimenter avec différentes approches : seuillage adaptatif et K-means sur les niveaux de gris.
- Comparer les résultats et visualiser l’efficacité de chaque méthode.

## Fichiers Python
### `binarisation.py`
- Lecture d’une image RGB avec OpenCV.
- Conversion en niveaux de gris.
- Calcul de l’histogramme des intensités.
- Détermination d’un seuil optimal via un **algorithme itératif de seuillage**.
- Deux méthodes de seuillage :  
  1. **Seuil simple** (binaire)  
  2. **Seuil pondéré** avec moyenne des classes de pixels (S1 et S2)
- Visualisation des images segmentées avec OpenCV.

### `kmeans.py`
- Implémentation d’un **algorithme K-means sur les intensités de l’image**.
- Initialisation aléatoire des classes et mise à jour itérative des centres.
- Assignation de chaque pixel à la classe la plus proche.
- Visualisation finale de l’image segmentée pour un K aléatoire (entre 2 et 9).

## Techniques et outils
- **Python 3**
- **OpenCV** : lecture, conversion, affichage et traitement d’images.
- **NumPy** : manipulation de tableaux et calculs numériques.
- **Matplotlib** : affichage des histogrammes.
- **Random** : initialisation aléatoire pour seuil et K-means.
- Algorithmes :
  - **Seuillage itératif adaptatif** pour binariser ou pondérer l’image.
  - **K-means** pour regrouper les pixels par intensité.

## Fonctionnement
1. Charger l’image avec OpenCV (`cv2.imread`).
2. Calculer l’histogramme pour analyser la distribution des intensités.
3. Appliquer la méthode de segmentation choisie : seuillage ou K-means.
4. Afficher l’image segmentée avec OpenCV (`cv2.imshow`).

## Résultats
- **Seuil simple et pondéré** : images binarisées ou avec intensités regroupées en deux classes.
- **K-means** : images segmentées selon K classes, permettant une détection plus fine des zones d’intérêt.

## Visualisation
Les images segmentées sont affichées à l’écran pour comparaison directe des méthodes.
