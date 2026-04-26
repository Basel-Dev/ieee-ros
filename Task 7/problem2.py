class Classroom:
    def __init__(self):
        self.students = []

    def add_student(self, name):
        self.students.append(name)

    def count_students(self):
        return len(self.students)
    
classroom1 = Classroom()

classroom1.add_student("Razan")

count = classroom1.count_students()

print(count)