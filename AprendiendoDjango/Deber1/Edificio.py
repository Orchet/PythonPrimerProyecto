from Inmueble import Inmueble

class Edificio(Inmueble):        
        def __init__(self, nroPiso, areaSocial):
            self.nroPiso = nroPiso
            self.areaSocial = areaSocial
        
        #======== Getter Setters ========         
        def setnroPiso(self, nroPiso):
            self.nroPiso = nroPiso

        def setareaSocial(self, areaSocial):
            self.areaSocial = areaSocial
            
        def getnroPiso(self):
            return self.nroPiso

        def getareaSocial(self):
            return self.areaSocial                        

        
        #======== Metodos ========      
        def getInfo (self, valor):
            print ("Datos del edificio" + "\n" +
                   "Valor terreno: $" + str(self.calcularValor(valor)) + "\n" +
                   "Direccion: " + self.getDireccion + "\n" +
                   "Antiguedad: " + str(self.getAntiguedad) + "\n" +
                   "Nro pisos: " + self.nroPiso + "\n" +
                   "Caracteristicas area social?:" + self.areaSocial)
                