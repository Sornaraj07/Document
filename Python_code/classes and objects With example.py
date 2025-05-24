class student:
    def __init__(self):
        self.name="Sornaraj"
        self.regno="600117"
    def display(self):
        print("Name : ",self.name)
        print("Register Number :",self.regno)

student1=student()

print(student1.name)
print(student1.regno)

student1.display()


class student:
    def __init__(self):
        self.name=""
        self.regno=""
    def display(self):
        print("Name : ",self.name)
        print("Register Number :",self.regno)

student1=student()
student2=student()

student1.name="Sornaraj"
student1.regno="575573"

student2.name="Ramesh"
student2.regno="600115"

student1.display()
student2.display()



# Passing value in parameter
print("Passing value in parameter")
class fruit:
    def __init__(self,colour):
        self.color=colour

apple=fruit("red")
print(apple.color)


# Passing value in  parameter
print("Passing value in multiple parameter")
class teacher:
    def __init__(self,name,sub):
        self.name=name
        self.subject=sub
    def display(self):
        print("Name :",self.name)
        print("Register number :",self.subject)

t1=teacher("Vimala","English")
t2=teacher("Thamarai Selvi","Maths")

t1.display()
t2.display()



class calculator:
         
    def add(self,a,b):
        print("A+B:",a+b)
    def sub(self,a,b):
        print("A-B:",a-b)
    def mul(self,a,b):
        print("A*B:",a*b)
    def div(self,a,b):
        print("A/B:",a/b)

obj=calculator()
obj.add(10,2)
obj.sub(10,5)
obj.mul(10,2)
obj.div(10,3)
    


class calculator:
    def __init__(self,a,b):    
        self.vlueofA=a
        self.vlueofB=b
    def add(self):
        print("A+B:",self.vlueofA+self.vlueofB)
    def sub(self):
        print("A-B:",self.vlueofA-self.vlueofB)
    def mul(self):
        print("A*B:",self.vlueofA*self.vlueofB)
    def div(self):
        print("A/B:",self.vlueofA/self.vlueofB)
        
    
obj1=calculator(10,2)
obj1.add()
obj1.sub()
obj1.mul()
obj1.div()


        
