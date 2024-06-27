import turtle, time, random

score = 0
high_score = 0
body_segments = []
delay = .1
wn = turtle.Screen()

#Ventana
turtle.title('La Culebrita')#Título de la ventana
wn.setup(width=600, height=600)#Tamaño de la ventana
wn.bgcolor('lightgreen')#Color de la ventana

#Cabeza Serpiente
head = turtle.Turtle()
head.speed(0)#Para que se quede fija
head.shape('square')#Forma de la cabeza
head.color('green')
head.goto(0, 0)#Posición en el eje x & y
head.direction = "stop"#En espera
head.penup()#Elimina el rastro de la animación

#Comida
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)
food.direction = "stop"

#Score
text = turtle.Turtle()
text.speed(0)
text.color('White')
text.penup()
text.hideturtle()
text.goto(0, 260)
text.write(f"Score 0        High Score 0", align="center", font=("Consola", 24))

#Funciones
def mov():
    if head.direction == "Up":
        #Almacenar el valor actual de la cordenada
        y = head.ycor()
        head.sety(y + 10)

    elif head.direction == "Down":
        y = head.ycor()
        head.sety(y - 10)

    elif head.direction == "Right":
        x = head.xcor()
        head.setx(x + 10)

    elif head.direction == "Left":
        x = head.xcor()
        head.setx(x - 10)

#Almacenan el valor de la tecla presionada
def dirUp():
    head.direction = "Up"
def dirDown():
    head.direction = "Down"
def dirRight():
    head.direction = "Right"
def dirLeft():
    head.direction = "Left"

#Conectar Teclado con el programa
wn.listen()
wn.onkeypress(dirUp, "Up")
wn.onkeypress(dirDown, "Down")
wn.onkeypress(dirRight, "Right")
wn.onkeypress(dirLeft, "Left")

#Ejecución
while True:
    wn.update()

    #Colinsiones con la ventana
    if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -280:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
        #Esconder segmentos
        for segment in body_segments:
            segment.goto(1000, 1000)
        body_segments.clear()#Limpiando los segmentos despues de reiniciar

        #Actualizar score al chocar con la ventana
        score = 0        
        text.clear()
        text.write(f"Score {score}        High Score {high_score}", align="center", font=("Consola", 24))


    if head.distance(food) < 20:#Si la cabeza toca la comida:
        #Dále una posición random a la comida
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)

        #Generar cuerpo de la culebra
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape('square')
        new_segment.color('yellow')
        new_segment.penup()
        body_segments.append(new_segment)
    
        #Actualizar score
        score += 10
        if score > high_score:
            high_score = score
        
        text.clear()
        text.write(f"Score {score}        High Score {high_score}", align="center", font=("Consola", 24))

    totalSeg = len(body_segments)

    for i in range(totalSeg - 1, 0, -1):
        x = body_segments[i - 1].xcor()
        y = body_segments[i - 1].ycor()
        body_segments[i].goto(x, y)

    if totalSeg > 0:
        x = head.xcor()
        y = head.ycor()
        body_segments[0].goto(x, y)

    mov()

    #Colisiones con el propio cuerpo
    for segment in body_segments:
        if segment.distance(head) < 10:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            for segment in body_segments:#Esconder los segmentos
                segment.goto(1000, 1000)

            body_segments.clear()#Limpiando los segmentos despues de reiniciar

            score = 0        
            text.clear()
            text.write(f"Score {score}        High Score {high_score}", align="center", font=("Consola", 24))

    time.sleep(delay)


turtle.done()#Mantiene la pantalla activa

