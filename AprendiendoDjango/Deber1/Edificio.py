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
        def getInfo (self, valorEntrada, valorXmt2):            
            print ("======== Datos del edificio ======== " + "\n" +
                   "Valor edificio: $" + str(self.calcularValorTerreno(valorXmt2)) + "\n" +
                   "Saldo a pagar: Con entrada de $" + str(valorEntrada) + " el saldo es: $" + str(self.validarEntrada(valorEntrada, valorXmt2)) + "\n" +
                   "Direccion: " + str(self.getDireccion()) + "\n" +
                   "Años antiguedad: " + str(self.getAntiguedad()) + "\n" +
                   "Nro pisos: " + str(self.nroPiso) + "\n" +
                   "Caracteristicas area social?: " + self.areaSocial)            
                