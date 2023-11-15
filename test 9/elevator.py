from sys import stdin

class Elevador:
    '''
    En esta clase se crea un elevador con lo informacion dicha en la prueba, este tiene piso actual, una direccion (Subiendo o bajando)
    tiene uno arreglo de pisos en los cuales se solicito el elecador y tambien tiene un pisos en laos cuales se le van a hacer peticiones (pisos_ingresados= {piso en el que se hace una peticion: piso solicitado})
    '''
    def __init__(self, piso_inicial, direccion_inicial):
        self.piso_actual = piso_inicial
        self.direccion = direccion_inicial
        self.pisos_ingresados = {}
        self.pisos_llamados = []

    def mover_elevador(self, pisos_llamados, pisos_ingresados):
        '''
        Este metodo se encarga de mover el elevador, hacia arriba o abajo segun las condiciones de llamada de cada uno de los pisos 
        y segun este, se encuentre subiendo o bajando.
        '''
        self.pisos_llamados = pisos_llamados #pisos que se deben solicitar
        self.pisos_ingresados = pisos_ingresados #solicitudes del elevador de la forma: {piso en que se hizo la solicitud, solicitud}
        while self.pisos_llamados:
            siguiente_piso = self.pisos_llamados.pop(0) # se recibe alguna solicitud
            self.direccion = 'Subiendo' if siguiente_piso > self.piso_actual else 'Bajando' #se decide la direccion en la se va a mover el elevador
            while self.piso_actual != siguiente_piso: #se mueve el elevador 
                print(f'Elevador {self.direccion}') #se muestre si el elevador sube o baja
                self.piso_actual += 1 if self.piso_actual < siguiente_piso else -1 #en caso de que sube, aumenta la cantidad de pisos necesaria, en caso de que llegue a su maximo, retorna -1
                print(f'Elevador en piso {self.piso_actual}')
                if self.piso_actual in self.pisos_ingresados: #si el piso actual se encuentra en los pisos que se deben visitar
                    if(self.pisos_ingresados[self.piso_actual] not in self.pisos_llamados and self.pisos_ingresados[self.piso_actual] != siguiente_piso):
                        self.pisos_llamados.append(self.pisos_ingresados[self.piso_actual]) #se agrega la solicitud que haya en el piso en que se encuentra
                    print(f'Piso ingresado {self.pisos_ingresados[self.piso_actual]}') #se ingresa un nuevo piso
            print(f'Elevador se detiene en piso {self.piso_actual}') #se detiene en el piso en que se encuentre en el momento.
            #print(f'Elevador se detiene en piso {self.piso_actual} → {self.pisos_llamados}')

peticiones = {}
piso_inicial = sLevel = int((stdin.readline().strip().split())[0]) #piso inicial
direccion_inicial =  map(str, stdin.readline().strip().split()) #'Subiendo' # o 'Bajando'
elevador = Elevador(piso_inicial, direccion_inicial)
arreglo_pisos = list(map(int, stdin.readline().strip().split())) #arreglo de pisos
vLevels = int((stdin.readline().strip().split())[0]) #cantidad de pisos ingresados
for i in range(vLevels):
    fLevel =  int((stdin.readline().strip().split())[0])  
    tLevel =  int((stdin.readline().strip().split())[0])
    peticiones[fLevel] = tLevel #dic = {piso ingresado, nuevo piso}
    
elevador.mover_elevador(arreglo_pisos, peticiones)
