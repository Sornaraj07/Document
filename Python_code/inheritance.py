class college():
    def department(self):
        print("College department")

class student():
    def dep_class(self):
        print("College Student")

sorna=student()
sorna.dep_class()
print("\n")

print("Single inheritance") #only 2 classes, one class access with onther class
print("-------------------")
class college():
    def department(self):
        print("College department")

class student(college):
    def dep_class(self):
        print("College Student")

sorna=student()
sorna.department()
sorna.dep_class()
print("\n")

print("Multiple inheritance") #2 or more classes, one class access with multiple classes 
print("----------------------")
class college():
    def department(self):
        print("College department")
class staff():
    def dep_staff(self):
        print("College department staff")

class student(college,staff):
    def dep_class(self):
        print("College Student")

sorna=student()
sorna.department()
sorna.dep_class()
sorna.dep_staff()
print("\n")

print("Multilevel inheritance") #2 or more classes, one class access with another classes 
print("------------------------")
class college():
    def department(self):
        print("College department")
class staff(college):
    def dep_staff(self):
        print("College department staff")

class student(staff):
    def dep_class(self):
        print("College Student")

sorna=student()
sorna.department()
sorna.dep_class()
sorna.dep_staff()
print("\n")
mca=staff()
mca.department()


print("\n")

print("Hierarichal inheritance") #2 or more classes access with one class
print("------------------------")
class college():
    def department(self):
        print("College department")
class staff(college):
    def dep_staff(self):
        print("College department staff")
class student(college):
    def dep_class(self):
        print("College Student")
class admin(college):
    def college_admin(self):
        print("College admin")


payroll=admin()
payroll.college_admin()
payroll.department()
print("\n")
sorna=student()
sorna.department()
sorna.dep_class()
print("\n")
mca=staff()
mca.dep_staff()
mca.department()



print("\n")

print("Hybrid inheritance") # combination of single,multiple, multilevel and Hierarichal inheritance
print("-------------------")
class college():
    def department(self):
        print("College department")
class location():
    def college_location(self):
        print("College loction is Pallvaram")
class staff(college):
    def dep_staff(self):
        print("College department staff")
class student(college,location,admin):
    def dep_class(self):
        print("College Student")
class admin(college):
    def college_admin(self):
        print("College admin")


sorna=student()
sorna.department()
sorna.dep_class()
sorna.college_location()
sorna.college_admin()
print("\n")
payroll=admin()
payroll.college_admin()
payroll.department()
print("\n")
mca=staff()
mca.dep_staff()
mca.department()

