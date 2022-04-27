
from PIL import Image
import numpy as nb
def afficher_tableau(tableau):
    n = len(tableau)
    m = len(tableau[0])
    for i in range(n):
        for j in range(m):
            print('{:>3d}'.format(tableau[i][j])," ", end="")
            print()
    return

def photomaton(tableau):

    n = len(tableau)
    nouv_tableau = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
            for j in range(n):
                if i % 2 == 0 and j % 2 == 0:
                    nouv_tableau[i//2][j//2] = tableau[i][j]
                if i%2 == 0 and j%2 == 1:
                    nouv_tableau[i//2][(n+j)//2]=tableau[i][j]
                if i%2 == 1 and j%2 == 0:
                    nouv_tableau[(n + i) // 2][j // 2] = tableau[i][j]
                if i%2 == 1 and j%2 == 1:
                    nouv_tableau[(n + i) // 2][(n + j) // 2] = tableau[i][j]
    return nouv_tableau


print("--- Transformation du photomaton ---")
tableau=nb.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
print((tableau)) ,print(nb.array(photomaton(tableau)))


def tableau_vers_image(tableau, nom_image):
    nom_fichier = "output/" + "koko " + ".bmp"
    fic = open("nom_fichier", "w")
    fic.write("P2\n")
    nb_lig = len(tableau)
    nb_col = len(tableau[0])
    fic.write(str(nb_col) + " " + str(nb_lig) + "\n")
    niveaux = 255
    fic.write(str(niveaux) + "\n")
    for i in range(nb_lig):
        ligne = ""
        for j in range(nb_col):
            coul = tableau[i][j]
            ligne = ligne + str(coul) + " "
        ligne = ligne + "\n"

        fic.write(ligne)

    fic.close()
    return


print("--- Tableau vers image ---")
tableau = [[128, 192, 128, 192, 128], [224, 0, 228, 0, 224], [228, 228, 228, 228, 228],
           [224, 64, 64, 64, 224], [192, 192, 192, 192, 192]]
tableau_vers_image(tableau, "test")


def image_vers_tableau(nom_image):
    nom_fichier = "input/" + "koko" + ".bmp"
    fic = open("nom_fichier", "r")
    i = 0
    for ligne in fic:
        if i == 1:
            liste_ligne = ligne.split()
            nb_col = int(liste_ligne[0])
            nb_lig = int(liste_ligne[1])
            tableau = [[0 for j in range(nb_col)] for i in range(nb_lig)]
        elif i > 2:
            liste = ligne.split()
            for j in range(nb_col):
                tableau[i - 3][j] = int(liste[j])
        i = i + 1

    fic.close()
    return tableau


print("--- Image vers tableau ---")
test_tableau = image_vers_tableau("test")
print(test_tableau)

afficher_tableau(test_tableau)


def ecrire_fichier_image_gris():
    nom_fichier = "input/koko.bmp"
    fic = open("nom_fichier", "w")

    fic.write("P2\n")
    nb_col = 256
    nb_lig = 256
    fic.write(str(nb_col) + " " + str(nb_lig) + "\n")
    niveaux = 255
    fic.write(str(niveaux) + "\n")
    for i in range(nb_lig):
        ligne = ""
        for j in range(nb_col):
            coul = (i ** 2 + j ** 2) % 256  # un niveau de gris en fonction de i et j
            ligne = ligne + str(coul) + " "
        ligne = ligne + "\n"

        fic.write(ligne)

    fic.close()
    return


print("--- Fichier 'image.pgm' ---")
ecrire_fichier_image_gris()


def photomaton_images(nom_image, kmax):
    tableau = image_vers_tableau("koko.bmp")
    tableau_vers_image(tableau, "koko.bmp" + "_photo_" + str(0))
    n = len(tableau)
    tab = [[tableau[i][j] for j in range(n)] for i in range(n)]
    for k in range(1, kmax + 1):
        tab = photomaton(tab)
        tableau_vers_image(tab, "koko.bmp" + "_photo_" + str(k))
    return


nom_imag = "koko.bmp"
img1 = open(nom_imag)
nana = photomaton_images(img1, 8)
Image.show(nana)
Image.close()
photomaton_images("koko.bmp", 8)
photomaton_images("pi_gimp_new", 8)
photomaton_images("chat_gimp_new", 8)


