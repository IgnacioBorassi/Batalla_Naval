from jugador import Jugador
class Juego():
    def __init__(self):
        self.jugador = Jugador()
        self.comenzarJuego()

    def comenzarJuego(self):
        '''Ayuda'''
        
        self.jugador.jugar()
        
        while (self.jugador.oponente.tablero.contador != 8):
            
            self.tableroOponente()
            self.tableroJugador()
            
            print("Su turno: Lanzara un misil en A-H y 1-8 ")
            valores = self.jugador.sacarValores()
            self.jugador.tirarMisil(valores[0], valores[1])

            if self.jugador.tablero.contador == 8:
                break
            
            self.tableroOponente()
            self.tableroJugador()

            print("Turno del oponente: ")
            valores = self.jugador.oponente.atacar()
            self.atacarAlJugador(valores[0],valores[1])

            if self.jugador.tablero.contador == 8:
                break
            
        self.tableroOponente()
        self.tableroJugador()
  
        if self.jugador.oponente.tablero.contador == 8:
            print ("Gano el jugador")
        else:
            print("Perdio el jugador")
                                
    def atacarAlJugador(self, letra, numero):
        '''Ataca a la celda en cuestión, devolviendo el resultado del ataque'''
        if self.jugador.tablero.coordenadas[numero][letra].barco == None:
            self.misilHundidoJ(numero, letra)
            print("Agua")
                
        elif self.jugador.tablero.coordenadas[numero][letra].barco.hundido == True:
            print("Ya esta hundido el barco")
                
        else:
            self.eliminarBarcoJ(numero, letra)
            print("El oponente hundio un barco.")
            self.jugador.tablero.contador += 1

        
        if self.jugador.tablero.contador == 8:
            print("Gano el oponente")

            
    def eliminarBarcoJ(self, x,y):
        '''Llama una funcion de celda para hundir un
        barco dadas las coord'''
        
        self.jugador.tablero.coordenadas[x][y].matarBarco() 


    def misilHundidoJ(self, x,y):
        '''Llama una funcion de celda para ubicar un
        misil dadas las coordendas sin un barco'''

        self.jugador.tablero.coordenadas[x][y].misilHundido()


    def tableroOponente(self):
        '''Muestra el tablero del oponente'''
        
        print("El tablero del oponente: ")
        self.jugador.oponente.tablero.dibujarTablero("0")


    def tableroJugador(self):
        '''Muestar el tablero del jugador'''

        print("Su tablero: ")
        self.jugador.tablero.dibujarTablero("0")

            
juego=Juego()
