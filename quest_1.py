# My function's
def avg_from_dict(dictionary): # Extract average from dict value's
    if len(dictionary) > 0:
        summ = 0
        amount = 0
        for rates in dictionary.values():
            summ += sum(rates)
            amount += len(rates)
        avg = summ / amount
        return avg
# Creating class - Student
class Student:
    students_list = []
    def __init__(self, name, surname, gender):
        self.students_list.append(self)
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.avg = 0
    def lecture_rate(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.lecturer_rates:
                lecturer.lecturer_rates[course].append(int(grade))
                lecturer.avg = avg_from_dict(lecturer.lecturer_rates)
            else:
                lecturer.lecturer_rates[course] = [int(grade)]
                lecturer.avg = avg_from_dict(lecturer.lecturer_rates)
        else:
            print('Error')
    
    def __str__(self):
        res = f'''Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за домащнее задание: {avg_from_dict(self.grades)}
Курсы в процессе изучения: {", ".join(self.courses_in_progress)}
Заверщенные курсы{", ".join(self.finished_courses)}'''
        return res
    
    def __lt__(self,other):
        if not isinstance(other, Student):
            return f'Not a Student!'
        else:
            return self.avg < other.avg
# Creating class - Mentor
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
# Creating class - Lecturer (Mentor)
class Lecturer(Mentor):
    lecturers_list = []
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lecturers_list.append(self)
        self.lecturer_rates = {}
        self.avg = 0
    def __str__(self):
            res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции:{self.avg}'
            return res
    def __lt__(self,other):
        if not isinstance(other, Lecturer):
            return f'Not a Lecturer!'
        else:
            return self.avg < other.avg
# Creating class - Reviewer (Mentor)
class Reviewer(Mentor):
        def rate_hw(self, student, course, grade):
            if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
                if course in student.grades:
                    student.grades[course] += [grade]
                    student.avg = avg_from_dict(student.grades)
                else:
                    student.grades[course] = [grade]
                    student.avg = avg_from_dict(student.grades)
            else:
                return 'Ошибка'
        def __str__(self):
            res = f'Имя: {self.name}\nФамилия: {self.surname}'
            return res
# Creating class examples
lecturer_1 = Lecturer('Old','Dude')
lecturer_2 = Lecturer('Second','Secondson')
first_student = Student('Bob', 'Fatherson', 'male')
second_student = Student('Ginny', 'Weasley', 'female')
reviewer_1 = Reviewer('Rev','Viewer')
reviewer_2 = Reviewer('Ver','Reweiv')
# Adding courses
first_student.courses_in_progress += ['Python'] + ['Java']
first_student.finished_courses += ['C++']
second_student.courses_in_progress += ['Java'] + ['Python'] + ['PHP']
lecturer_1.courses_attached += ['Java'] + ['Python'] + ['PHP'] + ['C++']
lecturer_2.courses_attached += ['Java'] + ['Python']
reviewer_1.courses_attached += ['PHP'] + ['C++']
reviewer_2.courses_attached += ['Java'] + ['Python']
# Using class method's - rate the Lecturer
first_student.lecture_rate( lecturer_2, 'Java', 8)
second_student.lecture_rate( lecturer_1, 'Python', 10)
second_student.lecture_rate( lecturer_1, 'Python', 3)

# rate the students
reviewer_2.rate_hw( first_student, 'Python', 7)
reviewer_1.rate_hw( second_student, 'PHP', 10)
reviewer_1.rate_hw( second_student, 'PHP', 6)
reviewer_2.rate_hw( second_student, 'Python', 10)
reviewer_2.rate_hw( first_student, 'Python', 3)

print(lecturer_1) # Check str format
print(lecturer_1 < lecturer_2) # Check __Lt__ in lecturer
print(first_student < second_student) # Check __lt__ in student

#### tasks number 4
# average on students
std_list = [first_student,second_student]
def course_score(list = std_list,course = 'Python'):
    course_score = {}
    for i in list:
        for keys,values in i.grades.items():
            if keys in course_score:
                course_score[keys] += values
            else:
                course_score[keys] = values
    ans = sum(course_score[course]) / len(course_score[course])
    ans = float('{:.2f}'.format(ans))
    print(ans)
course_score()

# average on lect
lect_list = [lecturer_1,lecturer_2]
def lect_course_score(list = lect_list,course = 'Python'):
    lect_course_score = {}
    for i in list:
        for keys,values in i.lecturer_rates.items():
            if keys in lect_course_score:
                lect_course_score[keys] += values
            else:
                lect_course_score[keys] = values
    ans = sum(lect_course_score[course]) / len(lect_course_score[course])
    ans = float('{:.2f}'.format(ans))
    print(ans)
lect_course_score()











