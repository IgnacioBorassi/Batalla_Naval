from tablero import Tablero

class Jugador():
    def __init__(self):
        self.tablero=Tablero()
        self.rta = " "
        self.jugar()

    def tirarMisil(self,letra,numero):
        '''Ataca a la celda en cuestión, devolviendo el resultado del ataque'''
        
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
                print("Hundiste un barco. Sabes cuantas vidas habia ahi? me imagine.")
                self.tablero.contador += 1


            self.tablero.dibujarTablero()
            if self.tablero.contador != 8:
                self.jugar()
            else:
                print("ganaste pa")


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
                
        print("Ingrese los valores para tirar el misl en: A-H y 1-8")
        valores = self.sacarValores()
        self.tirarMisil(valores[0],valores[1])
        


jugador=Jugador()
