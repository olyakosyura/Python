def f(x):
    return x**2
 
def left_rectaugle(a,b,n):
    h = (b-a)/n
    Integ = 0
    x = a
    for i in range (n-1):
        Integ = Integ+f(x)
        x = x + h
    Integ=Integ*h
    return Integ
 
def trapetc(a,b,n):
    h = (b-a)/n
    Integ = 0
    x = a 
    for i in range (1,n-1):
        Integ = Integ+f(x)
        x = x+h  
    f2 = f(a)+f(b)
    return h*(f2/2+Integ)
 
# returns (integral, count of intervals)
def trapetcWithAccuracy(a, b, eps, n):   
    while abs(trapetc(a, b, n) - trapetc(a, b, n*2)) > eps:
        n *= 2
        
    return trapetc(a, b, n)
 
# returns (integral, count of intervals)
def left_rectaugleWithAccuracy(Integ,n):
    while abs(left_rectaugle(a, b, n) - left_rectaugle(a, b, n*2)) > eps:
        n *= 2
        
    return left_rectaugle(a, b, n)
 
a = float(input('Нижний предел интегрирования = '))
b = float(input('Верхний предел интегрирования = '))
n1 = int(input('N1: '))
n2 = int(input('N2: '))

eps = float(input("Eps: "))

print('--------------------------------------------------------------')
print('| Метод                        |    n1 = {:4} |    n2 = {:4} |'.format(n1,n2))


i1 = trapetcWithAccuracy(a, b, eps,n1)
i2 = trapetcWithAccuracy(a, b, eps,n2)

j1 = left_rectaugleWithAccuracy(left_rectaugle(a,b,n1),n1)
j2 = left_rectaugleWithAccuracy(left_rectaugle(a,b,n2),n2)

print('| Метод Трапеции:              | {:12.6} | {:12.6} |'.format(i1,i2))
print('| Метод Левых прямоугольников: | {:12.6} | {:12.6} |'.format(j1,j2))
print('--------------------------------------------------------------')
