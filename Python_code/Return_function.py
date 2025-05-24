#Return

print("Function retun call")
def company():
    print("Ensono")
company()


def company():
    return "My company is Ensono"
print(company())

def company():
    return "My company is Ensono"
msg=company()
print(msg)


def valueofa():
    return 10
a=valueofa()
print(a)


print("Validation")
s_user="Sorna"
s_pwd="123"
user=input("Enter User name:")
password=input("Enter User password:")

def validate():
    if(s_user==user and s_pwd==password):
        print("correct")
    else:
        print("Wrong")
validate()


print("Return Validation")
s_user="Sorna"
s_pwd="123"
user=input("Enter User name:")
password=input("Enter User password:")

def validate():
    if(s_user==user and s_pwd==password):
        return True
    else:
        return False
a=validate()
print(a)



def add(n1,n2):
    return n1+n2
a=int(input("Enter Value of A:"))
b=int(input("Enter Value of B:"))
c=int(input("Enter Value of C:"))

added=add(a,b)

output=added*c

print(output)
   

