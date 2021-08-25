from jugador import Jugador
class Juego():
    def __init__(self):
        rta = ""
        self.jugador = Jugador()
        self.comenzarJuego()

    def comenzarJuego(self):
        '''Comienza el juego de Batalla Naval'''
        
        self.pregunta()
        
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
        '''Ataca a la celda en cuestión del jugador, devolviendo el resultado del ataque'''
        
        if self.jugador.tablero.coordenadas[numero][letra].barco == None:
            self.misilHundidoJ(numero, letra)
            print("Agua")
                
        else:
            self.eliminarBarcoJ(numero, letra)
            print("El oponente hundio un barco.")
            self.jugador.tablero.contador += 1

        
        if self.jugador.tablero.contador == 8:
            print("Gano el oponente")

            
    def eliminarBarcoJ(self, x,y):
        '''Hunde un barco del jugador dadas las coordenadas'''
        
        self.jugador.tablero.coordenadas[x][y].matarBarco() 


    def misilHundidoJ(self, x,y):
        '''Hunde un misil en el tablero del jugador dadas las coordenadas'''

        self.jugador.tablero.coordenadas[x][y].misilHundido()


    def tableroOponente(self):
        '''Muestra el tablero del oponente'''
        
        print("El tablero del oponente: ")
        self.jugador.oponente.tablero.dibujarTablero(" ")


    def tableroJugador(self):
        '''Muestar el tablero del jugador'''

        print("Su tablero: ")
        self.jugador.tablero.dibujarTablero("0")

    def pregunta(self):
        '''Le da la capacidad al jugador de elegir el modo de juego'''

        self.rta = str(input("Desea jugar con 8 barcos random? De ser su respuesta 'No', los colocarà usted: "))
        self.rta = self.rta.upper()
        if self.rta == "SI":
            self.jugador.tablero.barcosRandom()
        elif self.rta == "NO":
            for i in range(0,8):
                valores = self.jugador.sacarValores()
                self.jugador.agregarBarco(valores[1],valores[0])
        else:
            while self.rta not in ["SI","NO"]:
                self.rta = str(input("Desea jugar con 8 barcos? De ser su respuesta 'No', los colocarà usted: "))
                self.rta = self.rta.upper()
            if self.rta == "SI":
                self.jugador.tablero.barcosRandom()
            elif self.rta == "NO":
                for i in range(0,8):
                    valores = self.jugador.sacarValores()
                    self.jugador.agregarBarco(valores[1],valores[0])

                    
juego=Juego()
