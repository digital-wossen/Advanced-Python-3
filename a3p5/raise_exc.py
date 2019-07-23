# JTSK-350112
# a3 1.py
# Wossen Hailemariam
# w.hailemariam@jacobs-university.de


class A(Exception): pass

def check_one(n):
    """Raises Error for parameter One."""
    if n == 1:
        raise A("999")
    else: 
        pass

class B(Exception): pass

def check_two(n):
    """Raises Error for parameter two."""
    if n == 2:
        raise B("Error has happend")
    else:
        pass



class C(Exception): pass

def check_three(n):
    """Raises Error for parameter three."""
    if n == 3:
        raise C("1.23")
    else:
        pass







def something(num):
    for cls in [A,B,C]:
        try:
            raise cls()
        except A as exc:
            print(exc)
        except B as exc:
            print(exc)
        except C as exc:
            print(exc)
        else:
            print("No Error")
        finally:
            print("\nRAISE EXEPTIONS")
    #the question says to in


something(2)
#something()
#something()
#something()
#something()

#num = int(input())