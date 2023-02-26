import turtle

#Set initial position

turtle.penup()
turtle.left (90)
turtle.fd (200)
turtle.pendown ()
turtle.right (90)

#flower base 

turtle.fillcolor ("red")
turtle.begin_fill() 
turtle.circle (10,180)
turtle.circle (25,110)
turtle.left (50)
turtle.circle (60,45) 
turtle.circle (20,170)
turtle.right (24)
turtle.fd (30)
turtle.left (10)
turtle.circle (30,110)
turtle.fd (20)
turtle.left (40) 
turtle.circle (90,70)
turtle.circle (30,150)
turtle.right (30)
turtle.fd (15) 
turtle.circle (80,90)
turtle.left (15)
turtle.fd (45)
turtle.right (165)
turtle.fd (20)
turtle.left (155)
turtle.circle (150,80) 
turtle.left (50)
turtle.circle (150,90)
turtle.end_fill()

#Petal 1

turtle.left (150) 
turtle.circle (-90,70)
turtle.left (20)
turtle.circle (75,105) 
turtle.setheading (60)
turtle.circle (80,98) 
turtle.circle (-90,40)

#Petal 2

turtle.left (180)
turtle.circle (90,40)
turtle.circle (-80,98) 
turtle.setheading (-83)

#Leaves 1 
turtle.fd (30)
turtle.left (90)
turtle.fd (25) 
turtle.left (45)
turtle.fillcolor ("green")
turtle.begin_fill()
turtle.circle (-80,90)
turtle.right (90)
turtle.circle (-80,90)
turtle.end_fill()
turtle.right (135)
turtle.fd (60)
turtle.left (180)
turtle.fd (85)
turtle.left (90)
turtle.fd (80)

#Leaves 2

turtle.right (90)
turtle.right (45)
turtle.fillcolor ("green") 
turtle.begin_fill()
turtle.circle (80,90)
turtle.left (90)
turtle.circle (80,90)
turtle.end_fill ()
turtle.left (135)
turtle.fd (60)
turtle.left (180) 
turtle.fd (60)
turtle.right (90)
turtle.circle (200,60)
turtle.done()