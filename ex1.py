import os

def fonction(text, nom):
	os.chdir("C:/users/cabar/onedrive/bureau/")
	fichier_a = open(nom, "a")
	fichier_a.write(text)
	fichier_a.close()

if __name__ == "__main__":
	nom = input("nom du fichier : ")
	texte = input("text à écrire : ")

        fonction(texte, nom)

