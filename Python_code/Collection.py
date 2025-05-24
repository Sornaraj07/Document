#List[]
print("check List[] type")
a=[1,2,3]
print(type(a))

a=[1,2,3]
print(a)


print("Print selected postion value")
a=[1,2,3]
print(a[0])
print(a[2])


print("Append (add) next values a[3] and a[4]  ")
a=[1,2,3]
print(a)
a.append(10)
a.append(12)
print(a)


print("Insert values position (0,100)(2,1000)")
a=[1,2,3]
print(a)
a.insert(0,100)
a.insert(2,1000)
print(a)

print("Modify select value a[0]")
a=[1,2,3]
a[0]=100
print(a)


print("Pop (delete) select value a[2]")
a=[1,2,3,4,5]
a.pop(2)
print(a)

print("Pop (delete) last value a[4]")
a=[1,2,3,4,5]
a.pop()
print(a)

print("Pop (delete) last value a[4] and a[3]")
a=[10,20,30,40,50]
a.pop()
a.pop()
print(a)

print("Append (add) boolean values and string")
a=[1,2,3]
print(a)
a.append(True)
a.append("Ensono")
print(a)

print("Extend(concadinate) a+b")
a=[1,2,3]
b=[11,22,33]
print(a)
print(b)
a.extend(b)
print(a)


#Tuple()

print("check Tuple()type")
a=(1,2,3)
print(type(a))

print("We can't modify values")
a=(1,2,3,4,5)
#a[0]=100
b=list(a)
print(a)
print(b)

print("We can modify Any data type")
a=(1,2,3,4,5)
b=list(a)
b[0]=100
print(a)
print(b)


#Set{}
print("check Set{} type")
a={1,2,3}
print(type(a))

print("Duplicates values removed")
a={1,2,3,4,5,1,2}
print(a)

print("Can't modify values")
print("We can add values")
a={1,2,3,4,5}
a.add(10)
print(a)

print("Remove particular value")
a={1,2,3,4,5}
a.remove(4)
print(a)

print("Pop (delete) un order assigned and auto removed first value a[0]")
a={1,2,3,4,5}
a.pop()
print(a)

#Dictionary{}
print(" Dictionary{} is Key pair value Name(key), ensono(value)")

a={"Name":"Ensono"}
print(a)


print("Print Key value")
a={"Name":"Ensono"}
print(a["Name"])

a={
    "Name":"Ensono",
    "Location":"Chennai",
    "Pincode":600117
    }
print(a["Location"])


print("Print Key & value")
a={
    "Name":"Ensono",
    "Location":["Chennai","Bangalore","Pune"],
    "Pincode":600117
    }
print(a.keys())
print(a.values())

print("Delete Key pair value")
a={
    "Name":"Ensono",
    "Location":["Chennai","Bangalore","Pune"],
    "Pincode":600117
    }
a.pop("Name")
print(a)

a={
    "Name":"Ensono",
    "Location":["Chennai","Bangalore","Pune"],
    "Pincode":600117
    }
del a["Pincode"]
print(a)

print("Clear Key pair value")
a={
    "Name":"Ensono",
    "Location":["Chennai","Bangalore","Pune"],
    "Pincode":600117
    }
a.clear()
print(a)




