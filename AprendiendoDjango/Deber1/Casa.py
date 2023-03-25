from Inmueble import Inmueble

class Casa(Inmueble):        
        def __init__(self, nroHabitacion, cisterna):
            self.nroHabitacion = nroHabitacion
            self.cisterna = cisterna
        
        #======== Getter Setters ========         
        def setnroHabitacion(self, nroHabitacion):
            self.nroHabitacion = nroHabitacion

        def setcisterna(self, cisterna):
            self.cisterna = cisterna
            
        def getnroHabitacion(self):
            return self.nroHabitacion

        def getcisterna(self):
            return self.cisterna                        

        
        #======== Metodos ========      
        def getInfo (self, valorEntrada, valorXmt2):
            print ("======== Datos de la casa ======== " + "\n" +
                   "Valor casa: $" + str(self.calcularValorTerreno(valorXmt2)) + "\n" +
                   "Saldo a pagar: Con entrada de $" + str(valorEntrada) + " el saldo es: $" + str(self.validarEntrada(valorEntrada, valorXmt2)) + "\n" +
                   "Direccion: " + str(self.getDireccion()) + "\n" +
                   "Años antiguedad: " + str(self.getAntiguedad()) + "\n" +
                   "Nro habitaciones: " + str(self.nroHabitacion) + "\n" +
                   "¿ Tiene cisterna ?: " + self.cisterna)
