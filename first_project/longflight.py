import math
x=0
y=0
Vx=0
Vy=0
M=2150
g=1.62
lima=29,4
m=1000
Vgas=3660

def one_step(angle, fuelspend, time):
    global x,y,Vx,Vy,m
    x+= Vx * time - Vgas * math.cos(angle * math.pi / 180)*((-(m+M)/fuelspend+time)*math.log((M+m-fuelspend*time)/(m+M))-time)
    y+=Vy*time-g*time*time/2-Vgas * math.sin(angle * math.pi / 180)*((-(m+M)/fuelspend+time)*math.log((M+m-fuelspend*time)/(m+M))-time)
    Vx+=-Vgas*math.cos(angle*math.pi/180)*math.log((m+M-fuelspend*time)/(m+M))
    Vy+=-g*time-Vgas*math.sin(angle*math.pi/180)*math.log((m+M-fuelspend*time)/(m+M))
    m=m-fuelspend*time
    return [Vx,Vy,x,y]
def free_step(time):
    global Vx,Vy,x,y,m
    x=x+Vx*time
    y=y+Vy*time-g*time*time/2
    Vy=Vy-g*time
    return [Vx,Vy,x,y]
dt=0.01
while m>=450:
    newangle=45
    while newangle<=47.5:
        x=one_step(newangle,fuelspend,time)


        newangle=newangle+0.1