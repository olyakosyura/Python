def Minword(s): 
    s = s.split('.') 
    iminn = 0 
    minn = 10000
    for i in range(len(s)): 
        s1 = s[i].split()
        for j in range(len(s1)):
            if minn > len(s1[j]):
                minn = len(s1[j])
                iminn = i 
    return s[iminn] 


X = [] 


matrix = [] 
matrix.append('Раму мыла мама. Мыла раму мама. Ну а Маша-растеряша ') 
matrix.append('окна не помыла. За окном скворечник. Его сделал папа. Папа любит маму, ') 
matrix.append('которая моет раму. Со мной живут мама и папа. А еще живет сестра Маша. Наша Маша - растеряша, ') 
matrix.append('она часто теряет вещи. А я помогаю их искать. Вместе мы их всегда ') 
matrix.append('находим. Вот и кончился рассказ. Всем большое спасибо.') 


for i in range(len(matrix)): 
    print(matrix[i],end=' ') 

s = '' 
for i in range(len(matrix)): 
    for j in range(len(matrix[i])): 
        s = s + matrix[i][j] 
print() 
print('"',Minword(s),'"')
