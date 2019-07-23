# JTSK-350112
# a3 3.py
# Wossen Hailemariam
# w.hailemariam@jacobs-university.de



import pickle
import sys
from student import Student



#load data  ---  deserialize
fileobj = open('object.txt', 'rb')
while True:
    try:
        unserialized_data = pickle.load(fileobj)
    except EOFError:
        fileobj.close()
        break

fileobj.close()
print(unserialized_data)

#reading file line by line and...
fileobject = open('object.txt','r')

while True:
    text =  fileobject.readline()
    if text == '':
        break
    print(text)

f.close()
print("Summed Size:", sis.getsizeof('object.txt'))
