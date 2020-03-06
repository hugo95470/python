class animaux:
    def __init__(self, nb, regime, qqt_nrt):
        self.nb = 0
        self.regime = regime
        self.qtt_nrt = 0

    def __str__(self):
        return "cet animal est un " + self.nb

class terrestre(animaux):
    def __init__(self, nb, regime, qqt_nrt, nb_patte):
        super().__init__(nb, regime, qqt_nrt)
        self.nb_patte = 0

    def __str__(self):
        return "cet animal terrestre a " + self.nb_patte + " et est " + self.regime

if __name__=="__main__":
    
    zoo = {}
    zoo["humain"] = terrestre(2,"omnivore",600,2)
    zoo["lion"] = terrestre(1,"carnivore",3,4)
    zoo["lapin"] = terrestre(7,"herbivore",1,4)
    zoo["mouton"] = terrestre(5,"herbivore",5,4)
    zoo["chien"] = terrestre(2,"omnivore",2,0)
    zoo["pieuvre"] = animaux(1,"carnivore",2)
    zoo["serpent"] = terrestre(2,"carnivore",2,0)
    zoo["autruche"] = terrestre(4,"omnivore",1,2)
    zoo["poule"] = terrestre(8,"herbivore",20,2)


    #for nb in zoo:
    #    print("i y a un " + zoo["humain"].nb)
        
    input("Appuyer sur ENTER pour terminer le programme.")
