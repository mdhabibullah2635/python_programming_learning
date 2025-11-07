#-----------------Set(unordered,unique_items,not_allow_duplicates)-----------------#

#------------------Add_items----------------------------#

my_set = {1,3} 
print(my_set)

my_set.add(2) 
my_set.add(20)
print(my_set)

#-----------------Update-------------------------#

my_set.update([2,3,4]) 
print(my_set)

my_set.update([5,6,7,8]) 
print(my_set)


#----------------Deleting_Set_elements-------------#

my_set = {1,2,3,4} 

my_set.discard(4)
print(my_set) 
my_set.remove(3) 
print(my_set)


