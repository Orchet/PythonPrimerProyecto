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
        def getInfo (self, valor):
            print ("Datos de la casa:" + "\n" +
                   "Valor terreno: $" + str(self.calcularValor(valor)) + "\n" +
                   "Direccion: " + self.getDireccion + "\n" +
                   "Antiguedad: " + str(self.getAntiguedad) + "\n" +
                   "Nro habitaciones: " + self.nroHabitacion + "\n" +
                   "Tiene cisterna?:" + self.cisterna)
