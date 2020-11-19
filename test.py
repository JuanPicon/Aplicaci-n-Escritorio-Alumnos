#Robin Gonzalez Castro A01352066
Puntos = []

def suma():
        if answer == 'A':
            print("10 puntos\n")
            Puntos.append(10)
        elif answer == 'B':
            print("5 puntos\n")
            Puntos.append(5)
        elif answer == 'C':
            print("3 puntos\n")
            Puntos.append(3)
        elif answer == 'D':
            Puntos.append(1)
            print("1 puntos\n")
        else:
            print("Opción incorrecta\n")
    
def sumalista():
    laSuma = 0
    for i in Puntos:
        laSuma = laSuma + i
    print(laSuma,"puntos en total\n")
    
    if laSuma <= 150 and laSuma >= 100:
        print("Baja probabilidad de contagio, procura seguir como antes  y no asistir a las sesiones híbridas.")
    elif laSuma <= 99 and laSuma >= 50:
        print("Habria que cuidarse mas, trata de tomar más precauciones y avisa sobre cualquier malestar")
    elif laSuma <=49 and laSuma >=15 :
        print("No te ha importado tu salud, ni la de otros, hay alta probabilidad con causas de contraer la enfermedad, trata de tomar tus precauciones y necesitas realizar chequeos con tu médico.")
    print( "Gracias por su tiempo!\n")
#Empieza el programa
print("TEST")
#Pregunta 1
answer = ""
while answer != "A" and answer != "B" and answer != "C" and answer != "D":
    print("Escoger una de las siguientes opciónes")
    print("Si = A | Frecuentemente = B | Rara vez =  C | No = D")
    answer = input("¿Te realizas chequeos clinicos con frecuencia?\n")
    suma()
#Pregunta 2
answer = ""    
while answer != "A" and answer != "B" and answer != "C" and answer != "D":
    print("Escoger una de las siguientes opciónes")
    print("Si = A | Frecuentemente = B | Rara vez =  C | No = D")
    answer = input("¿Te has realizado la prueba de covid-19?\n")
    suma()
#Pregunta 3
answer = ""    
while answer != "A" and answer != "B" and answer != "C" and answer != "D":
    print("Escoger una de las siguientes opciónes")
    print("Si = A | Frecuentemente = B | Rara vez =  C | No = D")
    answer = input("¿Sanitizar tu teléfono y manos frecuentemente?\n")
    suma()
#Pregunta 4
answer = ""    
while answer != "A" and answer != "B" and answer != "C" and answer != "D":
    print("Escoger una de las siguientes opciónes")
    print("Si = A | Frecuentemente = B | Rara vez =  C | No = D")
    answer = input("¿Consideras que tienes una vida saludable para combatir enfermedades?\n")
    suma()
#Pregunta 5
answer = ""    
while answer != "A" and answer != "B" and answer != "C" and answer != "D":
    print("Escoger una de las siguientes opciónes")
    print("Si = A | Frecuentemente = B | Rara vez =  C | No = D")
    answer = input("¿Comes frutas y verduras por lo menos dos veces al día?\n")
    suma()
#Pregunta 6
answer = ""    
while answer != "A" and answer != "B" and answer != "C" and answer != "D":
    print("Escoger una de las siguientes opciónes")
    print("Si = A | Frecuentemente = B | Rara vez =  C | No = D")
    answer = input("¿No sale de su hogar aunque tenga necesidad?\n")
    suma()
#Pregunta 7
answer = ""    
while answer != "A" and answer != "B" and answer != "C" and answer != "D":
    print("Escoger una de las siguientes opciónes")
    print("Si = A | Frecuentemente = B | Rara vez =  C | No = D")
    answer = input("¿Considera que has respetado los días de cuarentena en su casa?\n")
    suma()
#Pregunta 8
answer = ""    
while answer != "A" and answer != "B" and answer != "C" and answer != "D":
    print("Escoger una de las siguientes opciónes")
    print("Si = A | Frecuentemente = B | Rara vez =  C | No = D")
    answer = input("¿Se ha alejado de personas infectadas de covid-19?\n")
    suma()
#Pregunta 9
answer = ""    
while answer != "A" and answer != "B" and answer != "C" and answer != "D":
    print("Escoger una de las siguientes opciónes")
    print("Si = A | Frecuentemente = B | Rara vez =  C | No = D")
    answer = input("¿No ha tenido síntomas como tos seca o temperatura en estos días?\n")
    suma()
#Pregunta 10
answer = ""    
while answer != "A" and answer != "B" and answer != "C" and answer != "D":
    print("Escoger una de las siguientes opciónes")
    print("Si = A | Frecuentemente = B | Rara vez =  C | No = D")
    answer = input("¿Haces regularmente ejercicio?\n")
    suma()
#Pregunta 11
answer = ""    
while answer != "A" and answer != "B" and answer != "C" and answer != "D":
    print("Escoger una de las siguientes opciónes")
    print("Si = A | Frecuentemente = B | Rara vez =  C | No = D")
    answer = input("¿No te consideras una persona sedentaria?\n")
    suma()
#Pregunta 12
answer = ""    
while answer != "A" and answer != "B" and answer != "C" and answer != "D":
    print("Escoger una de las siguientes opciónes")
    print("Si = A | Frecuentemente = B | Rara vez =  C | No = D")
    answer = input("¿Haces regularmente ejercicio?\n")
    suma()
#Pregunta 13
answer = ""    
while answer != "A" and answer != "B" and answer != "C" and answer != "D":
    print("Escoger una de las siguientes opciónes")
    print("Si = A | Frecuentemente = B | Rara vez =  C | No = D")
    answer = input("¿Tienes que tomar medicamentos por alguna enfermedad?\n")
    suma()
#Pregunta 14
answer = ""    
while answer != "A" and answer != "B" and answer != "C" and answer != "D":
    print("Escoger una de las siguientes opciónes")
    print("Si = A | Frecuentemente = B | Rara vez =  C | No = D")
    answer = input("¿Has padecido de alguna otra enfermedad en estos días?\n")
    suma()
sumalista()  