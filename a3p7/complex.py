# JTSK-350112
# a3 7.py
# wossen Hailemariam
# w.hailemariam@jacobs-university.de

class Complex(object):
    def __init__(self,a, b):
        self.a = a
        self.b = b


        """adding of two objects"""
    def __add__(self,other):
        sum1 = self.a + other.a
        sum2 = self.b + other.b
        return sum1, sum2



        """subtracting of two objects"""
    def __sub__(self,other):
        sub1 = self.a - other.a
        sub2 = self.b - other.b
        return sub1, sub2


        """multiplying of two objects"""
    def __mul__(self,other):
        mult1 = self.a*other.a - self.b*other.b
        mult2 = self.a*other.b + self.b*other.a
        return mult1, mult2


        """dividing of two objects"""
    def __div__(self,other):
        nume1 = self.a*other.a + self.b*other.b
        nume2 = self.b*other.a - self.a*other.b
        deno = other.a*other.a + other.b*other.b

        div1 = nume1/deno
        div2 = nume2/deno
        div = div1, div2
        return div


        """equal?? of two objects"""
    def __eq__(self,other):
        if self.a == other.a and self.b == other.b:
            return True
        else:
            return False

        
        """not equal?? of two objects"""
    def __ne__(self,other):
        if self.a != other.a or self.b != other.b:
            return True
        else:
            return False



        """printing"""
    def __str__(self): 
        return "COMPLEX NUMBER:"\
            "\n"+ str(self.a) + " + "+str(self.b) + "i"\
          
