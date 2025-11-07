#--------List(ordered,mutable,allows_duplicate_values)---#

#---------------Access_Elements----------------#

my_list = [10, 20, 30, 40, 40] 
print(my_list[1]) 
print(my_list[-1],my_list[1],my_list[-2])

#------------------Modify_Elements----------------#

my_list = [10, 20, 30, 40, 40] 
my_list[0]= 100
my_list[-1]= 50
print(my_list) 

#------------------Add_Items----------------------#

my_list.append(50)
print(my_list) 

# specific_position 
my_list.insert(1,200) 
print(my_list)

# extend()
my_list.extend([500,600,700]) 
print(my_list) 

#----------------Remove_Items-------------------------#

# remove(value)
my_list = [10, 20, 30, 40] 
my_list.remove(20) 
print(my_list)  

#  pop() – removes_last_item
my_list = [10, 20, 30, 40] 

my_list.pop() 
my_list.pop(1) #index_use 
print(my_list) 
