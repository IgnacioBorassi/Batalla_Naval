from tablero import Tablero
from oponente import Oponente

class Jugador():
    def __init__(self):
        self.tablero=Tablero()
        self.rta = " "
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
        '''Llama una funcion de celda para agregar un
        barco dadas las coord'''
        
        self.tablero.agregarBarco(x,y) 


    def eliminarBarco(self, x,y):
        '''Llama una funcion de celda para hundir un
        barco dadas las coord'''
        
        self.oponente.tablero.coordenadas[x][y].matarBarco() 

    def misilHundido(self, x,y):
        '''Llama una funcion de celda para ubicar un
        misil dadas las coordendas sin un barco'''

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

    
    def jugar(self):
        '''Le da la capacidad al jugador de elegir el modo de juego y de
        ingresar coordenadas para tirar un misil'''
        if self.rta != "":
            self.rta = str(input("Desea jugar con 8 barcos random? De ser su respuesta 'No', los colocarà usted: "))
            self.rta = self.rta.upper()
            if self.rta == "SI":
                self.tablero.barcosRandom()
                self.rta = ""
            elif self.rta == "NO":
                for i in range(0,8):
                    valores = self.sacarValores()
                    self.agregarBarco(valores[1],valores[0])
                self.rta = ""
            else:
                while self.rta not in ["SI","NO"]:
                    self.rta = str(input("Desea jugar con 8 barcos? De ser su respuesta 'No', los colocarà usted: "))
                    self.rta = self.rta.upper()
                if self.rta == "SI":
                    self.tablero.barcosRandom()
                    self.rta = ""
                elif self.rta == "NO":
                    for i in range(0,8):
                        valores = self.sacarValores()
                        self.agregarBarco(valores[1],valores[0])
                    self.rta = ""
        '''       
        print("Ingrese los valores para tirar el misil en: A-H y 1-8")
        valores = self.sacarValores()
        return valores
        self.tirarMisil(valores[0],valores[1])'''
        
