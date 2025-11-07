#-------------variable_declaration & dynamic_typing----------#

x = 10
name = "Habib"
print(type(name))

# multiple_assignments
x = y = z = 100
print(x)
print(y)
print(z)


a, b, c = 1, 2, 3
print(a)
print(b)
print(c)

#------------------------Advance---------------------------------------#
# global_variable
name = "Md_Habibullah"  # Global variable

def greet():
    print("Hello", name)
greet()  # Output: Hello Habib

# global_variable_reusable
def greet_2():
    print("hey", name)
greet_2()


#local_variable
def show_age():
    # global age
    age = 25  # Local variable, only exists inside this function
    print("Inside function, Age:", age)
show_age()
# print(age)


#-----------instance_variable----------------#

class Person:
    def __init__(self, name):
        self.name = name  # Instance variable

# Create objects (instances)
p1 = Person("Habib")
print(p1.name) 



#--------------------class_variable-------------------------#

class Student:
    school = "daffodil international university"  # Class variable

    def __init__(self, name):
        self.name = name  # Instance variable

s1 = Student("Habib")
s2 = Student("Mahi")

print(s1.school)  
print(s2.school)

# Modifying class variable
Student.school = "brac university"
print(s1.school)
