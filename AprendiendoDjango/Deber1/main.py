from Edificio import Edificio
from Casa import Casa

#Clase Casa
casa1 = Casa(3, "SI")
casa1.setAntiguedad(5)
casa1.setDireccion("Urb. Veranda mz 4 villa 1")
casa1.setMt2(120)
casa1.getInfo(500, 40)

#Clase Edificio
print ("    ")
edificio1 = Edificio(10, "piscina, ginmasio, BBQ")
edificio1.setAntiguedad(2)
edificio1.setDireccion("Malecon 2000")
edificio1.setMt2(700)
edificio1.getInfo(15000, 80)

#Detectar tipado
print ("    ")
print ("========= TIPOS ==========")
print ("Tipo de casa1: " + str(type(casa1)))
print ("Tipo de edificio1: " + str(type(edificio1)))
