import timeit
import sys
def findstep(field):# функция для нахождения нуля на поле, понадобится для проверки в рекусии того, что все поля заполнены
    for x in range(0,n):
        for y in range(0,n):
            if field[x][y]==0:
                return x,y


def listpossibilities(i,j):#фукнция выдает список потенциальных ходов из данной клетки
    x=[-2,-1,1,2,2,1,-1,-2]
    y=[1,2,2,1,-1,-2,-2,-1]
    result=[]
    for k in range(0,8):
        if (i+x[k]>=0) and (i+x[k]<=n-1) and (j+y[k]>=0) and (j+y[k]<=n-1):
            if (field[i+x[k]][j+y[k]]==0):
                result.append([i+x[k],j+y[k]])
    return result


def solution(field,i,j,k):#рекурсивная процедура решения
    t=findstep(field)
    if t==None:
        return 1
    currentlist=listpossibilities(i,j)
    for y in currentlist:
        field[y[0]][y[1]]=k+1
        if solution(field, y[0], y[1],k+1):
            return 1
        field[y[0]][y[1]] = 0
    k=k-1

    return 0
#считывание из файла
text=open('input.txt','r')
strlist=text.readlines()
n=int(strlist[0])
f=open('output.txt','w')
tim=timeit.default_timer()
field=[]
for i in range(1,2*n,2):
    s=list(strlist[i].split())
    s=list(item for item in s)
    field.append(s)
start1=0
start2=0
max1=0
for i in range(0,n):#переход в следующую итерацию
    for j in range(0,n):
        field[i][j]=int(field[i][j])
        if field[i][j]>max1:
            start1=i
            start2=j
            max1=field[i][j]

solution(field,start1,start2,max1)#старт рекурсии
for i in range(0,n):#проверка, что есть решение, иначе после возвращение из рекусии остались нули
    for j in range(0,n):
        if field[i][j]==0:
            print('No solution',file=f)
            exit()

for i in range(0,n):
    for j in range(0,n):
        print(int(field[i][j]),end='\t',file=f)
    print(file=f)

f.close()
