class Inmueble:                
        def __init__(self, valorMt2, antiguedad, direccion):
            self.valorMt2 = valorMt2
            self.antiguedad = antiguedad
            self.direccion = direccion
        
        #======== Getter Setters ========         
        def setvalorMt2(self, valorMt2):
            self.valorMt2 = valorMt2
            
        def setAntiguedad(self, antiguedad):
            self.antiguedad = antiguedad
        
        def setDireccion (self, direccion):
            self.direccion = direccion

        def getvalorMt2(self):
            return self.valorMt2

        def getAntiguedad(self):
            return self.antiguedad

        def getDireccion(self):
            return self.direccion
        
        
        #======== Metodos ========         
        def calcularValor (self, metros):
            return (self.getvalorMt2() * metros)
        
        def validarValorMt2 (self, valor):
            return("Valor Mt2: $" + str(self.getvalorMt2()) + ", valor disponible para pagar: $" + str(valor))
            


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
                