#1
def in_ra():
    for x in range(3):
        print("Hello World!")
in_ra()

#2
def plus(a,b):
    print(a+b)
plus(4,5)

#3
from turtle import *

def draw_square(a,line):
    color(str(line))
    for y in range(4):
        forward(int(a))
        left(90)

#4
for i in range(30):
    draw_square(i*5,'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()

#5
def draw_star(x,y,length):
    penup()
    forward(x)
    left(90)
    forward(y)
    right(90)
    pendown()
    for i in range(5):
        right(144)
        forward(int(length))

#6
speed(0)
color('blue')
for i in range(100):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(3,10)
    draw_star(x,y,length)

#7
def remove_dollar_sign(s):
    s = s.replace('$','')
    print(s)
    return(s)

#8
string_with_no_dollars = remove_dollar_sign("$80% percent of $life is showing up")
if string_with_no_dollars == "80% percent of life is showing up":
    print("Your function is correct")
else:
    print("Oops, there's a bug")

#9
def get_even_list(l):
    for i in l:
        if i % 2 == 0:
            pass
        else:
            l.remove(i)
    print(l)
    return(l)

#10
even_list = get_even_list([1,2,5,-10,9,6])
if set(even_list) == set([2, -10, 6]):
    print("Your function is correct")
else:
    print("Oops, bugs detected")

#11
def is_inside(point,regtangle):
    if point[0] > regtangle[0] and point[1] > regtangle[1]:
        if regtangle[2] > (point[0]-regtangle[0]) and regtangle [3] > (point[1]-regtangle[1]):
            result = True
        else:
            result = False
    else:
        result = False
    print(result)
    return(result, point, regtangle)

#12
inside = bool(is_inside([200,120],[140,60,100,200]))
if inside == True:
    print("Your function is correct")
else:
    print("Bugs detected")
is_inside([200,120],[140,60,100,200])

#13
# Bài này nằm trong folder back-color-problem ạ. Thực ra thì để chạy đc game em sửa lại code ở file app.py TT_TT
# K hiểu tại sao nhưng vd là cứ "from PyQt5.QtGui import QColor" thì k được trong khi cú pháp đúng rồi
# nhưng đến khi đổi thành "from PyQt5 import QtGui" rồi ở dưới code sửa thành "QtGui.Qcolor" thì lại được ạ.
# Anh có được những dòng này thì giải đáp cho em với ạ em tra không ra huhu






