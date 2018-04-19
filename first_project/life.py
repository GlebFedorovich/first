import copy
#считываем файл
text=open('input.txt','r')
f= open("output.txt", "w")
strlist=text.readlines()
list0=list(strlist[0].split())
high,wide=int(list0[1]),int(list0[0])
#преоразуем считанные данные в поле для игры двухуровневым списком
field=[]
for i in range(1,high+1):
    s=[]
    for j in range(0,wide):
        s.append(int(strlist[i][j]))
    field.append(s)

repeat=1
#ограничиваем количество итерации 10, можно поставить и больше
while repeat<=10:
    old=copy.deepcopy(field)
    for j in range(high):#проверяем сколько соседей и какая это потенциально клетка 2-клетка родится 3-умрет
        for i in range(wide):
            count=0
            if (i-1 >= 0) and (j-1 >= 0):
                if field[j-1][i-1]==1 or field[j-1][i-1]==3:
                    count=count+1
            if (j - 1 >= 0):
                if field[j-1][i] == 1 or field[j-1][i] == 3:
                    count = count + 1
            if (i+1<=wide-1) and (j-1>=0):
                if field[j-1][i+1]==1 or field[j-1][i+1]==3:
                    count=count+1
            if (i+1<=wide-1):
                if field[j][i+1]==1 or field[j][i+1]==3:
                    count=count+1
            if (i+1<=wide-1) and (j+1<=high-1):
                if field[j+1][i+1]==1 or field[j+1][i+1]==3:
                    count=count+1
            if (j+1<=high-1):
                if field[j+1][i]==1 or int(field[j+1][i])==3:
                    count=count+1
            if (i-1 >=0) and (j+1<=high-1):
                if field[j+1][i-1]== 1 or field[j+1][i-1] == 3:
                    count = count + 1
            if (i-1 >= 0):
                if field[j][i-1]== 1 or field[j][i-1] == 3:
                    count = count + 1

            if field[j][i]==0:
                if count==3:
                   field[j][i]=2
            if field[j][i]==1:
                if count<2 or count>3:
                   field[j][i]=3
    if old==field:#проверяем на совпадение с прерыдущим ходом, вдруг статическая ситуация получилась
        print("static Life",file=f)
        exit()
    for x in range(0,high):#выводим поле
        for y in range(0,wide):
            if int(field[x][y])==3:
                field[x][y]=0
            if int(field[x][y])==2:
                field[x][y]=1
            print(int(field[x][y]),end=' ',file=f)
        print(file=f)
    print(file=f)

    repeat=repeat+1
f.close()