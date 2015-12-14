#Предложение с большим кол-вом одинаковых слов
def SameW(s):
    s = s.split('.')
    a = 0
    imax = 0
    for i in range(len(s)):
        s1 = s[i].split()
        for j in range(len(s1)):
            if s1.count(s1[j]) > a:
                a = s1.count(s1[j])
                imax = i
    return s[imax] 
                


matrix = [] 
matrix.append('Сергей пишет программы и учит математику. ')
matrix.append('такс такс такс.')
matrix.append('')


for i in range(len(matrix)): 
    print(matrix[i],end=' ') 

s = '' 
for i in range(len(matrix)): 
    for j in range(len(matrix[i])): 
        s = s + matrix[i][j]

print() 
print('"',SameW(s),'"')
