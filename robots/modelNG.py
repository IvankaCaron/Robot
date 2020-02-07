from robots.model import Robot

class RobotNG(Robot):
    
    def __init__(self, nom):
        super().__init__(nom)
        self.__turbo = False
        

    def avance(self,pas=2):
        if self.__turbo==True:
            pas = pas * 3
        for i in range(pas):
            super().avance()

    def demiTour(self):
        self.droite()
        self.droite()

    def gauche(self):
        #Nord
        if self._direction == "N":
            self._direction = "O"
        #Est
        elif self._direction == "E":
            self._direction = "N"
        #Sud
        elif self._direction == "S":
            self._direction = "E"
        #Ouest
        elif self._direction == "O":
            self._direction = "S"

    def turbostart(self):
        self.__turbo = True

    def turbostop(self):
        self.__turbo = False

    def etat(self):
        super().etat()
        if self.__turbo==True:
            print("le robot est en mode turbo")
        elif self.__turbo==False:
            print("le robot n est pas en mode turbo")
        