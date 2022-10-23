#pong game 
WIDTH = 800
HEIGHT = 600
brzinay = 0.1
brzinax = 0.1

import turtle
import winsound
window = turtle.Screen()
window.bgcolor("Black")
window.setup(width = WIDTH, height = HEIGHT)
turtle.title("Pong na Maro :)")
window.tracer(0)
#Poeni
poeni_a = 0
poeni_b = 9
#Palka A
palka_a = turtle.Turtle()
palka_a.speed(0)
palka_a.shape("square")
palka_a.color("white")
palka_a.shapesize(stretch_wid=5, stretch_len=1)
palka_a.penup()
palka_a.goto (-350,0)

#Palka B
palka_b = turtle.Turtle()
palka_b.speed(0)
palka_b.shape("square")
palka_b.color("white")
palka_b.shapesize(stretch_wid=5, stretch_len=1)
palka_b.penup()
palka_b.goto (350,0)
#topka
topka = turtle.Turtle()
topka.speed(0)
topka.shape("circle")
topka.color("white")
topka.shapesize(stretch_wid=1, stretch_len=1)
topka.penup()
topka.goto (0,0)
topka.dx = brzinax
topka.dy = brzinay
#penkalo 
penkalo = turtle.Turtle()
penkalo.speed(0)
penkalo.color("white")
penkalo.penup()
penkalo.hideturtle()
penkalo.goto (0,260)
penkalo.write(f"Играч A: {poeni_a}   Играч Б: {poeni_b}", align="center", font = ("Courier",24, "normal"))
#Funkcii
def palka_a_gore():
    y = palka_a.ycor()
    y += 20
    palka_a.sety(y)
def palka_a_dole():
    y = palka_a.ycor()
    y -= 20
    palka_a.sety(y)
def palka_b_gore():
    y = palka_b.ycor()
    y += 20
    palka_b.sety(y)
def palka_b_dole():
    y = palka_b.ycor()
    y -= 20
    palka_b.sety(y)

#tastatura
window.listen()
window.onkeypress(palka_a_gore, "w")
window.onkeypress(palka_a_dole, "s")
window.onkeypress(palka_b_gore, "i")
window.onkeypress (palka_b_dole, "k")

#Main loop tuka
while True: 
    window.update()
    #Dvizenje na topka
    topka.setx(topka.xcor() + topka.dx)
    topka.sety(topka.ycor()+ topka.dy)
    #Proverka za granici 
    if topka.ycor() > 290:
        topka.sety(290)
        topka.dy *= -1
        
    if topka.ycor() < -290:
        topka.sety(-290)
        topka.dy *= -1
        
    if topka.xcor() > 390:
        topka.goto(0, 0)
        topka.dx *=-1
        poeni_a+=1
        penkalo.clear()
        penkalo.write(f"Играч A: {poeni_a}   Играч Б: {poeni_b}", align="center", font = ("Courier",24, "normal"))
    if topka.xcor() < -390:
        topka.goto(0, 0)
        topka.dx *=-1
        poeni_b +=1
        penkalo.clear()
        penkalo.write(f"Играч A: {poeni_a}   Играч Б: {poeni_b}", align="center", font = ("Courier",24, "normal"))

    # sudar na topka i palka
    if topka.xcor() > 340 and topka.xcor() < 350 and (topka.ycor() < palka_b.ycor() + 40 and topka.ycor() > palka_b.ycor()-40):
        topka.setx(340)
        topka.dx *= -1
        
        
    if topka.xcor() < -340 and topka.xcor() > - 350 and (topka.ycor() < palka_a.ycor() + 40 and topka.ycor() > palka_a.ycor()-40):
        topka.setx(-340)
        topka.dx *= -1
        
    #Granici za igraci
    if palka_a.ycor() > 250:
        palka_a.goto (-350,250)
    if palka_a.ycor() < -250:
        palka_a.goto (-350,-250)
    if palka_b.ycor() > 250:
        palka_b.goto (350,250)
    if palka_b.ycor() < -250:
        palka_b.goto (350,-250)

    #Pobednik 
    if poeni_a == 10:
        pobednik = turtle.Turtle()
        pobednik.speed(0)
        pobednik.color('white')
        pobednik.penup()
        pobednik.goto(0,0)
        pobednik.write(f"Победникот е играч A", align="center", font = ("Courier",30, "normal"))
        
    if poeni_b == 10:
        pobednik = turtle.Turtle()
        pobednik.speed(0)
        pobednik.color('white')
        pobednik.penup()
        pobednik.goto(0,0)
        pobednik.write(f"Победникот е играч Б", align="center", font = ("Courier",30, "normal"))
        



    

        




