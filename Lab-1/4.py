
students = {'1MS17IS020':'Amaana','1MS17IS021':'alfa'}
list = ["value1","value2","value3"]

j = 0

for i in students:
    print("Key is ",i," and value is ",students[i])
    list[j] = students[i]
    j = j+1

print(list)
print(students.keys)
print(students.values())
