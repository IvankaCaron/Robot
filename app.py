from model import Robot
from modelNG import RobotNG

robot1 = Robot("Cedric")
print(robot1._nom)
robot1.avance()
robot1.avance()
robot1.droite()
robot1.avance()
robot1.avance()
robot1.etat()

print("novy robot")

robot2 = Robot("ja")
print(robot2._nom)
robot2.avance()
robot2.avance()
robot2.droite()
robot2.avance()
robot2.avance()
robot2.avance()
robot2.avance()
robot2.droite()
robot2.etat()

print("novy robotNG")
meidi = RobotNG("Meidi")
print(meidi._nom)
meidi.avance()
meidi.gauche()
meidi.avance()
meidi.avance()
meidi.etat()

print("novy robotNG + turbo")
ana = RobotNG("Ana")
print(ana._nom)
ana.avance(pas = 4)
ana.turbostart()
ana.avance(pas = 4)
ana.etat()
ana.droite()
ana.avance(pas = 4)
ana.etat()
ana.turbostop()
ana.avance()
ana.etat()