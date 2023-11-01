import turtle

rozmiar_ukladu = 500
rozmiar_strzalki = rozmiar_ukladu / 10
rozmiar_znaczka = rozmiar_ukladu / 100
skala = 20

t = turtle.Turtle()
t.shape('circle')
t.shapesize(0.01,0.01)
t.speed(2000)
t.color('black')

t.up()
#Oś X
t.goto(-rozmiar_ukladu,0)
t.down()
t.goto(rozmiar_ukladu,0)
t.lt(150)
t.fd(rozmiar_strzalki)
t.backward(rozmiar_strzalki)
t.lt(60)
t.fd(rozmiar_strzalki)
#Oś y
t.up()
t.goto(0,-rozmiar_ukladu)
t.down()
t.goto(0,rozmiar_ukladu)
t.lt(30)
t.fd(rozmiar_strzalki)
t.backward(rozmiar_strzalki)
t.lt(60)
t.fd(rozmiar_strzalki)
#Wracamy do 0,0
t.up()
t.goto(0,0)
t.lt(60)
#Rysujemy skalę dla X
t.goto(-rozmiar_ukladu,0)
t.down()
for i in range(0,int((2*rozmiar_ukladu - rozmiar_strzalki) / skala)):
    t.lt(90)
    t.fd(rozmiar_znaczka)
    t.backward(2*rozmiar_znaczka)
    t.fd(rozmiar_znaczka)
    t.rt(90)
    t.fd(skala)
#Rysujemy skalę dla Y
t.up()
t.goto(0,-rozmiar_ukladu)
t.down()
t.lt(90)
for i in range(0,int((2*rozmiar_ukladu - rozmiar_strzalki) / skala)):
    t.lt(90)
    t.fd(rozmiar_znaczka)
    t.backward(2*rozmiar_znaczka)
    t.fd(rozmiar_znaczka)
    t.rt(90)
    t.fd(skala)   

turtle.mainloop()
