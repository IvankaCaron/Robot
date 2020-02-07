#from model import Robot

class Robot:
    def __init__(self, nom):
        self._nom = nom
        self._x = 0
        self._y = 0
        self._direction = 'E'
    
    def avance(self):
        #Nord
        if self._direction == "N":
            self._y += 1
        #Est
        elif self._direction == "E":
            self._x += 1
        #Sud
        elif self._direction == "S":
            self._y -= 1
        #Ouest
        elif self._direction == "O":
            self._x -= 1
        else:
            pass
    
    def droite(self):
        #Nord
        if self._direction == "N":
            self._direction = "E"
        #Est
        elif self._direction == "E":
            self._direction = "S"
        #Sud
        elif self._direction == "S":
            self._direction = "O"
        #Ouest
        elif self._direction == "O":
            self._direction = "N"

    def position(self):
        print("_x : ",self._x)
        print("_y : ",self._y)

    def etat(self):
        print("_nom: ", self._nom)
        print("_x: ",self._x)
        print("_y: ",self._y)
        print("_direction : ", self._direction)

        


        
    




