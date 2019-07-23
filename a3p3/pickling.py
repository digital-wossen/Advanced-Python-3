# JTSK-350112
# a3 3.py
# Wossen Hailemariam
# w.hailemariam@jacobs-university.de

import pickle
from student import Student


# store data --- serialize

obj = Student('Wossen', 'Hailemariam', 'Ethiopian')
print(obj)

fileobj = open('object.txt', 'wb')
pickle.dump(obj, fileobj)
fileobj.close()
