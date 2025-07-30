# a list is a container of object 
# which is: mutable, ordered, allows duplicates
# Has several operations:
# Adding elements using index we use .insert(index, value)
# Adding element at the end .append(value)
# Replacing an element list_name[index] = value
# Deleting elements .remove(value)
# removing last element .pop()
# range .list_name[range] 
marks = [12,78,90,78,90,45,37,65]
marks.append(100)
marks.insert(0,10)
marks[1] = 20
marks.remove(20)
marks.pop()
print(marks[2:6])
for mark in marks:
    print(mark)