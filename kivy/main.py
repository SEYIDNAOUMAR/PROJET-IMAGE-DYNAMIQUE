from kivy.app import App
#from matplotlib import image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from matplotlib import image
from matplotlib import pyplot as plt
from PIL.Image import*
from PIL import Image


class jeu(GridLayout):
    def graphique(self):
        self.data = image.imread("koko.bmp")
        print(self.data)
        plt.imshow(self.data)
        plt.show()

    class jeu2(GridLayout):
        def photomaton(self):

            for a in range(1, 9):

                img = Image.open('koko.bmp')

                # rÈcupÈration de la largeur et hauteur de l’image

                colonne, ligne = img.size

                # crÈation d’une image de mÍme type

                imgF = Image.new(img.mode, img.size)

                # boucle de traitement des pixel

                for j in range(ligne):

                    for i in range(colonne):

                        pixel = img.getpixel((i, j))

                        # on calcule le complement ‡ MAX pour chaque composante – effet nÈgatif

                        if i % 2 == 0 and j % 2 == 0:
                            (x, y) = (i // 2, j // 2)

                        if i % 2 == 0 and j % 2 == 1:
                            (x, y) = (i // 2, (ligne + j) // 2)

                        if i % 2 == 1 and j % 2 == 0:
                            (x, y) = ((colonne + i) // 2, j // 2)

                        if i % 2 == 1 and j % 2 == 1:
                            (x, y) = ((colonne + i) // 2, (ligne + j) // 2)

                        imgF.putpixel((x, y), pixel)

                        # composition de la nouvelle image

                # la fonction de PIL qui fait la mÍme chose

                # imgF = ImageChops.invert(img)

                # affichage de l’image

                imgF.show()

                c = a + 1

                imgF.save('koko.bmp')

            # fermeture du fichier image

            img.close()


class Game(App):
    def build(self):
        self.title = "IMAGE DYNAMIQUE"
        self.load_kv("game.kv")

        return jeu()
        return jeu2()







if __name__=='__main__':
    Game().run()



