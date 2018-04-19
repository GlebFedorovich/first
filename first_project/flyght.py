import math
ship_mass=2150
equipmass=1000
summass=ship_mass+equipmass
g=1.62
speedp=3660
speedx=0
speedy=0
limspeedx=1
limspeedy=3
x=0
y=0
delta_t=0.05 # будем все дробить на участки с "постоянным" ускорением

text=open('input.txt','r') # считываем файлик с траекториями
output=open('output.txt','w')
strlist=text.readlines()
moves=[] # массив движений двумерным списком
for i in range(len(strlist)):
    s=list(strlist[i].split())
    for j in range(len(s)): s[j]=float(s[j])
    moves.append(s)


def one_step(angle1,dm):
    global speedx, speedy, x, y, g,equipmass,delta_t, limitspeedx,limitspeedy,output
    boostx=(math.cos(math.pi*angle1/180)*dm*speedp)/summass
    boosty=(math.sin(math.pi*angle1/180)*dm*speedp)/summass-g
    speedx=speedx+boostx*delta_t
    speedy = speedy + boosty * delta_t
    x = x + speedx * delta_t + boostx * (delta_t*delta_t) / 2
    y = y + speedy * delta_t + boosty * (delta_t*delta_t) / 2
    equipmass=equipmass-dm*delta_t
    if y<0:
        y=0
        if (abs(speedx) > limspeedx) or (-speedy > limspeedy):
            print(round(speedx), round(speedy), round(x), round(y),sep='\t\t', file=output)
            print("Live as a king, die as a hero...", file=output)
        else:
            print(round(speedx), round(speedy), round(x), round(y),sep='\t\t',  file=output)
            print("New GAGARIN!!!", file=output)
        exit()

def one_move(newangle,onedm,onetime):
    global speedx, speedy, x, y, g, equipmass, delta_t, limitspeedx, limitspeedy, output
    for i in range(int(onetime/delta_t)):
        one_step(newangle,onedm)


def mainflyght(moves):
    global speedx, speedy, x, y, g, equipmass, delta_t, limitspeedx, limitspeedy, output
    for i in range(len(moves)):
        one_move(moves[i][0],moves[i][1]/moves[i][2],moves[i][2])
        print(round(speedx), round(speedy), round(x), round(y), sep='\t\t', file=output)
    angle = math.atan2(speedy, speedx) * 180 / math.pi
    print("Odin raz givyom", file=output)
    while y > 0:
        one_step(angle, 0)


mainflyght(moves)
output.close()
