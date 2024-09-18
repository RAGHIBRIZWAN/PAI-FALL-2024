from abc import ABC, abstractmethod

class shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
class rectangle(shape):
    def area(self,x,y):
        return x*y
    
class triangle(shape):
    def area(self,x,y):
        return x*y*0.5
        
class square(shape):
    def area(self,x):
        return x*x
        
r = rectangle()
a = r.area(2,3)
print(a)

t = triangle()
b = t.area(2,3)
print(b)

s = square()
c = s.area(3)
print(c)
