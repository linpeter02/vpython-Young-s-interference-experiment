import numpy as np
from vpython import*




length=1000
height=100




#光源座標

x1=(length/2)+5
y1=height/2
z1=0
x2=(length/2)-5
y2=height/2
z2=0

#點到屏幕=10000


#波長
Lambda=830*10**(-7)





a=np.zeros((length*height,3))
p1=np.zeros((length*height,3))
p2=np.zeros((length*height,3))


for i in range(length*height):

    a[i][2]=10000
    
    p1[i][0]=x1
    p1[i][1]=y1
    p1[i][2]=z1

    p2[i][0]=x2
    p2[i][1]=y2
    p2[i][2]=z2
    



#終止點座標
for j in range(0,height,1):
    for k in range(0,length,1):
        a[k+length*j][1]=j
        a[k+length*j][0]=k



L1=np.zeros((length*height,3))
L2=np.zeros((length*height,3))


L1=a[:]-p1[:]
L2=a[:]-p2[:]


delta_L1=np.zeros(length*height)
delta_L2=np.zeros(length*height)
phase=np.zeros(length*height)


#點到屏幕距離
for f in range(length*height):
    
    delta_L1[f]= ((L1[f][0]**2)+(L1[f][1]**2)+(L1[f][2]**2))**0.5
    delta_L2[f]= ((L2[f][0]**2)+(L2[f][1]**2)+(L2[f][2]**2))**0.5
    
#求出疊加的相位角    
phase=(abs (((delta_L2-delta_L1)% Lambda)-0.5*Lambda))


#畫圖
scene = canvas(width=1200, height = 600,center=vec(length/2,height/2,0),background=vec(0,0,1)) 
boxs = [box(length=1,width=1,height=1,pos=vec(a[L][0],a[L][1],a[L][2]),color=vec(phase[L]*2/Lambda,0,0)) for L in range(length*height)]
































