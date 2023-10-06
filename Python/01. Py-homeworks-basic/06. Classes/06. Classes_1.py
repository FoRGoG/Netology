class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer) and course in
                lecturer.courses_attached and course in
                self.courses_in_progress):
            if course in lecturer.grades_from_students:
                lecturer.grades_from_students[course] += [grade]
            else:
                lecturer.grades_from_students[course] = [grade]
        else:
            return 'Mistake!'

    def __middle__(self):
        sum = 0
        count = 0
        for i in self.grades.values():
            for x in i:
                sum += int(x)
                count += 1
        return round(sum/count, 2)

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашнее задание: {self.__middle__()}\n'
                f'Курсы в процессе изучения: {",".join(self.courses_in_progress)}\n'
                f'Завершенные курсы: {",".join(self.finished_courses)}')

    def __lt__(self, other):
        if not isinstance(other, Student):
            return 'Ошибка'
        n = self.__middle__() > other.__middle__()
        if n:
            return f'Средняя оценка выше у студента {self.name}'
        else:
            return f'Средняя оценка выше у студента {other.name}'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_lecturer(self):
        return super().rate_lecturer


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_from_students = {}

    def __middle__(self):
        sum = 0
        count = 0
        for i in self.grades_from_students.values():
            for x in i:
                sum += int(x)
                count += 1
        return round(sum/count, 2)

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка: {self.__middle__()}\n')

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return 'Ошибка'
        n = self.__middle__() > other.__middle__()
        if n:
            return f'Средняя оценка выше у лектроа {self.name}'
        else:
            return f'Средняя оценка выше у лектора {other.name}'


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student) and course in
                self.courses_attached and course in
                student.courses_in_progress):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (f'Имя: {self.name} \n'
                f'Фамилия: {self.surname}')


def average_student(list, name_course):
    sum = 0
    count = 0
    for i in list:
        for j in i.grades[name_course]:
            sum += int(j)
            count += 1
    return round(sum/count, 2)


def average_lecturer(list, name_course):
    sum = 0
    count = 0
    for i in list:
        for j in i.grades_from_students[name_course]:
            sum += int(j)
            count += 1
    return round(sum/count, 2)

student_1 = Student('Elon', 'Musk', 'Male')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['Git']
student_1.finished_courses += ['English']

student_2 = Student('Jeff', 'Bezos', 'Male')
student_2.courses_in_progress += ['Python']
student_2.courses_in_progress += ['Git']
student_2.finished_courses += ['English']

reviewer_1 = Reviewer('Steeve', 'Jobs')
reviewer_1.courses_attached += ['Python']
reviewer_1.courses_attached += ['Git']

reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Git', 9)
reviewer_1.rate_hw(student_2,'Python', 9)
reviewer_1.rate_hw(student_2, 'Git', 8)

lecturer_1 = Lecturer('Albert', 'Einstein')
lecturer_1.courses_attached += ['Python']
lecturer_2 = Lecturer('Nicola', 'Tesla')
lecturer_2.courses_attached += ['Python']

student_1.rate_lecturer(lecturer_1, 'Python', '8')
student_1.rate_lecturer(lecturer_2, 'Python', '9')
student_2.rate_lecturer(lecturer_1, 'Python', '6')
student_2.rate_lecturer(lecturer_2, 'Python', '5')

result_1 = average_student([student_1, student_2], 'Python')
result_2 = average_lecturer([lecturer_1, lecturer_2], 'Python')

print('')
print(reviewer_1)
print('')
print(lecturer_1)
print('')
print(student_1)
print('')
print(student_2)
print('')
print(student_1 > student_2)
print(lecturer_1 < lecturer_2)
print('')
print(f'Средняя оценка у студентов: {result_1}')
print(f'Средняя оценка у лекторов: {result_2}')
