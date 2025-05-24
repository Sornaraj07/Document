#function
print("Function call")
def company():
    print("Ensono")

company()


print("Function calling")
def add():
    print("Addition")
    a=int(input("Enter Value of A:"))
    b=int(input("Enter Value of B:"))
    print("A+B:",a+b)
add()
def mul():
    print("Multipilication")
    a=int(input("Enter Value of A:"))
    b=int(input("Enter Value of B:"))
    print("A*B:",a*b)
mul()

def add():
    print("Addition")
    a=int(input("Enter Value of A:"))
    b=int(input("Enter Value of B:"))
    print("A+B:",a+b)
def mul():
    print("Multipilication")
    a=int(input("Enter Value of A:"))
    b=int(input("Enter Value of B:"))
    print("A*B:",a*b)
mul()
add()

print("Function call with argument")
def company(msg):
    print(msg,"Ensono")

company("My company name is")

def company(msg):
    print("Ensono",msg)
company("is my company name")

print("Function value assign to argument")
def argu_value(b):
    print(b)
argu_value(100)

def argu_value(b):
    print(b)
a=10
argu_value(a)

print("Odd or Even")


def odd_even(a):
    if(a%2==0):
        print("Even")
    else:
        print("Odd")
b=int(input("Enter Value to find Odd or Even number:"))
odd_even(b)


print("For loop with function call")
def printrange():
    for i in range(1,6):
        print(i)
printrange()

def printrange(r1,r2):
    for i in range(r1,r2):
        print(i)
printrange(1,6)

def printrange(r1,r2):
    for i in range(r1,r2):
        print(i)
a=int(input("Enter Value of A:"))
b=int(input("Enter Value of B:"))
    
printrange(a,b)






