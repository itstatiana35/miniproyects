import random
import turtle
import time

posponer = 0.1

#Marcador 
score = 0
high_score = 0

#Configuracion de la ventana
wn = turtle.Screen()
wn.title("tati's snake")
wn.bgcolor("black")
wn.setup(width = 600, height = 600)
wn.tracer(0)

#Cabeza de la serpiente
cabeza = turtle.Turtle()
cabeza.penup()
cabeza.speed(0)
cabeza.shape("square")
cabeza.direction = "stop"
cabeza.color("white")
cabeza.goto(0, 0)

#Comida
comida = turtle.Turtle()
comida.penup()
comida.speed(0)
comida.shape("circle")
comida.direction = "stop"
comida.color("red")
comida.goto(0, 100)

#texto
texto = turtle.Turtle()
texto.speed(0)
texto.penup()
texto.color("white")
texto.hideturtle()
texto.goto(0, 260)
texto.write("Score: 0       High Score: 0", align = "center", font = ("Arial", 24, "normal"))

#Cuerpo de la serpiente
segmentos = []

#Funciones

def arriba():
    cabeza.direction = "up"

def abajo():
    cabeza.direction = "down"

def derecha():
    cabeza.direction = "right"

def izquierda():
    cabeza.direction = "left"

def mov():
    if cabeza.direction == "up":
        y = cabeza.ycor()
        cabeza.sety(y + 20)

    if cabeza.direction == "down":
        y = cabeza.ycor()
        cabeza.sety(y - 20)

    if cabeza.direction == "right":
        x = cabeza.xcor()
        cabeza.setx(x + 20)

    if cabeza.direction == "left":
        x = cabeza.xcor()
        cabeza.setx(x - 20)

#Teclado
wn.listen()
wn.onkeypress(arriba, "Up")
wn.onkeypress(abajo, "Down")
wn.onkeypress(izquierda, "Left")
wn.onkeypress(derecha, "Right")

#Bucle
while True:

    wn.update()

    #Colisiones bordes
    if cabeza.xcor() > 280 or cabeza.xcor() < -290 or cabeza.ycor() > 280 or cabeza.ycor() < -280:
        time.sleep(0.75)
        cabeza.goto(0,0)
        cabeza.direction = "stop"

        #Esconder segmento
        for segmento in segmentos:
            segmento.goto(1000, 1000)

        #limpiar lista de segmentos
        segmentos.clear()

        #Resetear score
        score = 0
        texto.clear()   
        texto.write("Score: {}      High Score: {}".format(score, high_score), 
                align = "center", font =("Arial", 24, "normal"))

        #Resetear comida
        comida.clear()
        comida.goto(0, 100)


    #Colisiones comida
    if cabeza.distance(comida) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 240)
        comida.goto(x, y)

        nuevo_segmento = turtle.Turtle()
        nuevo_segmento.speed(0)
        nuevo_segmento.shape("square")
        nuevo_segmento.penup()
        nuevo_segmento.color("grey")
        segmentos.append(nuevo_segmento)


        #aumentar marcador
        score += 1
        if score > high_score:
            high_score = score

        texto.clear()   
        texto.write("Score: {}      High Score: {}".format(score, high_score), 
                align = "center", font =("Arial", 24, "normal"))

    #Colisiones con el cuerpo
    for segmento in segmentos:
        if segmento.distance(cabeza) < 20:
            time.sleep
            cabeza.goto(0,0)
            cabeza.direction = "stop"

            #Esconder los segmentos
            for segmento in segmentos:
                segmento.goto(1000,1000)

            segmentos.clear()

            #Resetear score
            score = 0
            texto.clear()   
            texto.write("Score: {}      High Score: {}".format(score, high_score), 
                align = "center", font =("Arial", 24, "normal"))

             #Resetear comida
            comida.clear()
            comida.goto(0, 100)


    #Mover la serpiente
    totalSeg = len(segmentos)
    for index in range(totalSeg -1, 0, -1):
        x = segmentos[index - 1].xcor()
        y = segmentos[index - 1].ycor()
        segmentos[index].goto(x,y)

    if totalSeg > 0:
         x = cabeza.xcor()
         y = cabeza.ycor()
         segmentos[0].goto(x,y)

    mov()
    time.sleep(posponer)