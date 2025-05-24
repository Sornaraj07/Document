print("Called both constructors") 
class a():
    def __init__(self):
        print("A")

    def display(self):
        print("You are in print A")

class b():
    def __init__(self):
        print("B")

    def display(self):
        print("You are in print B")

obj1=a()
obj2=b()
obj1.display()
obj2.display()

print("\n")


print("Using class A constructor in class B") 
class a():
    def __init__(self):
        print("A")

    def display(self):
        print("You are in print A")

class b(a):
    def display(self):
        print("You are in print B")


obj2=b()
obj2.display()


print("\n")

print("Using class A constructor in class B, It's taken same constructor in class B") 
class a():
    def __init__(self):
        print("A")

    def display(self):
        print("You are in print A")

class b(a):    
    def __init__(self):
        print("B")
    def display(self):
        print("You are in print B")

obj2=b()
obj2.display()

print("\n")

print("Using class A constructor in class B, Called both constructors using superkey word") 
class a():
    def __init__(self):
        print("A")

    def display(self):
        print("You are in print A")

class b(a):    
    def __init__(self):
        super().__init__()
        print("B")
    def display(self):
        print("You are in print B")

obj2=b()
obj2.display()

print("\n")

print("Using class C called  in class B, class b called right side in call A [class c(b,a)]") 
class a():
    def __init__(self):
        print("A")

    def display(self):
        print("You are in print A")

class b():    
    def __init__(self):
        super().__init__()
        print("B")
    def display(self):
        print("You are in print B")
        
class c(b,a):    #left object b is the parent constructor in multiple inhertance & b class call parent constructor of right side class A
    def __init__(self):
        super().__init__()
        print("C")
    def display(self):
        print("You are in print C")

obj2=c()
obj2.display()


print("\n")

print("Using class C called  in class B, class b called right side in call A [class c(b,a)][class d(c,b)]") 
class a():
    def __init__(self):
        print("A")

    def display(self):
        print("You are in print A")

class b():    
    def __init__(self):
        super().__init__()
        print("B")
    def display(self):
        print("You are in print B")
        
class c(b,a):    #left object b is the parent constructor in multiple inhertance & b class call parent constructor of right side class A
    def __init__(self):
        super().__init__()
        print("C")
    def display(self):
        print("You are in print C")

class d(c,b):    #left object c is the parent constructor in multiple inhertance & c class call parent constructor of right side class B
    def __init__(self):
        super().__init__()
        print("D")
    def display(self):
        print("You are in print D")

obj2=d()
obj2.display()


print("\n")

print("Using class C called  in class B, class b called right side in call A [class c(b,a)][class d(c,b)]") 
class a():
    def __init__(self):
        print("A")

    def display(self):
        print("You are in print A")

class b():    
    def __init__(self):
        super().__init__()
        print("B")
    def display(self):
        print("You are in print B")
        
class c():    #left object b is the parent constructor in multiple inhertance & b class call parent constructor of right side class A
    def __init__(self):
        super().__init__()
        print("C")
    def display(self):
        print("You are in print C")

class d(c,a):    #left object c is the parent constructor in multiple inhertance & c class call parent constructor of right side class B
    def __init__(self):
        super().__init__()
        print("D")
    def display(self):
        print("You are in print D")

obj2=d()
obj2.display()
