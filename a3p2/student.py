# JTSK-350112
# a3 2.py
# Wossen Hailemariam
# w.haillemarim@jacobs-university.de




"""
File: student.py
Resources to manage a student's name and test scores.
"""
import random

class Student(object):
   """Represents a student."""

   def __init__(self, name, number):
      """All scores are initially 0."""
      self._name = name
      self._scores = []
    

     # for count in range(10):
      #   self._names.append(0)
      for count in range(number):
         self._scores.append(0)

   def getName(self):
      """Returns the student's name."""
      return self._name
  
   def setScore(self, i, score):
      """Resets the ith score, counting from 1."""
      self._scores[i - 1] = score

   def getScore(self, i):
      """Returns the ith score, counting from 1."""
      return self._scores[i - 1]
   
   def getAverage(self):
      """Returns the average score."""
      return sum(self._scores) / len(self._scores)
    
   def getHighScore(self):
      """Returns the highest score."""
      return max(self._scores)
 
   def __str__(self):
      """Returns the string representation of the student."""
      return "Name: " + self._name  + "\nScores: " + \
             " ".join(map(str, self._scores)) +\
            " ".join(map(str, self._names))
                 


   def __eq__(self, other):
       if self._name == other._name and \
           self._scores == other._scores:
           return True     #Object identtty
       else:
           return False

   def __ne__(self, other):
       if self._name != other._name and \
           self._scores != other._scores:
           return True     #Object identtty
       else:
           return False
       

   def __lt__(self, other):
       if self._name < other._name:
           return True
       else:
           return False


   def __le__(self, other):
       if self._name <= other._name:
           return True
       else:
           return False


   def __gt__(self, other):
       if self._name > other._name:
           return True
       else:
           return False


   def __ge__(self, other):
       if self._name >= other._name:
           return True
       else:
           return False


   def shuffle(self):
       """Shuffles the cards."""
       random.shuffle(self._names)

          


