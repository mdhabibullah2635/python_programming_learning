#--------------------Dictionary(unordered,changeable,does_not_allow_duplicate_keys-------------------------------#

#--------------------Accessing_Values_in_Dictionary--------------------------------------------#

Mydict_info = { 
    'Name': 'Md Habibullah', 
    'Roll No': 665104, 
    'University' : 'DIU' 

} 
print(Mydict_info['Name']) 
print(Mydict_info['Roll No'])

#loop_use
Mydict_info_2 = { 
    'Name': 'Md Habibullah', 
    'Roll No': 665104, 
    'University' : 'DIU' 

}
for i in Mydict_info_2: 
    print(i,Mydict_info[i]) 

#-----------------------Values_added_dic-------------------------------#

Mydict_info = { 

    'Name': 'Md Habibullah', 
    'Roll No': 665104, 
    'University' : 'DIU' 
} 
Mydict_info['Dep']='CSE' 
print(Mydict_info)

#-------------------------Update-------------------------------------------#

Country_Code_Dict = {'India': 91,'UK' : 44, 'USA' : 1, 'Spain' : 34}

# add_single_key_value 
Country_Code_Dict.update( {'Germany' : 49})
print(Country_Code_Dict)

Country_Code_Dict.update( {'India' : 100}) 
print(Country_Code_Dict)


# add_multi 
Country_Code_Dict.update([('Austria',43),('Russia,',7)]) 
print(Country_Code_Dict)

#------------------------------Deleted--------------------------------------#

Mydict_info = {  
    'Name': 'Md Habibullah',  
    'Roll No': 665104,  
    'University' : 'DIU'  
}  

 
Mydict_info.pop("Name") 
print("After pop('Name'):", Mydict_info) 

Mydict_info.popitem() 
print("After popitem():", Mydict_info) 

 
Mydict_info.clear() 
print("After clear():", Mydict_info) 


# If you still want to use del, do it at the very end: 
del Mydict_info
# print(Mydict_info)  # Uncommenting this will raise NameError 