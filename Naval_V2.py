import random

class Barco():
    '''Esto es un barco de 1x1'''
    
    def __init__(self, hundido):
        self.hundido = hundido


        
class Celda:
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
        self.cambiar(True, Barco(False))


    def matarBarco(self):
        '''Hunde un barco en la coordenada en cuestion.'''
        self.cambiar(True, Barco(True))


    def ubicarBarco(self):
        '''Saber si en la celda especificada hay un barco.'''
        
        if self.estado == True:
            print("Hay una serpiente en mi bota")
        else:
            print("Tu bota esta limpia")


            
class Tablero():
    def __init__(self):
        self.coordenadas = []
        self.listatablero = []
        self.crearCeldas()
        self.barcosRandom()
        self.contador = 0
        
    def crearCeldas(self):
        ''' Crea una lista de objeto Celda'''
        
        self.coordenadas = []
        self.listatablero = []
        
        for i in range(0,8):
            self.coordenadas.append([])
            for x in range(0,8):
                self.coordenadas[i].append(Celda(False, None))


    def tirarMisil(self,letra,numero):
        '''Ataca a la celda en cuestión, devolviendo el resultado del ataque'''

        numero -= 1
        letra -= 1

        if numero >= 8 or letra >=8 or numero <= -1 or letra <= -1:
            print("No hay coordenadas mayores a 8 o menores a 1.")

        else:
            self.coordenadas[numero][letra].estado = True
        
            if self.coordenadas[numero][letra].barco == None:
                print("Agua")
            elif self.coordenadas[numero][letra].barco.hundido == True:
                print("Ya esta hundido el barco")
            else:
                self.coordenadas[numero][letra].barco.hundido = True
                print("No te la puedo creer, man hundiste un barco. Sabes cuantas vidas habia ahi? no verdad? egoista.")
                self.contador += 1

                if self.contador == 8:
                    print("ganaste")

            self.crearTablero()

        
    def barcosRandom(self):
        '''Ubica 8 barcos de 1x1 en posiciones aleatorias'''
        
        for i in range(0,8):
            posicionX = int(random.randrange(0,8))
            posicionY = int(random.randrange(0,8))
            
            if self.coordenadas[posicionX][posicionY].estado == True:
                
                while self.coordenadas[posicionX][posicionY].estado == True:
                    posicionX=int(random.randrange(0,8))
                    posicionY=int(random.randrange(0,8))
                    
                self.coordenadas[posicionX][posicionY].cambiar(True, Barco(False))    
            else:
                self.coordenadas[posicionX][posicionY].cambiar(True, Barco(False))


    def ubicaciones(self):
        '''Da la ubicacion de los barcos colocados'''
        
        letras = ['A','B','C','D','E','F','G','H']
        numeros = ['1','2','3','4','5','6','7','8']
        for x in range(0,8):
            for i in range(0,8):
                if self.coordenadas[i][x].barco != None:
                    print("Hay un barco en: " + str(letras[x])+ str(numeros[i]))


    def crearTablero(self):
        self.listatablero = []
        for i in range(0,8):
            self.listatablero.append([])
            for x in range(0,8):
                if self.coordenadas[i][x].barco != None:
        ..            if self.coordenadas[i][x].barco.hundido == True:
                        self.listatablero[i].append("X")
                    else:    
                        self.listatablero[i].append("0")
                elif self.coordenadas[i][x].estado == True:
                    self.listatablero[i].append("+")
                else:
                    self.listatablero[i].append(" ")
        letras= ['  ','|A|','B','|C','|D|','E','|F','|G|','H|']
        numeros=['1','2','3','4','5','6','7','8']
        print(str(letras[0]) + str(letras[1])+ str(letras[2])+str(letras[3])+
              str(letras[4])+ str(letras[5])+ str(letras[6])+str(letras[7])+str(letras[8]))
        for i in range(0,8):
            print("|"+str(numeros[i])+ "|"+str(self.listatablero[i][0])+ "|" +
                  str(self.listatablero[i][1]) + "|" + str(self.listatablero[i][2])+ "|" +
                  str(self.listatablero[i][3]) + "|" + str(self.listatablero[i][4])+ "|" +
                  str(self.listatablero[i][5]) + "|" + str(self.listatablero[i][6])+ "|" +
                  str(self.listatablero[i][7]) + "|")






        
