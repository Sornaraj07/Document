print("Instance method")
class phone():
    chargertype="Type-C"             # class variable
    def __init__(self):
        self.brandname=""         #instance variable
        self.amount=1000
        
    def setprice(self,price):       #using self it's instance method
        self.amount=price

    def getprice(self):
        print(" Price :",self.amount)

    def changechargertype(cls):  # using class variable
        cls.chargertype="Lightning Type-C"
        print("New chargertype is Lightning Type-C")      
 

phone.changechargertype(phone)

Vivo=phone()
Vivo.setprice(20000)
Vivo.getprice()
    
Oppo=phone()
Oppo.setprice(25000)
Oppo.getprice()
print("\n")



print("Class method")
class phone():
    chargertype="Type-C"             # class variable
    def __init__(self):
        self.brandname=""         #instance variable
        self.amount=1000
        
    def setprice(self,price):       #using self it's instance method
        self.amount=price

    def getprice(self):
        print(" Price :",self.amount)

    @classmethod                    # using class method(decarator)
    def changechargertype(cls):  # using class variable
        cls.chargertype="Lightning Type-C"
        print("New chargertype is Lightning Type-C")      
 
Vivo=phone()
Vivo.setprice(20000)
Vivo.getprice()
    
Oppo=phone()
Oppo.setprice(25000)
Oppo.getprice()

phone.changechargertype()
print("\n")



print("Static method")
class phone():
    chargertype="Type-C"             # class variable
    def __init__(self):
        self.brandname=""         #instance variable
        self.amount=1000
        
    def setprice(self,price):       #using self it's instance method
        self.amount=price

    def getprice(self):
        print(" Price :",self.amount)

    @classmethod                    # using class method(decarator)
    def changechargertype(cls):  # using class variable
        cls.chargertype="Lightning Type-C"
        print("New chargertype is Lightning Type-C")

    @staticmethod                   # using static method(decarator)
    def info():                     # withou assign variable
        print("Static method calling without self and cls variable")
 
Vivo=phone()
Vivo.setprice(20000)
Vivo.getprice()
Vivo.info()


Oppo=phone()
Oppo.setprice(25000)
Oppo.getprice()
Oppo.info()

phone.changechargertype()

