from math import *
def f(x):
    return cos(x)*x - 2

def LeftPr(a,b,n):
    h = (b - a) / n
    Integ = 0
    x = a
    for i in range(n-1):
        Integ = Integ + f(x)
        x = x + h
    Integ = Integ * h
    return Integ

def precision(Integ):
     n = 1
     while abs(LeftPr(a,b,n) - LeftPr(a,b,n * 2)) > eps:
          n = n * 2
     print('Ответ для заданной точности: ',LeftPr(a,b,n))
     print('При разбиении на',n,'интервалов')

a = int(input('Введите начало отрезка интегрирования: '))
b = int(input('Введите конец отрезка интегрирования: '))
n = int(input('Введите количество разбиений: '))
eps = float(input('Введите точность: '))

precision(LeftPr(a,b,n))
print(LeftPr(0,1,500))
