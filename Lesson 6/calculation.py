#initial function
def calculate(x,y,operator):
    if operator == '+':
        z = x+y
    elif operator == '-':
        z = x-y
    elif operator == '*':
        z = x*y
    elif operator == '/':
        z = x/y
    return z #đưa z ra ngoài để có thể sử dụng đc ngoài function

if __name__ == "__main__":
    a = calculate(4,5,'-')
    print(a)
#function


