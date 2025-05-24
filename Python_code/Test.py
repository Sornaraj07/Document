
a=10
b=5
c=a+b
print(c)

# print("Enter your Name : ")
name=input("Enter your Name : ")
# print("Enter your Age : ")
age= int(input("Enter your Age : "))
print("your Name is ",name)
print("your Age is ",age)

#If condition
if(age>=30):
    print("Welcome to Senior group")
else:
    print("Not eligible in Senior group")    

# Arithmetic operator
if(age>=30 and age<=40):
    print("Welcome to Senior L3 group")
else:
    print("Not eligible in Senior L3 group")

if(age<30):
    print("Welcome to 2K kidz group")
elif(age>=30 and age<=40):
    print("Welcome to 90's kidz group")
else:
    print("Welcome to 80's kidz group") 

# reminder value
if(age%2==0):
    print(name,"Age is even")
else:
    print(name,"Age is odd")

#opreators
a=int(input("A:"))
b=int(input("B:"))
operation=input("Enter operation :add/sub/mul/div :")
if(operation=="add"):
    print("Addition of A+B=",a+b)
elif(operation=="sub"):
    print("Subration of A-B=",a-b)
elif(operation=="mul"):
    print("Multiplication of A*B=",a*b)
elif(operation=="div"):
    print("Division of A/B=",a/b)
else:
    print("Invalid operation")



        

















