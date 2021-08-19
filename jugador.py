from tablero import Tablero

class Jugador():
    def __init__(self):
        self.tablero=Tablero()
        jugador=Jugador()
        

        
    def tirarMisil(self,letra,numero):
        '''Ataca a la celda en cuestión, devolviendo el resultado del ataque'''

        numero -= 1
        letra -= 1

        if numero >= 8 or letra >=8 or numero <= -1 or letra <= -1:
            print("No hay coordenadas mayores a 8 o menores a 1.")

        else:
        
            if self.tablero.coordenadas[numero][letra].barco == None:
                self.misilHundido(numero, letra)
                print("Agua")
                
            elif self.tablero.coordenadas[numero][letra].barco.hundido == True:
                print("Ya esta hundido el barco")
                
            else:
                self.eliminarBarco(numero, letra)
                print("No te la puedo creer, man hundiste un barco. Sabes cuantas vidas habia ahi? no verdad? egoista.")
                self.tablero.contador += 1

                if self.tablero.contador == 8:
                    print("ganaste")

            self.tablero.dibujarTablero()


    def agregarBarco(self, x,y):
        '''Llama una funcion de celda para agregar un
        barco dadas las coord'''
        
        self.tablero.agregarBarco(x,y) 


    def eliminarBarco(self, x,y):
        '''Llama una funcion de celda para hundir un
        barco dadas las coord'''
        
        self.tablero.coordenadas[x][y].matarBarco() 

    def misilHundido(self, x,y):
        '''Llama una funcion de celda para ubicar un
        misil dadas las coordendas sin un barco'''

        self.tablero.coordenadas[x][y].misilHundido()
