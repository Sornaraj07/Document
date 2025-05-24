a=[1,2,3,4,5]
for i in a:
    print(i)

a=[]
a.append(10)
a.append(20)
b=int(input("enter next value:"))
a.append(b)
print(a)


a=[]
for i in range(10):
    print(i)

a=[]
print("Enter the 5 values")
for i in range(5):
    num=int(input("Enter the value "+str(i+1)+" : "))
    a.append(num)
print(a)
sum=0
for i in a:
        sum=sum+i
print("Addition of 5 Values=",sum)




