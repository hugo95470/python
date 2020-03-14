import datetime
import time

class Animal:
    def __init__(self, genre, birth_year, sex, age):
        self.genre = genre
        self.birth_year = birth_year
        self.sex = sex
        self.age = age

    def __str__(self):
        return "ceci est un " + self.genre +" est " + self.sex + " et a " + str(self.age) + " mois"

class Farm:
    def __init__(self, name, date_creation, liste_animaux):
        self.name = name
        self.date_creation = date_creation
        self.liste_animaux = liste_animaux
    
    #def __init__(self, name, json_string):
    #    pass

    def __str__(self):
        return "|          "+ self.name + "         |"
        
if __name__=="__main__":
    date_time = datetime.datetime.now()
    
    animal_1=[Animal("cochon", str(date_time), "masculin", 0), Animal("cheval", str(date_time), "feminin", 0)]
    animal_2=[Animal("chevre", str(date_time), "feminin", 0), Animal("cochon", str(date_time), "feminin", 0)]
    animal_3=[Animal("poule", str(date_time), "masculin", 0)]
    
    Farm_list = []
    Farm_list.append(Farm("ferme n°1", date_time, animal_1))
    Farm_list.append(Farm("ferme n°2", date_time, animal_2))
    Farm_list.append(Farm("ferme n°3", date_time, animal_3))
    
    Farm_list[0].liste_animaux.append(Animal("poule", str(date_time), "masculin", 0))
    
    while date_time.month<12:
        date_time = date_time + datetime.timedelta(weeks = +4)
        print (date_time)
        
        for farm in Farm_list:
            print(" ===========================")
            print (farm)
            print (" ===========================")
            
            for animals in farm.liste_animaux:
                animals.age = animals.age + 1
                print (animals)
                print ("")
                print ("")
                time.sleep(0.1)
        








    