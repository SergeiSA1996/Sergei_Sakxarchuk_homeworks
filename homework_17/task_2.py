# 2)	Создайте класс Students, содержащий поля: фамилия и инициалы, номер группы,
# успеваемость (список из пяти элементов).
# Создать класс School:
# Добавить возможно для добавления студентов в школу
# Добавить возможность вывода фамилий и номеров групп студентов, имеющих оценки, равные только 5 или 6.
# Добавить возможность вывода учеников заданной группы
# Добавить возможность вывода учеников претендующих на автомат(средний балл >= 7)


class Students:
    def __init__(self, name, group_number, performance):
        self.name = name
        self.group_number = group_number
        self.performance = performance


class School:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def get_students_high_marks(self):
        students_high_marks = []
        for student in self.students:
            if all(mark >= 5 for mark in student.performance):
                students_high_marks.append(student)
        return students_high_marks

    def get_students_by_group(self, group_number):
        students_by_group = []
        for student in self.students:
            if student.group_number == group_number:
                students_by_group.append(student)
        return students_by_group

    def get_students_eligible_for_auto(self):
        students_eligible_for_auto = []
        for student in self.students:
            average_mark = sum(student.performance) / len(student.performance)
            if average_mark >= 7:
                students_eligible_for_auto.append(student)
        return students_eligible_for_auto


school = School()

student1 = Students("Иванов И.И.", 1, [5, 6, 5, 5, 6])
student2 = Students("Петров П.П.", 2, [6, 6, 6, 6, 6])
student3 = Students("Сидоров С.С.", 1, [5, 6, 7, 8, 9])

school.add_student(student1)
school.add_student(student2)
school.add_student(student3)

students_high_marks = school.get_students_high_marks()
for student in students_high_marks:
    print(student.name, student.group_number)

students_by_group = school.get_students_by_group(1)
for student in students_by_group:
    print(student.name, student.group_number)

students_eligible_for_auto = school.get_students_eligible_for_auto()
for student in students_eligible_for_auto:
    print(student.name, student.group_number)