#------------------Arithmetic_Operators----------------#
a = 5
b = 3

print("Addition: ", a + b)       # 8
print("Subtraction: ", a - b)    # 2
print("Multiplication: ", a * b) # 15
print("Division: ", a / b)       # 1.6666...
print("Floor Division: ", a // b)# 1
print("Modulus: ", a % b)        # 2
print("Exponent: ", a ** b)      # 125

#---------------------Comparison_Operators-------------------#

print("Equal: ", a == b)     # False
print("Not Equal: ", a != b) # True
print("Greater: ", a > b)    # True
print("Less: ", a < b)       # False
print("Greater or Equal: ", a >= b) # True
print("Less or Equal: ", a <= b)    # False

#--------------------Logical_Operators------------------#

x = True
y = False

print("Logical Operators:")
print("x and y: ", x and y) # False
print("x or y: ", x or y)   # True
print("not x: ", not x)     # False

#---------------Bitwise_Operators--------------------#

m = 5  # 0101
n = 3  # 0011

print("Bitwise Operators:")
print("AND: ", m & n)   # 1 (0001)
print("OR: ", m | n)    # 7 (0111)
print("XOR: ", m ^ n)   # 6 (0110)
print("NOT m: ", ~m)    # -6
print("Left Shift: ", m << 1)  # 10 (1010)
print("Right Shift: ", m >> 1) # 2  (0010)

#----------------Membership & Identity-----------------#

my_list = [1, 2, 3]
print("2 in my_list: ", 2 in my_list)         # True
print("5 not in my_list: ", 5 not in my_list) # True

a_list = [1, 2]
b_list = a_list
c_list = [1, 2]

print("a_list is b_list: ", a_list is b_list)   # True
print("a_list is c_list: ", a_list is c_list)   # False
print("a_list == c_list: ", a_list == c_list)   # True