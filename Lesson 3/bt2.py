from turtle import *
speed(-1)
shapesize(1)
shape("turtle")
count=0

mau = ["red","blue","brown","yellow","grey"]
for i in range(3,8):
    for a in range(i):
        for b in range(len(mau)):
            color(mau[count])
        forward(100)
        left(360/i)
    count=count+1

mainloop()