from turtle import*


#we want to paint a house
#step 1. draw a square
speed(30)
width(7)
color("orange")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door

forward(70)
color("yellow")
left(90)
forward(120)    #height of the door
right(90)
forward(60)
right(90)
forward(120)

penup()
goto(200,200)
pendown()

color ("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(15,100)
pendown()

right(150)
forward(75)
right(90)
forward(35) 
right(90)
forward(75)
right(90)
forward(35)

penup()
goto(150,100)
pendown()

right(180)
forward(35)
left(90)
forward(75)
left(90)
forward(35)
left(90)
forward(75)

exitonclick()