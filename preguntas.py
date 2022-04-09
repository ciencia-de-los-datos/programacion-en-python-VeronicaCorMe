"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    
    with open( "data.csv" , "r") as file:
        datos= file.readlines()
   
    datos=[f.replace("\n", "") for f in datos]
    datos= [f.split("\t") for f in datos]
    
    columna_dos=sum([int(f[1]) for f in datos])

    return columna_dos


#Lectura de datos

def pregunta_02():
    with open("data.csv", "r") as file:
        datos2= file.readlines()
  
    datos2= [f.replace("\n","") for f in datos2]
    datos2=[f.split("\t") for f in datos2]

   #En adelante creo una lista que contenga como elementos la tupla en las columnas 1 y 2
    x=0
    lista_columna0=[]
    lista_columna0= [x[0] for x in datos2]

    id=sorted(set(lista_columna0))

    x=0
    y=0
    tupla=[(x ,lista_columna0.count(x)) for x in id]
    return tupla


    

def pregunta_03():
  """

    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ] 
  """
  #Lectura de datos

  with open("data.csv", "r") as file:
    datos3= file.readlines()
  
  datos3= [f.replace("\n","") for f in datos3]
  datos3=[f.split("\t") for f in datos3]

  
  list_columnas= [[x[0],int(x[1])] for x in datos3 ]
  list_id=sorted(set([x[0] for x in datos3]))

  c=0
  tupla2=[]

  for y in list_id:
    for x in list_columnas:
      if x[0]== y:
        c+= x[1]
      
    tupla2.append((y,c)) 
    c=0

  return tupla2


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    with open("data.csv","r") as file:
        datos4= file.readlines()
        datos4= [f.replace("\n","") for f in datos4]
        datos4= [f.split("\t") for f in datos4]
    
    list_fechas=[f[2].split("-") for f in datos4 ]
    list_meses=[f[1] for f in list_fechas]
    meses=sorted(set([f for f in list_meses]))
    tupla3=[(x, list_meses.count(x)) for x in meses]

    return tupla3



def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    with open("data.csv","r") as file:
        datos5=file.readlines()
    datos5=[f.replace("\n","")for f in datos5]
    datos5=[f.split("\t") for f in datos5]
    
    id_list=sorted(set([f[0] for f in datos5]))
    lista_datos5=[(f[0],int(f[1])) for f in datos5]
    valores=[]
    tupla4=[]

    for y in id_list:
        for x in lista_datos5:
            if x[0]== y:
                valores.append(x[1])

        tupla4.append((y, max(valores),min(valores)))
        valores.clear()  

    return tupla4


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    with open("data.csv","r") as file:
        datos6=file.readlines()
    datos6=[f.replace("\n","") for f in datos6]
    datos6=[f.split("\t") for f in datos6]
    datos6=[f[4].split(",") for f in datos6]
    
    lista_clave_valor= [(y[:3],int(y[4:]))for x in datos6 for y in x]
    keys_dict=sorted(set(elem[0] for elem in lista_clave_valor ))
    valores=[]
    tupla5=[]
    for clave in keys_dict:
        for elem in lista_clave_valor:
            if elem[0]== clave:
                valores.append(elem[1])
        tupla5.append((clave, min(valores),max(valores)))
        valores.clear()
    return tupla5


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    with open("data.csv","r") as file:
        datos7=file.readlines()
    datos7=[f.replace("\n","") for f in datos7]
    datos7=[f.split("\t") for f in datos7]
    #creo una lista de datos con elementos columna 2 y columna 1
    lista_datos=[(int(x[1]),x[0]) for x in datos7]
    #extraigo el conjunto de numeros unicos ordenados en la columna 2 de los datos
    numeros=sorted(set(x[0] for x in lista_datos))
    tupla6=[]
    letras=[]
    #para cada numero extraigo la lista letras que aparecen en la lista de datos
    for y in numeros:
        for x in lista_datos:
            if x[0]-y == 0:
                letras.append(x[1])    

        tupla6.append((y,letras))
        letras=[]
      
    
    return tupla6



def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """

    with open("data.csv","r") as file:
        datos8=file.readlines()
    datos8=[f.replace("\n","") for f in datos8]
    datos8=[f.split("\t") for f in datos8]
    #creo una lista de datos con elementos columna 2 y columna 1
    lista_datos=[(int(x[1]),x[0]) for x in datos8]
    #extraigo el conjunto de numeros unicos ordenados en la columna 2 de los datos
    numeros=sorted(set(x[0] for x in lista_datos))
    #para cada numero extraigo la lista letras que aparecen en la lista de datos, ordenada y eliminando los repetidos.
    tupla7=[]
    letras=[]
    
    for y in numeros:
        for x in lista_datos:
            if x[0]-y == 0:
                letras.append(x[1])    

        tupla7.append((y,sorted(set(letras))))
        letras=[]
      
    
    return tupla7


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    with open("data.csv","r") as file:
        datos9=file.readlines()
    datos9=[f.replace("\n","") for f in datos9]
    datos9=[f.split("\t") for f in datos9]
    datos9=[f[4].split(",") for f in datos9]
    
    #extraigo cada clave usando metodos string, recorriendo cada fila y cada elemento dentro de la fila
    lista_clave= [(y[:3])for x in datos9 for y in x]
    #creo las claves unicas ordenadas usando conjuntos (set)
    keys_dict=sorted(set( elem for elem in lista_clave ))
    #Creo una tupla contando las veces que aparece cada llave
    tupla8=[(x,lista_clave.count(x))for x in keys_dict]
    dict1=dict(tupla8)
           
    return dict1


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]

    """
    with open("data.csv", "r") as file:
        datos10=file.readlines()
    datos10=[f.replace("\n","")for f in datos10]
    datos10=[f.split("\t") for f in datos10]

    #extraigo los valores de la columna 1 y los anchos de las columnas 4 y 5 despues de dividirlas
    anc_col4=[len(f[3].split(","))for f in datos10]
    anc_col5=[len(f[4].split(",")) for f in datos10]
    col1=[(f[0]) for f in datos10]
    
    #uno los datos de cada fila usando zip
    data_base= list(zip(col1,anc_col4,anc_col5))
    
    return data_base



def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    with open("data.csv", "r") as file:
        datos11=file.readlines()
    datos11=[f.replace("\n","")for f in datos11]
    datos11=[f.split("\t") for f in datos11]

    #extraigo los valores de la columna 2 y  4 despues de dividirlas
    col4=[f[3].split(",")for f in datos11]
    col1=[int(f[1]) for f in datos11]
    #Creo mis datos como una lista que empareja la columna 4 y la 2
    datos_letras_numero=list(zip(col4,col1))
    #asigno a cada letra el valor que se le asocia en la columna 2 mediante una lista
    lista_letra_num=[]
    c=0
    for elem in datos_letras_numero:
        for y in elem[c]:
            lista_letra_num.append((y,elem[1]))
            c += 1
        c=0
    
    #Creo el diccionario
    dict2={}

    for llave,valor in lista_letra_num:
        if llave in dict2.keys():
            dict2[llave] +=valor
        else:
            dict2[llave] =valor

    #ordeno el diccionario
    sorted_keys=sorted(dict2)
    dict2_sort={}
    for x in sorted_keys:
        dict2_sort[x]=dict2[x]

    return dict2_sort


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    with open("data.csv", "r") as file:
        datos12=file.readlines()
    datos12=[f.replace("\n","")for f in datos12]
    datos12=[f.split("\t") for f in datos12]

    #extraigo los valores de la columna 1 y  5 despues de dividirlas
    col5=[f[4].split(",")for f in datos12]
    col1=[(f[0]) for f in datos12]
    datos_letras=list(zip(col1,col5))

    dict3_keys=sorted(set(col1))
    #Creo mis datos como una lista que empareja la columna 1 y la 5
    #creo diccionario con llaves ordenadas
    dict3={}
    for llave in dict3_keys:  
        dict3[llave]= 0
    #sumo valores en el diccionario
    for x, y in datos_letras:
       for z in y:
           dict3[x]+= int(z[4:])
         
    return dict3

