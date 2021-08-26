import random
import celdas

class Tablero():
    '''Tablero de Batalla Naval'''
    
    def __init__(self):
        self.coordenadas = []
        self.listatablero = []
        self.crearCeldas()
        self.contador = 0
        self.numeros = ['1','2','3','4','5','6','7','8']

    def crearCeldas(self):
        ''' Crea una lista de objetos Celda'''
        
        self.coordenadas = []
        self.listatablero = []
        
        for i in range(0,8):
            self.coordenadas.append([])
            for x in range(0,8):
                self.coordenadas[i].append(celdas.Celda(False, None))

    
    def agregarBarco(self, x,y):
        '''Agrega un barco dadas las coordenadas'''
        
        self.coordenadas[x][y].agregarBarco()

        
    def barcosRandom(self):
        '''Ubica 8 barcos de 1x1 en posiciones aleatorias'''
        
        for i in range(0,8):
            posicionX = int(random.randrange(0,8))
            posicionY = int(random.randrange(0,8))
            
            if self.coordenadas[posicionX][posicionY].barco != None:
                
                while self.coordenadas[posicionX][posicionY].barco != None:
                    posicionX = int(random.randrange(0,8))
                    posicionY = int(random.randrange(0,8))
                    
                self.agregarBarco(posicionX, posicionY)    
            else:
                self.agregarBarco(posicionX, posicionY)


    def ubicaciones(self):
        '''Da la ubicacion de los barcos colocados'''
        
        letras = ['A','B','C','D','E','F','G','H']
        
        for x in range(0,8):
            for i in range(0,8):
                if self.coordenadas[i][x].barco != None:
                    print("Hay un barco en: " +
                          str(letras[x]) + str(self.numeros[i]))


    def dibujarTablero(self,barco):
        '''Dibuja el tablero con barcos, barcos hundidos,
        misiles ya lanzados y espacios de agua'''
        
        listatablero = []
        
        for i in range(0,8):
            listatablero.append([])
            for x in range(0,8):
                if self.coordenadas[i][x].barco != None:
                    if self.coordenadas[i][x].barco.hundido == True:
                        listatablero[i].append("X")
                    else:    
                        listatablero[i].append(barco)
                elif self.coordenadas[i][x].estado == True:
                    listatablero[i].append("+")
                else:
                    listatablero[i].append(" ")

        letras= ['  ','|A|','B','|C','|D|','E','|F','|G|','H|']

        print(str(letras[0]) + str(letras[1]) + str(letras[2]) +
              str(letras[3]) + str(letras[4]) + str(letras[5]) +
              str(letras[6]) + str(letras[7]) + str(letras[8]))

        for i in range(0,8):
            print("|"+str(self.numeros[i])+ "|" +
                  str(listatablero[i][0]) + "|" +
                  str(listatablero[i][1]) + "|" +
                  str(listatablero[i][2]) + "|" +
                  str(listatablero[i][3]) + "|" +
                  str(listatablero[i][4]) + "|" +
                  str(listatablero[i][5]) + "|" +
                  str(listatablero[i][6]) + "|" +
                  str(listatablero[i][7]) + "|")
