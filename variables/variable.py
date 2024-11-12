
#All primitive data types are immutable i.e new memory is allocated
age: int = 20
print(id(age))# diff memory
age = age + 1
print(id(age))#Diff memory

#Objects data types are mutable. No allocation of new memory.
courses = ["maths", "Computer", "History"]
print(id(courses))# Same memory
courses.append("Physics")
print(id(courses))#Same memory