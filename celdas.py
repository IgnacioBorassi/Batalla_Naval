import barcos

class Celda():
    '''Esto es una celda, contiene barcos, misiles y/o agua.'''
    
    def __init__(self, estado, barco):
        self.estado = estado
        self.barco = barco

        
    def cambiar(self, estado, barco):
        '''Poder cambiar el estado de la celda y del barco en cuestion.'''
        
        self.estado = estado
        self.barco = barco


    def agregarBarco(self):
        '''Agrega un barco en la coordenada en cuestion.'''
        self.cambiar(True, barcos.Barco(False))


    def matarBarco(self):
        '''Hunde un barco en la coordenada en cuestion.'''
        self.cambiar(True, barcos.Barco(True))

    def misilHundido(self):
        '''Ubica un misil en la coordenada en cuestion cuando no hay
        un barco'''
        self.cambiar(True, None)

        
    def estadoCelda(self):
        '''Saber si en la celda especificada esta ocupada
        por un barco o misil.'''
        estadoActual = ""
        if self.estado == True:
            if self.barco != None:
                if self.barco.hundido == True:
                    estadoActual = "BarcoH"
                    return estadoActual
                else:
                    estadoActual = "BarcoNoH"
                    return estadoActual
            else:
                estadoActual = "MisilH"
                return estadoActual
        else:
            estadoActual = "Agua"
            return estadoActual
