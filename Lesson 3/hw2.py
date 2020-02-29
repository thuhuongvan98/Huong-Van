from turtle import *
speed(-1)
shapesize(1)
shape("turtle")

mau = ["red","yellow","blue","brown","purple"]
for a in range(len(mau)):
    fillcolor(mau[a])
    color(mau[a])
    begin_fill()
    right(90)
    forward(100)
    right(90)
    forward(50)
    if a<4:
        for b in range(2):
            right(90)
            forward(100)
    else:
        right(90)
        forward(100)
    end_fill()

mainloop()