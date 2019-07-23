# JTSK-350112
# a3 1.py
# Wossen Hailemariam
# w.haillemarim@jacobs-university.de



from student import Student



Ob1 = Student("katy", 2) #by changing the inputs we can check
Student.setScore(Ob1, 1,100)
Student.setScore(Ob1, 2,90)


Ob2 = Student("katy", 2) 
Student.setScore(Ob2, 1,80)
Student.setScore(Ob2, 2,90)

print(Ob1)
print(Ob2) 


print(Ob1 == Ob2)
print(Ob1 != Ob2)


print(Ob1 < Ob2)
print(Ob1 <= Ob2)
print(Ob1 > Ob2)
print(Ob1 >= Ob2)
