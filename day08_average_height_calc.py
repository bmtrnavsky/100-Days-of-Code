student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total_height = 0
for height in student_heights:
  total_height = total_height + height
total_students = 0
for students in student_heights:
  total_students = total_students +1

avaerge_height = round(total_height / total_students) 
print(avaerge_height)
