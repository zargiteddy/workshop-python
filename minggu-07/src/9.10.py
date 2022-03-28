class Student:
    gpa = 0
    name = ""

print(sum(i*i for i in range(10)))                 

xvec = [10, 20, 30]
yvec = [7, 5, 3]
print(sum(x*y for x,y in zip(xvec, yvec)))        

page = "hello world"
unique_words = set(word for line in page  for word in line.split())
print(unique_words)

student = Student()
student.gpa = 4
student.name = "Argi"

student2 = Student()
student2.gpa = 3
student2.name = "Bun-Bun"

graduates = [student, student2]

valedictorian = max((student.gpa, student.name) for student in graduates)
print(valedictorian) #menampilkan data dengan nilai terbesar diantara 2 data

data = 'golf'
list = (list(data[i] for i in range(len(data)-1, -1, -1)))
print(list)
