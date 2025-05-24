def add(a,b):
    print(a+b)
add(5,10)

print("\n")
def add(a=3,b=4):
    print(a+b)
add()

print("\n")
def add(a,b,c=4):
    print(a+b+c)
add(5,8)

print("\n")
def add(a,b,c=4):
    print(a+b+c)
add(5,8,10)

print("\n")
def add(a,b,c=0):
    print(a+b+c)
add(5,10)    
add(5,8,10)


print("\n")
class animal():
    def sound(self):
        print("Animals make sound")
a1=animal()
a1.sound()

print("\n")
print("Polymorphism or Method over riding")
class animal():
    def sound(self):
        print("Animals make sound")
class dog(animal):
    def sound(self):
        print("Dog barks")

d1=dog()
d1.sound()

print("\n")
print("Polymorphism or Method over riding")
class animal():
    def sound(self):
        print("Animals make sound")
class dog(animal):
    def sound(self):
        print("Dog barks")
class bird(animal):
    def sound(self):
        print("Bird singing")
b1=bird()
b1.sound()



print("\n")

class shape():
    def area(self):
        return 0

s1=shape()
print(s1.area())

print("\n")

class shape():
    def area(self):
        return 0
class rectangle(shape):
    def area(self):
        l=10
        b=20
        print(l*b)

r1=rectangle()
r1.area()

