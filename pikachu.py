import turtle
turtle.Screen().bgcolor('DARKMAGENTA') # BACKGROUND

t = turtle.Turtle()
t.speed(20)
t.up()

t.fillcolor('YELLOW')  #main
t.begin_fill()         #main

t.setpos(-73 , 33)  # staring from left
t.down()
#t.fd(20)
t.right(54)
t.circle(50 , -67)
t.right(170)
t.circle(70 , 14)
t.right(170)
t.circle(50 , -55)
t.up()

t.setpos(-55 , 143)  # from left ear to right cheek
t.down()
#t.fd(20)
t.right(-120)
t.circle(150 , -45)
t.right(120)
t.circle(150 , -45)
t.right(-62)
t.circle(200 , -30)
t.right(-60)
t.circle(150 , -45)
t.right(120)
t.circle(150 , -45)
t.right(-110)
t.circle(80 , -30)
t.right(190)
t.circle(70 , 25)
t.right(170)
t.circle(30 , -80)
t.right(-10)
t.circle(100 , -20)
t.up()

t.setpos(67 , 11)           # right hand
t.down()
t.right(-90)
#t.circle(200 , 4)
#t.up()


#t.setpos(70 , -2)
#t.down()
#t.seth(-250)
t.circle(100 , -67)
t.right(145)
t.fd(8)
t.right(180)
t.circle(3 , -180)
t.right(130)
t.fd(4)
t.left(110)
t.fd(4)
t.right(160)
t.circle(3 , -145)
t.right(190)
t.fd(4)
t.right(235)
t.fd(4)
t.right(180)
t.circle(3 , -160)
t.right(180)
t.fd(4)
t.right(220)
t.fd(6)
t.right(200)
t.circle(3 , -160)
t.right(180)
t.fd(6)
t.right(200)
t.fd(9)
t.right(220)
t.circle(3 , -180)
t.right(60)
t.fd(0.5)
t.right(175)
t.circle(100 , -40)
t.up()

t.setpos(65 , -80)          # right thigh
t.down()
t.right(270)
t.fd(8)
t.right(180)
t.circle(50 , -30)
t.up()

t.setpos(72 , -130)         # right leg
t.down()
t.right(232)
t.circle(100 , -30)
t.circle(2 , -180)
t.right(160)
t.fd(17)
t.right(180)
t.fd(21)
t.right(180)
t.circle(2 , -180)
t.right(180)
t.fd(20)
t.right(180)
t.fd(19)
t.right(180)
t.circle(2 , -180)
t.right(340)
t.circle(100 , -45)
t.circle(5 , - 150)
t.right(170)
t.fd(8)
t.up()

t.setpos(63 , -150)         # lower part to left leg
t.down()
t.right(250)
t.fd(20)
t.right(25)
t.circle(100 , 30)
t.right(0)
t.circle(60 , 25)
t.right(97)
t.circle(6 , -170)
t.right(0)
t.circle(100 , -40)
t.right(-10)
t.circle(3 , -200)
t.right(157)
t.fd(15)
t.right(180)
t.fd(17)
t.right(180)
t.circle(3 , -200)
t.right(157)
t.fd(17)
t.right(180)
t.fd(15)
t.right(180)
t.circle(3 , -180)
t.right(343)
t.circle(100 , -40)
t.right(30)
t.circle(6 , -140)
t.right(270)
t.circle(75 , -30)
t.circle(30 , -70)
t.right(-10)
t.circle(80 , -30)
t.right(165)
t.circle(130 , 19)
t.up()

t.setpos(-68 , -35)         # left hand
t.down()
t.right(120)
t.circle(100 , -65)
t.right(-10)
t.fd(3)
t.right(-50)
t.end_fill()               #main

t.fillcolor('YELLOW')      #main
t.begin_fill()             #main

t.circle(2 , -200)
t.right(180)
t.fd(5)
t.right(215)
t.fd(5)
t.right(180)
t.circle(2 , -180)
t.right(150)
t.fd(5)
#t.right(215)
t.right(195)
t.fd(10)
t.right(180)
t.circle(3, -180)
t.right(180)
t.fd(10)
t.right(195)
t.fd(10)
t.right(180)
t.circle(3 , -180)
t.right(180)
t.fd(10)
t.right(130)
t.circle(20 , -30)
t.right(-33)
t.circle(80 , -50)
t.end_fill()               #main
t.up()

t.fillcolor('BLACK')       #main
t.begin_fill()             #main

t.setpos(70 , 90)           # right eye
t.down()
t.circle(15 , 360)
t.end_fill()               #main
t.up()

t.fillcolor('WHITE')       #main
t.begin_fill()             #main

t.setpos(60 , 92)           # right pupil
t.down()
t.circle(7 , 360)
t.end_fill()               #main
t.up()


t.fillcolor('BLACK')       #main
t.begin_fill()             #main

t.setpos(-23 , 100)         # left eye
t.down()
t.circle(15 , 360)
t.end_fill()               #main
t.up()


t.fillcolor('WHITE')       #main
t.begin_fill()             #main

t.setpos(-27.5 , 102.5)
t.down()
t.circle(7 , 360)
t.end_fill()               #main
t.up()


t.setpos(15 , 70)           #left pupil
t.down()
#t.fd(20)
t.right(20)
t.circle(3 , -180)

t.fillcolor('BLACK')        # nose
t.begin_fill()
t.right(0)
t.circle(2 , 180)
t.end_fill()
t.up()


t.setpos(10 , 70)           # lip(right)
t.down()
t.right(90)
t.fd(6)
t.up()

#t.fillcolor('DARKRED')
#t.begin_fill()
t.setpos(10 , 60)           # lip(left)
t.down()
t.right(30)
t.circle(35 , 50)
#t.end_fill()
t.up()

t.fillcolor('DARKRED')     #main
t.begin_fill()             #main

t.setpos(10 , 60)           # mouth
t.down()
t.right(-30)
t.circle(35 , -50)
t.end_fill()               #main
t.up()


t.fillcolor('DARKRED')     #main
t.begin_fill()             #main

t.setpos(32 , 50)           # mouth
t.down()
#t.fd(20)
t.right(250)
t.circle(40 , -75)
t.right(47)
t.circle(40 , -75)
t.end_fill()               #main
t.up()

t.fillcolor('HOTPINK')     #main  IF COLOR IS NOT MATCH THEN ADD ANOTHER CIRCLE LAYER AND COLOR
t.begin_fill()             #main

t.setpos(-16 , 40)          # tounge
t.down()
#t.fd(20)
t.right(48)
t.circle(40 , -70)
t.right(63)
t.circle(40 , -55)
t.right(48)
t.circle(40 , -57)
t.end_fill()               #main
t.up()

t.fillcolor('RED')         #main
t.begin_fill()             #main

t.setpos(-77 , 43)          #cheek dot
t.down()
t.right(-40)
t.circle(17 , 360)
#t.right(-21)
#t.circle(45 , 25)
t.end_fill()               #main
t.up()

t.fillcolor('RED')         #main
t.begin_fill()             #main


t.setpos(93 , 42)
t.down()
t.right(-120)
t.circle(17 , -360)
#t.right(10)
#t.circle(30 , -31)
t.end_fill()               #main
t.up()

t.fillcolor('YELLOW')      #main
t.begin_fill()             #main

t.setpos(-86 , -80)        #tail(lower)
t.down()
t.right(-70)
t.fd(10)
t.right(110)
t.fd(20)
t.right(-50)
t.fd(30)
t.right(-70)
t.fd(30)
t.right(90)
t.fd(13)
t.right(115)
t.circle(90 , -20)
t.right(55)
t.fd(60)
t.right(-110)
t.fd(50)
t.right(110)
t.fd(40)
t.right(-100)
t.fd(35)
t.right(-96)
t.fd(14)
t.end_fill()               #main
t.up()

t.fillcolor('YELLOW')      #main
t.begin_fill()             #main

t.setpos(-115 , 23)          #tail(upper)
t.down()
t.right(-93)
t.fd(140)
t.right(-90)
t.circle(200 , -25)
t.right(63)
t.circle(500 , -16.5)
t.right(-90)
t.circle(50 , 67)
t.right(119.3)
t.fd(44)
t.end_fill()               #main
t.up()

t.setpos(-68 , -35)         # left hand
t.down()
t.right(-143)
t.circle(100 , -65)
t.right(-10)
t.fd(3)
t.right(-50)
t.end_fill()               #main

t.fillcolor('YELLOW')      #main
t.begin_fill()             #main

t.circle(2 , -200)
t.right(180)
t.fd(5)
t.right(215)
t.fd(5)
t.right(180)
t.circle(2 , -180)
t.right(150)
t.fd(5)
#t.right(215)
t.right(195)
t.fd(10)
t.right(180)
t.circle(3, -180)
t.right(180)
t.fd(10)
t.right(195)
t.fd(10)
t.right(180)
t.circle(3 , -180)
t.right(180)
t.fd(10)
t.right(130)
t.circle(20 , -30)
t.right(-33)
t.circle(80 , -50)
t.end_fill()               #main
t.up()

t.setpos(-95 , 55)
t.down()
t.right(-90)
t.circle(4 , 180)
t.up()

t.fillcolor('BROWN')
t.begin_fill()

t.setpos(-86 , -80)
t.down()
t.right(-140)
t.fd(10)
t.right(110)
t.fd(20)
t.right(-105)
t.fd(30)
t.right(-100)
t.fd(40)
t.right(-95)
t.fd(35)
t.right(-101)
t.fd(13.5)
t.end_fill()        #main
t.up()

t.fillcolor('BLACK')            #main
t.begin_fill()                  #main

t.setpos(-100 , 171)
t.down()
t.right(118)
t.circle(150 , -25)
t.right(120)
t.circle(150 , -20)
t.right(-88)
t.circle(100 , 22.7)
t.end_fill()                    #main
t.up()

t.fillcolor('BLACK')            #main
t.begin_fill()                  #main

t.setpos(111 , 183)
t.down()
t.right(63)
t.circle(150 , -25)
t.right(120)
t.circle(150 , -20)
t.right(-88)
t.circle(100 , 22.7)
t.end_fill()                    #main



t.hideturtle()
