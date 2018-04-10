# a, b = map(int, input().split())
# x1 = list(map(int, input().split()))
import time
def checkpossibility(field,i,j,number):
    row=0
    for k in range(0,9):
        if number==field[i][k]:
            return 0
    if row==0:
        col = 0
        for k in range(0, 9):
            if number == field[k][j]:
                return 0
        if col==0:
            squarex=(i//3)*3
            squarey=(j//3)*3
            for x in range(squarex,squarex+3):
                for y in range(squarey,squarey+3):
                    if field[x][y]==number:
                        return 0
            return 1
        return 0
    return 0

def findstep(field,i,j):
    for x in range(i,9):
        for y in range(j,9):
            if field[x][y]==0:
                return x,y
    for x in range(0,9):
        for y in range(0,9):
            if field[x][y]==0:
                return x,y
    return None,None

def solution(field,i=9,j=9):
    i,j=findstep(field,i,j)
    if (i==None or j==None): return 1
    for number in range(1,10):
        if checkpossibility(field,i,j,number):
            field[i][j]=number
            if solution(field,i,j):
                return 1
            field[i][j]=0
    return 0

text=open('input.txt','r')
strlist=text.readlines()

field=[]
for i in range(0,11):
    if (i%4)!=3:
        s=list(strlist[i].split())
        s=list(int(item) for item in s)
        field.append(s)
start_time = time.time()
solution(field,0,0)

for x in range(9):
    for y in range(9):
        if field[x][y]==0:
            print("NO solution")
            exit()

for x in range(9):
    for y in range(9):
        if (y==3) or (y==6):
            print('|',end=' ')
            print(field[x][y],end=' ')
        else:
            if ((x==3) and (y==0)) or ((x==6) and (y==0)) :
                print(21*'-')
                print(field[x][y],end=' ')
            else:
                print(field[x][y],end=' ')
    print()


print("--- %s seconds ---" % (time.time() - start_time))