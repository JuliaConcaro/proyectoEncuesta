#Presentación y comiienzo de la encuesta
print ("Presentación: Hola, mi nombre es Nombre y lo llamo de la Consultora para hacerle una encuesta sobre distintas cuestiones de UnidadTerritorial. ¿Me daría unos minutos?")
print ("Escriba 1 en caso de respuesta afirmativa y 0 en caso de negativa.")

while True:
    respuesta = input ()
    if respuesta == "1":
        break 
    elif respuesta == "0":
        raise ValueError ('La respuesta debe ser afirmativa para proceder')
    elif respuesta != "1" or respuesta != "0":
        print ('Debe ingresar uno de los dos dígitos para proceder')

#Primer filtro
print ("¿Usted es argentinx y vive y vota en UnidadTerritorial? De ser así, escribir 1. Sino, escribir 0")

while True:
    respuesta = input ()
    if respuesta == "1":
        break 
    elif respuesta == "0":
        raise ValueError ('La respuesta debe ser afirmativa para proceder')
    elif respuesta != "1" or respuesta != "0":
        print ('Debe ingresar uno de los dos dígitos para proceder')

#Segundo filtro
print ("¿Me podría indicar su edad?")

while True:
    try:
        edad= int(input('Ingrese un número'))
        break
    except:
        print ("Debe ingresar un número")


if edad < 16:
    assert (edad > 16 and edad <75), "No podremos realizarle la encuesta"
    try: 
        print (edad)
    except AssertionError as mensaje:
        print (mensaje)
elif edad >= 16 and edad <= 75:
    edad_entrevistadx=edad
    print ("Siguiente pregunta")
elif edad > 75:
    assert (edad > 16 and edad <75), "No podremos realizarle la encuesta"
    try: 
        print (edad)
    except AssertionError as mensaje:
        print (mensaje)

#Género de lx entrevistadx
print ("Seleccione el género de lx entrevistadx")

genero = ["1) Mujer", "2) Varón", "3) Otro"]
for i in genero:
    print (i)

digit = int(input())
genero_entrevistadx=genero[digit-1]

while True:
    if digit == 1 or digit == 2 or digit == 3:
        break
    elif digit != 1 or digit != 2 or digit != 3:
        print ("Debe ingresar uno de los 3 dígitos para proceder")

#Localidad en que vota
print ("Seleccione la localidad en que vota lx entrevistadx")
#Buscar cómo poner comillas dentro de un string.
localidades= ["1) Localidad1", "2) Localidad2", "3) Localidad3"]
for i in localidades:
    print (i)

digit = int(input())
localidad_entrevistadx=localidades[digit-1]

while True:
    if digit == 1 or digit == 2 or digit == 3:
        break
    elif digit != 1 or digit != 2 or digit != 3:
        print ("Debe ingresar uno de los 3 dígitos para proceder")

#Nivel de estudios
print ("¿Cuál es su máximo nivel de estudios?")

nivelDeEstudios= ["1) Sin estudios", "2) Primarios incompletos", "3) Primarios completos", "4) Primarios completos", "5) Secundarios incompletos", "6) Secundarios completos", "7) Universitarios/Terciarios incompletos", "8) Universitarios/Terciarios completos"]

for i in nivelDeEstudios:
    print (i)

digit = int(input())
estudios_entrevistadx=nivelDeEstudios[digit-1]

while True:
    if digit == 1 or digit == 2 or digit == 3 or digit == 4 or digit == 5 or digit == 6 or digit == 7 or digit == 8:
        break
    elif digit != 1 or digit != 2 or digit != 3 or digit != 4 or digit != 5 or digit != 6 or digit != 7 or digit != 8:
        print ("Debe ingresar uno de los 8 dígitos para proceder")

#Evaluación de la gestión del Presidente
print ("¿Cómo evaluaría la gestión de NombrePresidente desde que asumió como Presidente hasta el día de hoy?")

vordinalEvaluacionGP= ["1) Muy buena", "2) Buena", "3) Regular", "4) Mala", "5) Muy mala"]

for i in vordinalEvaluacionGP:
    print (i)

digit = int(input())
evaluacionGP_entrevistadx=vordinalEvaluacionGP[digit-1]

while True:
    if digit == 1 or digit == 2 or digit == 3 or digit == 4 or digit == 5:
        break
    elif digit != 1 or digit != 2 or digit != 3 or digit != 4 or digit != 5:
        print ("Debe ingresar uno de los 5 dígitos para proceder")

#Imagen de dirigentes
print ("Ahora le voy a preguntar cuál es su imagen, si es que tiene alguna, sobre lxs siguientes dirigentes políticxs")

dirigentesImg= ["Dirigente1", "Dirigente2", "Dirigente3"]
vordinal= ["1) Muy buena", "2) Buena", "3) Regular buena", "4) Regular mala", "5) Mala", "6) Muy mala"]

#ImgDirigente1
print (dirigentesImg[0])
for i in vordinal:
    print (i)
while True:
    if digit == 1 or digit == 2 or digit == 3 or digit == 4 or digit == 5 or digit == 6:
        break
    elif digit != 1 or digit != 2 or digit != 3 or digit != 4 or digit != 5 or digit != 6:
        print ("Debe ingresar uno de los 6 dígitos para proceder")
digit= int(input())
opinionDirigente1=vordinal[digit-1]

#ImgDirigente2
print (dirigentesImg[1])
for i in vordinal:
    print (i)
while True:
    if digit == 1 or digit == 2 or digit == 3 or digit == 4 or digit == 5 or digit == 6:
        break
    elif digit != 1 or digit != 2 or digit != 3 or digit != 4 or digit != 5 or digit != 6:
        print ("Debe ingresar uno de los 6 dígitos para proceder")
digit= int(input())
opinionDirigente2=vordinal[digit-1]

#ImgDirigente3
print (dirigentesImg[2])
for i in vordinal:
    print (i)
while True:
    if digit == 1 or digit == 2 or digit == 3 or digit == 4 or digit == 5 or digit == 6:
        break
    elif digit != 1 or digit != 2 or digit != 3 or digit != 4 or digit != 5 or digit != 6:
        print ("Debe ingresar uno de los 6 dígitos para proceder")
digit= int(input())
opinionDirigente3=vordinal[digit-1]

#Elecciones a Presidente
print ("Si hoy fueran las elecciones a Presidente, ¿Ud. votaría por...?")

candidatxsP= ["1) Candidatx1", "2) Candidatx2", "3) Candidatx3", "4) Otrxs", "5) Votaría en blanco, anulado o impugnado", "6) No sabe/No contesta"]

for i in candidatxsP:
    print (i)

digit = int(input())
votoP_entrevistadx=candidatxsP[digit-1]

if votoP_entrevistadx == candidatxsP[3]:
    print ("A continuación escriba lx candidatx no mencionadx en la lista a quien votaría")
    votoOtrxsP_entrevistadx=(input())
elif votoP_entrevistadx == candidatxsP[5]:
    print ("Y aunque todavía no lo tenga definido, ¿a quién es más probable que vote?")
    for i in candidatxsP:
        print (i)
    
    digit = int(input())
    votoNoDefinidoP_entrevistadx=candidatxsP[digit-1]

while True:
    if digit == 1 or digit == 2 or digit == 3 or digit == 4 or digit == 5 or digit == 6:
        break
    elif digit != 1 or digit != 2 or digit != 3 or digit != 4 or digit != 5 or digit != 6:
        print ("Debe ingresar uno de los 6 dígitos para proceder")

#Escenario de ballotage
print ("Si hubiera un ballotage entre estxs dos candidatxs, ¿a quién votaría?")

candidatxsPBallo= ["1) Candidatx1", "2) Candidatx2"]

for i in candidatxsPBallo:
    print (i)

digit = int(input())
votoPBallo_entrevistadx=candidatxsPBallo[digit-1]

if votoPBallo_entrevistadx == candidatxsPBallo[0]:
    print ("¿Podría decirnos por qué decidiría votar lx Candidatx1 antes que a lx Candidatx2?")
    razonVoto1PBallo=(input())
elif votoPBallo_entrevistadx == candidatxsPBallo[1]:
    print ("¿Podría decirnos por qué decidiría votar lx Candidatx2 antes que a lx Candidatx1?")
    razonVoto2PBallo=(input())

while True:
    if digit == 1 or digit == 2:
        break
    elif digit != 1 or digit != 2:
        print ("Debe ingresar uno de los 2 dígitos para proceder")

#Voto anterior
print ("¿Podría decirnos a quién votó en las útlimas elecciones a Presidente?")

candidatxsEleccionesPasadas= ["1) Candidatx1", "2) Candidatx2", "3) Candidatx3"]

for i in candidatxsEleccionesPasadas:
    print (i)

digit = int(input())
votoAnterior_entrevistadx=candidatxsEleccionesPasadas[digit-1]

while True:
    if digit == 1 or digit == 2:
        break
    elif digit != 1 or digit != 2:
        print ("Debe ingresar uno de los 2 dígitos para proceder")

#Nombre de lx entrevistadx
print ("¿Me podría dar un nombre o un apodo suyo?")
nombre_entrevistadx=input()

#Finalización de la encuesta
print ("Muchas gracias por su tiempo. Ha finalizado la encuesta.")