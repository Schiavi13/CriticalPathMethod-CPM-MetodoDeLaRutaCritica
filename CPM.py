class Actividad():    #clase actividad
  def __init__(self,duracion, inicio_cercano, inicio_lejano, termino_cercano, termino_lejano, holgura, etapa,nombre = ""):
    self.duracion = duracion
    self.inicio_cercano = inicio_cercano
    self.inicio_lejano = inicio_lejano
    self.termino_cercano = termino_cercano
    self.termino_lejano = termino_lejano
    self.holgura = holgura
    self.etapa = etapa
    self.precedencia = []
    self.nombre = nombre

  def calcularInicioCercano(self):    #calcula el inicio cercano, buscando el termino lejano de una actividad de la etapa anterior
    self.inicio_cercano = lista_etapas[self.etapa-1][0].termino_lejano

  def calcularTerminoCercano(self):    #calcula el termino cercano, sumando la duración de la actividad al inicio cercano
    self.termino_cercano = int(self.inicio_cercano) + int(self.duracion)

  def asignarEtapa(self):        #calcula la etapa mediante la función determinarEtapa y le suma 1
    self.etapa = determinarEtapa(self.precedencia)+1
	
  def calcularTerminoLejano(self):     #calcula el termino lejano mediante la función maxDuracionEtapa
    self.termino_lejano = self.inicio_cercano + maxDuracionEtapa(self.etapa)
    

  def calcularHolgura(self):    #calcula la holgura restando el termino cercano al temrino lejano
    self.holgura = self.termino_lejano - self.termino_cercano

  def calcularInicioLejano(self):    #calcula el inicio lejano sumandole al inicio cercano la holgura
    self.inicio_lejano = self.inicio_cercano + self.holgura

#------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------	

def listaEtapas(n):    #función que inicializa la lista de etapas
  lista = []
  for i in range (0,n+1):
    lista.append([]*(n+1))
  return lista


lista_actividades = []
lista_precedencias= []


def llenarActividades(n):    #función que inicializa la lista de actividades, adicionando una actividad nula al inicio
  actividad_nula = Actividad(0,0,0,0,0,0,0)
  actividad_nula.nombre = "Nula"
  lista_actividades.append(actividad_nula)
  for i in range (0,n):
    actividad = Actividad(0,0,0,0,0,0,0)
    lista_actividades.append(actividad)

def definirNombres():    #función que asigna los nombres de las actividades según el abecedario
  for i in range (0,len(lista_actividades)-1):
    name = chr(65+i)
    lista_actividades[i+1].nombre=name

def determinarEtapa(precedencias):    #Función que determina la etapa máxima a la que pertenecen las precedencias de una actividad
  lista=[]
  for i in range (0,len(precedencias)):
    lista.append(precedencias[i].etapa)
  return max(lista)
"""
def llenarEtapas():        #Función que llena una lista de actividades por etapas como su índice
  actividad_nula = Actividad(0,0,0,0,0,0,0)
  lista_etapas.append(actividad_nula)
  for i in range len(lista_actividades)-1:
    lista_etapas[lista_actividades[i+1].getEtapa].append(lista_actividades[i+1])
"""
def maxDuracionEtapa(etapa):    #función que determina la duración máxima de una etapa
  lista = []
  for i in range (0,len(lista_etapas[etapa])):
    lista.append(lista_etapas[etapa][i].duracion)
  return int(max(lista))

def rutaCritica():    #función que determina la ruta crítica
  lista = []
  inic = 2
  compare = 1
  for i in range (0,len(lista_actividades)):
    if lista_actividades[i].holgura == 0:
      lista.append(lista_actividades[i])
  for i in range (1,len(lista)):
    if lista[len(lista)-inic].etapa == lista[len(lista)-compare].etapa:
      lista.remove(lista[len(lista)-inic])
    else:
      inic = inic+1
      compare = compare+1
  return lista

def asignarDuracion():    #función que asigna las duraciones de las actividades
  for i in range (0,len(lista_actividades)-1):
    print("Ingrese la duración de la etapa "+lista_actividades[i+1].nombre)
    n=input()
    lista_actividades[i+1].duracion=n 

def asignarPrecedencias():    #función que asigna las precedencias de las actividades
  for i in range (0,len(lista_actividades)-1):
    print("Ingrese el número de precedencias de la actividad "+lista_actividades[i+1].nombre)
    n=int(input())
    for j in range (0,n):
      print("Precedencia "+str(j+1))
      pre=input()
      for k in range (0,len(lista_actividades)):
        if pre!=lista_actividades[k].nombre:
          continue
        else:  
          pre_obj = lista_actividades[k]
          lista_precedencias.append(pre_obj)
    lista_actividades[i+1].precedencia = lista_precedencias[:]
    for t in range(0,len(lista_precedencias)):
      lista_precedencias.pop(0)
#---------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------

print("Ingrese el número de actividades del proyecto\n")
n = int(input())
llenarActividades(n)
lista_etapas=listaEtapas(n)
definirNombres()
asignarDuracion()
asignarPrecedencias()
lista_etapas[0].append(lista_actividades[0])
for i in range (1,len(lista_actividades)):
  lista_actividades[i].asignarEtapa()
  lista_etapas[lista_actividades[i].etapa].append(lista_actividades[i])
for i in range (1,len(lista_actividades)):
  lista_actividades[i].calcularInicioCercano()
  lista_actividades[i].calcularTerminoCercano()
  lista_actividades[i].calcularTerminoLejano()
  lista_actividades[i].calcularHolgura()
  lista_actividades[i].calcularInicioLejano()

for i in range (1,len(lista_actividades)):
  print("Actividad: "+lista_actividades[i].nombre)
  print("Duración: "+lista_actividades[i].duracion)
  print("Etapa: "+str(lista_actividades[i].etapa))
  print("Inicio cercano: "+str(lista_actividades[i].inicio_cercano))
  print("Término cercano: "+str(lista_actividades[i].termino_cercano))
  print("Inicio lejano: "+str(lista_actividades[i].inicio_lejano))
  print("Término lejano: "+str(lista_actividades[i].termino_lejano))
  print("Holgura: "+str(lista_actividades[i].holgura))
  print("\n")

lista_ruta_critica = rutaCritica()
print("Ruta crítica")

for i in range(1,len(lista_ruta_critica)):
  print(lista_ruta_critica[i].nombre)

print("Duración máxima del proyecto: ")
print(lista_ruta_critica[-1].termino_lejano)
