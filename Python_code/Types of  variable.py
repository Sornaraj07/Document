class phone():
    def __init__(self,brand,price,charger):
        self.brandname=brand                #instance variable
        self.amount=price
        self.chargertype=charger
    def display(self):
        print(" Brand :",self.brandname)
        print(" Price :",self.amount)
        print(" Charger :",self.chargertype)

Vivo=phone("Vivo T21", "22000", "Type-C")
Vivo.display()
    
Oppo=phone("Oppo M30", "30000", "Lightning Type-C")
Oppo.display()
        

print("Class variable")
class phone():
    chargertype="Type-C"             # class variable
    def __init__(self,brand,price):
        self.brandname=brand         #instance variable
        self.amount=price
        
    def display(self):
        print(" Brand :",self.brandname)
        print(" Price :",self.amount)
        print(" Charger :",self.chargertype)

phone.chargertype="Lightning Type-C"

Vivo=phone("Vivo T21", "22000")
Vivo.display()
    
Oppo=phone("Oppo M30", "30000")
Oppo.display()
