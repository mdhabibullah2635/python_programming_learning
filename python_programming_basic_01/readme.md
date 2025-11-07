# ----------------🐍 Python_Basic_Syntax----------------------#

## 1. print() Function  
- Used to display output.  
- Can print text or variables.  
- f-strings allow easy variable insertion inside strings.  

## 2. Comments  
- `#` → Single-line comment.  
- `""" ... """` → Multi-line comment / Docstring.  

## 3. Multi-line String  
- Use triple quotes (`""" ... """`) to write text across multiple lines.  
- Output keeps the same formatting.  

## 4. Indentation  
- Wrong indentation → `IndentationError`.



# 🐍---------------------Python_Variables------------------------#

## 🔹 Variable Declaration & Dynamic Typing
- In Python, no need to specify type while declaring a variable.  
- Type is decided automatically based on the assigned value (dynamic typing).  
- Multiple variables can be assigned in one line (same or different values).  

---

## 🔹 Global Variable
- Declared outside any function.  
- Accessible inside functions directly.  
- Can be used anywhere unless overwritten.  

---

## 🔹 Local Variable
- Declared inside a function.  
- Exists only within that function’s scope.  
- Accessing it outside causes `NameError`.  

---

## 🔹 Instance Variable
- Declared with `self.variable` inside the `__init__` method.  
- Each object (instance) gets its own separate value.  
- Different objects can hold different values.  

---

## 🔹 Class Variable
- Declared inside the class but outside methods.  
- Shared among all objects of the class.  
- Changing it affects all objects.  


# 🐍---------------------Python_Data_Type------------------------#

1. Numerical_Data_Types

* int (Represents integers.)
* float(Represents floating-point numbers)
* complex (Complex numbers)

2. Text_Type

* str (A sequence of Unicode characters & Strings are immutable & Support slicing: s[0:5])


# 3.Sequence_Data_Types

* list (A List in Python is a collection which is ordered and changeable (mutable). It allows duplicate values.)

* tuple (A tuple is an ordered, unchangeable (immutable) collection. It allows duplicate values. Fixt not change value )

* rance (Used in loops or to generate sequences)

# 4.Set & Mapping_Data_Types
* set (A set is an unordered collection of unique items. It does not allow duplicates.)

* dic (A dictionary is a collection of key-value pairs. It's unordered (before Python 3.7), changeable, and does not allow duplicate keys.)

# Boolean_Type
* Logical values: True or False

