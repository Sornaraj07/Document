# Constructor calling function( __init__) inbuild function

print("Without call any function  Constructor  function( __init__) calling automatically")
class laptop:
    def __init__(self):
        print("Constructor Demo")
    def display(slef):
        print("Display")

Hp=laptop()


class laptop:
    def __init__(self):
        self.price=0
        self.ram=""
        self.processor=""

    def display(self):
        print("Ram :",self.ram)
        print("Processor :",self.processor)

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

Hp.display()
Dell.display()
Lenova.display()


