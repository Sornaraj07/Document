#for
for fruit in "APPLE":
    print(fruit)
    
for i in range(5):
    print(i)

for j in range(1,5):
    print("\t",j)
    
for k in range(1,6):
    print(k,"\n")

for k in range(1,6):
    print("Ensono")

for k in range(1,6):
    print("Ensono")
    print(k)

for k in range(1,6):
    print(k,"Ensono")
print("\n")

for k in range(1,11):
    print(k,"x 2 =",k*2)

x=int(input("X:"))
y=int(input("Y:"))
for i in range(x+1,y):
    print(i)
print("\n")

for i in range(1,11):
    if(i%2==0):
       print(i)
print("\n")


even_count=0
odd_count=0
for i in range(1,11):
    if(i%2==0):
       even_count=even_count+1
    else:
        odd_count=odd_count+1
print("Even number in the loop :",even_count)
print("Odd number in the loop :",odd_count)


count=0
for i in range(1,101):
    if(i%3==0 and i%5==0):
       count=count+1    
print("1 -100 Divisible by 3,5 number in the loop :",count)

sum=0
for i in range(1,5):
    sum=sum+i
print("sum of :",sum)


