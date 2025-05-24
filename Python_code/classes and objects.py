#Objects & functions
class test:
    
    def monthly(self):
        print("Tution monthly test")
    def exam(self):
        print("School exam")
tution=test()
school=test()

tution.monthly()
school.exam()



class test:
    tution_name=""                              # Object Value not assigned
    school_name="C.S.I Corley HSS"              # Object Value assigned
    
    def monthly(self):
        print("Tution monthly test")
    def exam(self):
        print("School exam")
tution=test()
school=test()

tution.tution_name="Excel Tution"               # Assigning value

print("Tution Name :",tution.tution_name)
print("School Name :",school.school_name)

# Class aobect created and assigned values
class laptop:
    price=0
    processor=""
    ram=""

    
Hp=laptop()
Dell=laptop()
Lenova=laptop()

Hp.price=50000
Hp.processor= "i5"
Hp.ram="12GB"

Dell.price=50000
Dell.processor= "i7"
Dell.ram="16GB"

Lenova.price=45000
Lenova.processor= "i3"
Lenova.ram="8GB"


print("HP Laptop price :",Hp.price)
print("Dell processor : ",Dell.processor)
print("Lenova Ram : ",Lenova.ram)





