class Inmueble:                
        def __init__(self, mt2, antiguedad, direccion):
            self.mt2 = mt2
            self.antiguedad = antiguedad
            self.direccion = direccion
        
        #======== Getter Setters ========         
        def setMt2(self, mt2):
            self.mt2 = mt2
            
        def setAntiguedad(self, antiguedad):
            self.antiguedad = antiguedad
        
        def setDireccion (self, direccion):
            self.direccion = direccion

        def getMt2(self):
            return self.mt2

        def getAntiguedad(self):
            return self.antiguedad

        def getDireccion(self):
            return self.direccion
        
        
        #======== Metodos ========         
        def calcularValorTerreno (self, valorXmt2):
            return (self.getMt2() * valorXmt2)
        
        def validarEntrada (self, valorEntrada, valorXmt2):
            valorTerreno = calcularValorTerreno(valorXmt2)
            saldo = valorTerreno - valorEntrada
            return("Valor Terreno: $" + str(valorTerreno) + ", Saldo para pagar: $" + str(saldo))
            




