# A-Force, Avengers, Mercs for Money, League of Realms, Strange Academy y X-Men.

class A_Force():

    def __init__(self, name, movement_type, health):
        try:
            self.name = name
            self.movement_type = movement_type
            self.health = health
            str(self.name)
            str(self.movement_type)
            int(self.health)
        except:
            print("No ha introducido los datos adecuados")
        
        self.superheroes = {"Name":self.name, "Movement_Type":self.movement_type, "Health":self.health, "ID":1}

    def is_undefeated(self):
        #Si la salud es negativa, devuelve True ya que esta derrotado
        if self.superheroes["Health"] <= 0:
            return True
        #Si la salud es positiva, devuelve False ya que no esta derrotado
        else:
            return False
    
    def surrender(self):
        self.superheroes["Health"] = 0
    
    def str(self):
        r = []
        for value in self.superheroes.values():
            r.append(value)
        print("{} with a {} and health: {}".format(r[0], r[1], r[2]))

    def repr(self):
        return print("{}\t{}\t{}".format(self.superheroes["ID"], 
        self.superheroes["Name"], self.superheroes["Movement_Type"]))


Aprobadisimo = A_Force("Medusa","karate Punch",100)
Aprobadisimo.str()
Aprobadisimo.repr()