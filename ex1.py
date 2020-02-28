import os

def fonction(text, nom):
	os.chdir("C:/users/cabar/onedrive/bureau/")
	fichier_a = open(nom, "a")
	fichier_a.write(text)
	fichier_a.close()


nom = input("nom du fichier : ")
texte = input("text à écrire : ")

if __name__ == "__main__":
        fonction(texte, nom)

