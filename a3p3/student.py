# JTSK-350112
# a3 3.py
# Wossen Hailemariam
# w.hailemariam@jacobs-university.de


import sys

class Student(object):
    def __init__(self, firstname,lastname,nationality):
        self._firstname = firstname
        self._lastname = lastname
        self._nationality = nationality

    def setFirstName(self, firstname):
        self._firstname = firstname
    
    def getFirstName(self):
        return self._firstname

    def setLastName(self, lastname):
        self._lastname = lasttname

    def getLastName(self):
        return self._lastname

    def setNationalityt(self, nationality):
        self._nationality = nationality

    def getFirstName(self):
        return self._nationality

    def __str__(self):
        """Returns the string representation of the student."""
        return "First Name: " + self._firstname +"\nLast Name: " +\
             self._lastname+ "\nSize: " + str(sys.getsizeof(self))