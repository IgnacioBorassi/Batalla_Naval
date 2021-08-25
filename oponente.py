import random
from tablero import Tablero

class Oponente():
    '''Oponente del Batalla Naval'''
    
    def __init__(self):
        self.tablero=Tablero()
        self.tablero.barcosRandom()


    def eliminarBarco(self, x,y):
        '''Hunde un barco dadas las coordenaas'''
        
        self.tablero.coordenadas[x][y].matarBarco() 


    def misilHundido(self, x,y):
        '''Llama una funcion de celda para ubicar un
        misil dadas las coordendas sin un barco'''

        self.tablero.coordenadas[x][y].misilHundido()


    def atacar(self):
        '''Le da la capacidad al oponente de elegir las
        coordenadas para tirar un misil'''
        
        posicionX = int(random.randrange(0,8))
        posicionY = int(random.randrange(0,8))
            
        if self.tablero.coordenadas[posicionX][posicionY].estadoCelda() == "MisilH" or self.tablero.coordenadas[posicionX][posicionY].estadoCelda() == "BarcoH":
                
            while self.tablero.coordenadas[posicionX][posicionY].estadoCelda == "MisilH" or self.tablero.coordenadas[posicionX][posicionY].estadoCelda() == "BarcoH":
                posicionX = int(random.randrange(0,8))
                posicionY = int(random.randrange(0,8))
                
        valores= [posicionX, posicionY]
        return valores
