NAMES = ('wossen', 'kirubel', 'henok', 'hailemariam')
SCORES = ( 5,4,3,2,1)


class Student(object):
   """Represents a student."""

   def __init__(self, name, number):
      """All scores are initially 0."""
      self._name = name
      self._scores = []



class Stud(object):
    
    def __init__(self):
        
        self._names = []
        for name in NAMES:
            for score in SCORES:
                c = Student(name, score)
                self._names.append(c)

for i in range (10):
    print ('obj',i)      