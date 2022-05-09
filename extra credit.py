import matplotlib.pyplot as plt
import numpy as np
import random
import math

def accuracy():
    success=0
    test=[]
    succ=[]
    died_outside_1km=[]
    mos_outside_1km=0
    for run in range(1,1000001):
        for z in range(10):
            a=random.randint(0, 360)
            if z==0:
                x=250*math.cos(a) # Polar Coordinates formula x = r cos 0
                y=250*math.sin(a) # Polar Coordinates formula y = r sin 0
            else:
                x+=250*math.cos(a)
                y+=250*math.sin(a)
            d1 = math.sqrt((x-0)**2 + (y-200)**2) # Distance formula d=square_root((x-h)^2 + (y-k)^2)
            d2 = math.sqrt((x)**2+(y)**2)
            if d2>1000:
                mos_outside_1km +=1
            if d1<50:
                success+=1
                break
        acc_for_succ=success/run
        died_1km_out=mos_outside_1km/run
        test.append(run)
        succ.append(acc_for_succ)
        died_outside_1km.append(died_1km_out)
    x_point=np.array(test)
    y_point=np.array(succ)
    z_point=np.array(died_outside_1km)
    plt.plot(x_point, y_point)
    plt.plot(x_point, z_point)
    plt.show()
    acc_for_succ=success/1000000
    print("Out of 1 Million run, It has been succedded only {0}, so Mosquito has probability of {1} times to find the host".format(success,acc_for_succ))
    died_1km_out=mos_outside_1km/1000000
    print("Out of 1 Million run, It has been died outside 1km is {0}, so Mosquito has probability of {1} to die outside 1Km".format(mos_outside_1km,died_1km_out))


def monti_carlo_mosquito():
    fig,ax=plt.subplots()
    ax.set_xlim(-1500,1500)
    ax.set_ylim(-1500,1500)
    x1,x2=[0,0],[1500,-1500]
    y1,y2=[1500,-1500],[0,0]
    plt.plot(x1,y1)
    plt.plot(x2,y2)
    outer_circle = plt.Circle((0,0 ), 1000, fill = False)
    ax.set_aspect( 1 )
    ax.add_artist( outer_circle )
    Drawing_uncolored_circle = plt.Circle((0, 200 ), 50, fill = False)
    ax.set_aspect( 1 )
    ax.add_artist( Drawing_uncolored_circle )
    for z in range(10):
        a=random.randint(0, 360)
        if z==0:
            x=250*math.cos(a)# Polar Coordinates formula x = r cos 0
            y=250*math.sin(a)# Polar Coordinates formula y = r sin 0
        else:
            x+=250*math.cos(a)
            y+=250*math.sin(a)
        point_1=x1
        point_2=[x,y]
        x_value=[point_1[0],point_2[0]]
        y_value=[point_1[1],point_2[1]]
        plt.plot(x_value,y_value)
        x1=point_2
        d = math.sqrt((x-0)**2 + (y-200)**2) # Distance formula d=square_root((x-h)^2 + (y-k)^2)
        if d<=50:
            plt.show()
            return "Mosquito finds the host on day {0}".format(z+1)
    plt.show()
    return "Mosquito Died, It can't find the host"

    
print(monti_carlo_mosquito())
accuracy()
