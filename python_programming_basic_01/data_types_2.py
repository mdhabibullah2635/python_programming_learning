#----------------------------1_Text_Type-------------------------------#

# str
s = "Hello, md habib"
type(s)  # <class 'str'>


# string_operation

a = "Md"
b = "Habibullah"
c = "Habib"

print(a +" " + b +" " + c)
print(a * 4) 
print(len(a))

print(b[0]) # (Indexing) 
print(b[-2]) # Negative_Indexing
print(b [1:4]) # Slicing
print(b[0:5])

a = "mdhabibullahhabib"

print(a[:5]) # 1st first 5 ta digit 
print(a[7:]) # 1st 7 digit por baki gula 

# Negative_Indices
a = "Hello,world!" 
print(a[-6:-1]) 

# Slicing with Step Size syntax: sequence[start:end:step] 
a = "Hello, world!" 

print(a[::2]) # Every second character # : 0, 2, 4, 6, 8, 10, 12

a = "Hello, world!"
print(a[::-1])  # "Reverses the string 
print(a[::-4])  # "Reverses the string  -1,-4,-9,-13

print(a[5:0:-1]) # 5,4,3,2,1
print(a[-5:-2:1]) # -5, -4, -3

# String_Methods
s = "python programming" 

print(s.upper())  # "PYTHON PROGRAMMING" 
print(s.lower())  # "python programming" 
print(s.title())  # "Python Programming" 
print(s.replace("python", "Java"))  # "Java programming" 
print(s.split())  # ['python', 'programming']  


#----------------------2_Numerical_Data_Types------------------------------#
 
# int
x = 10
y = 3
type(x)  # <class 'int'>


# float
y = 3.14
type(y)  # <class 'float'>

# complex
z = 2 + 3j
type(z)  # <class 'complex'>

#-------------------------------------3_Sequence_Types-------------------------------------#

# List
my_list = ["habib","mahi","tuhin"]
print(type(my_list))

# tuple
my_tuple = (10,20,30)
print(type(my_tuple))

# range
for i in range(5):
    print(i)

#----------------------------------------4_Mapping_Type--------------------------------#

#  dictionary
my_dictionary_info = {
    'Name': 'Md Habibullah',
    'Roll': 664104
}
print(my_dictionary_info)

#----------------------------------------4_Set_Types------------------------------------#

# set
my_set = {'swe','cse','ai'}
print(type(my_set))


#------------------------------------------5_Boolean_Type------------------------------------#

# boolean_Type
x = True
y = False

print(x)   # True
print(y)   # False
print(type(x))  # <class 'bool'>


#-----------------------------Binary_Types---------------------------------#

# ------------------ bytes ------------------
# bytes are immutable (cannot be changed) binary data
x = b"Hello"
print(x)              # b'Hello'
print(type(x))        # <class 'bytes'>
print(x[0])           # 72 (ASCII value of 'H')

# ------------------ bytearray ------------------
# bytearray is mutable (can be changed) binary data
y = bytearray(b"Hello")
print(y)              # bytearray(b'Hello')
print(type(y))        # <class 'bytearray'>

# modifying bytearray
y[0] = 90             # Replace 'H' (72) with 'Z' (90)
print(y)              # bytearray(b'Zello')

# ------------------ memoryview ------------------
# memoryview lets you access parts of binary data without copying it
z = memoryview(b"Hello")
print(z)              # <memory at 0x...>
print(type(z))        # <class 'memoryview'>

# accessing specific bytes from memoryview
print(z[0])           # 72 ('H')
print(z[1])           # 101 ('e')


#--------------------Type_Casting--------------------------------#

# int → float
a = 10
b = float(a)
print(b)          # 10.0
print(type(b))    # <class 'float'>


# eval() for Direct Data Type Conversion

x = eval(input("Enter a number: ")) 

print("You entered:", x) 
print("Type:", type(x)) 

