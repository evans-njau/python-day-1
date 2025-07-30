marks = [55, 72, 48, 91, 66, 59, 87, 33]
marks.append(77)
marks.insert(3, 60)
marks.remove(33)
marks[2] = 50

print("Updated Marks:", marks)

# Count students who scored above 60
count = 0
for mark in marks:
    if mark > 60:
        count += 1
print("Students scoring above 60:", count)

# Print marks in descending order
print("Descending order:", sorted(marks, reverse=True))

# Average mark
average = sum(marks) / len(marks)
print("Average mark:", average)

# Pass/Fail list
status = ["pass" if mark >= 50 else "fail" for mark in marks]
print("Status:", status)

