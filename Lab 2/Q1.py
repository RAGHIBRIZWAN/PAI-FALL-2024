def areaTrap(a,b,h):
    area = ((a + b)/2) * h
    return area

def areaParallel(b,h):
    area = b * h
    return area
    
def areaCyl(r,h):
    area  = 2*(3.14)*r*h + 2 *3.14*r*r
    return area
    
def volCyl(r,h):
    area = 3.14*r*r*h
    return area

a = int(input('Enter the value for trapezoid: '))
b = int(input('Enter the value for base: '))
r = int(input('Enter the radius: '))
h = int(input('Enter the height: '))

print(areaTrap(a,b,h))
print(areaParallel(b,h))
print(areaCyl(r,h))
print(volCyl(r,h))
