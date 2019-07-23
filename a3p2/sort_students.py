# JTSK-350112
# a3 2.py
# Wossen Hailemariam
# w.haillemarim@jacobs-university.de





from student import Student
from random import shuffle
#1
ob1 = Student('Jhon', 3)

Student.setScore(ob1, 1,100)
Student.setScore(ob1, 2,90)
Student.setScore(ob1, 3,50)
#2
ob2 = Student('Thor', 3)

Student.setScore(ob2, 1,40)
Student.setScore(ob2, 2,90)
Student.setScore(ob2, 3,20)
#3
ob3 = Student('Stark', 3)

Student.setScore(ob3, 1,50)
Student.setScore(ob3, 2,20)
Student.setScore(ob3, 3,10)
#4
ob4 = Student('Tony', 3)

Student.setScore(ob4, 1,100)
Student.setScore(ob4, 2,100)
Student.setScore(ob4, 3,100)
#5
ob5 = Student('Rahel', 3)

Student.setScore(ob5, 1,100)
Student.setScore(ob5, 2,99)
Student.setScore(ob5, 3,52)
#6
ob6 = Student('Steve', 3)

Student.setScore(ob6, 1,80)
Student.setScore(ob6, 2,40)
Student.setScore(ob6, 3,52)
#7
ob7 = Student('Will', 3)

Student.setScore(ob7, 1,100)
Student.setScore(ob7, 2,92)
Student.setScore(ob7, 3,88)
#8
ob8 = Student('Adam', 3)

Student.setScore(ob8, 1,100)
Student.setScore(ob8, 2,90)
Student.setScore(ob8, 3,80)

#9
ob9 = Student('Zing', 3)

Student.setScore(ob9, 1,100)
Student.setScore(ob9, 2,80)
Student.setScore(ob9, 3,50)
#10
ob10 = Student('alex', 3)

Student.setScore(ob10, 1,100)
Student.setScore(ob10, 2,90)
Student.setScore(ob10, 3,55)


names = []
info =  ob10._name + ob10._scores
names.append(ob10._name, ob10._scores)



print(names)