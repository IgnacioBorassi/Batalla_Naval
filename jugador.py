from tablero import Tablero
from oponente import Oponente

class Jugador():
    '''El jugador que inicia el juego de Batalla Naval'''
    
    def __init__(self):
        self.tablero=Tablero()
        self.oponente = Oponente()

        
    def tirarMisil(self,letra,numero):
        '''Ataca a la celda en cuestión, devolviendo el resultado del ataque'''
        
        if self.oponente.tablero.coordenadas[numero][letra].barco == None:
            self.misilHundido(numero, letra)
            print("Agua")
                
        elif self.oponente.tablero.coordenadas[numero][letra].barco.hundido == True:
            print("Ya esta hundido el barco")
                
        else:
            self.oponente.eliminarBarco(numero, letra)
            print("Hundiste un barco. Sabes cuantas vidas habia ahi? me imagine.")
            self.oponente.tablero.contador += 1


            if self.oponente.tablero.contador == 8:
                print("Gano el jugador")


    def agregarBarco(self, x,y):
        '''Agrega un barco dadas las coordenadas'''
        
        self.tablero.agregarBarco(x,y) 


    def eliminarBarco(self, x,y):
        '''Hunde un barco del oponente dadas las coordenas'''
        
        self.oponente.tablero.coordenadas[x][y].matarBarco() 

    def misilHundido(self, x,y):
        '''Ubica un misil dadas las coordenas en el tablero del oponente'''

        self.oponente.tablero.coordenadas[x][y].misilHundido()


    def sacarValores(self):
        '''Otorga letra y numero validos en una lista'''

        letra = str(input("Ingrese una letra: "))
        letra = letra.upper()
        letras = ['A','B','C','D','E','F','G','H']
        
        if letra not in ['A','B','C','D','E','F','G','H']: 
            while letra not in ['A','B','C','D','E','F','G','H']:
                letra = str(input("Ingrese una letra valida: "))
                letra = letra.upper()
                exit

        numero = int(input("Ingrese un numero: "))

        
        if numero in [1,2,3,4,5,6,7,8]:
            exit
        else:
            while numero not in [1,2,3,4,5,6,7,8]:
                numero = str(input("Ingrese un numero: "))

        for i in range (0,8):
            if letra == letras[i]:
                numero -= 1
                valores = [i, numero]
        return valores

        
