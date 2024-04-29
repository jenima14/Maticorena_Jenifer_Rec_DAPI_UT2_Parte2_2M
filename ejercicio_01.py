import csv

def process_class(ruta):
    '''
    Lee los datos y los almacena en una lista de diccionarios
    donde en cada uno de los alumnos las claves serán los datos
    de la cabecera del archivo CSV y los valores serán los datos
    de cada alumno/a.
    Parámetro ruta: un str con la ruta del fichero(.csv) a abrir
    return: None
    '''
    alumnado = []
    with open(ruta, newline='', encoding="UTF-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for fila in reader:
            alumnado.append(fila)
    return alumnado

x = (process_class("class.csv"))

lista1 =[]
lista2 =[]
for i in x:
    nombres = i.get("Nombre")
    apellidos = i.get("Apellido")
    lista1.append(nombres)
    lista2.append(apellidos)

def create_email(nombres, apellidos):
    '''
    recibirá el nombre y apellido de cada alumno/a y devolverá
    una dirección de correo en el dominio de Educación Navarra.
    Parámetros de entrada: la función tendrá dos str con el nombre
    y el apellido de cada alumno/a.
    Salida: deberá concatenar la 1ra letra del nombre con las
    5 primeras letras del apellido y el dominio de educación “@educacion.navarra.es”
    '''

    for o,u in zip(nombres, apellidos):
        print(f"{str(o[0])}{u[0:5]}@educacion.navarra.es")

create_email(lista1, lista2)