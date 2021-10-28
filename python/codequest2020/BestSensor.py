import sys
import math

def distance_3D(x1,x2,y1,y2,z1,z2): 
    return (((x2-x1)**2)+((y2-y1)**2)+((z2-z1)**2)) ** (0.5)

def reg_round(n, dp):
    n *= 10 ** dp
    if n - math.floor(n) < 0.5: 
        return math.floor(n)/10 ** dp
    return math.ceil(n)/10 ** dp

class Sensor():
    def __init__(self, name, x, y, z, d_f_av=0):
        self.name = name
        self.x = x
        self.y = y
        self.z = z

def solve(index, final):
    n = int(sys.stdin.readline().strip())
    r = []
    x,y,z = [0,0,0]
    for i in range(n):
        s_n, a, b, c = sys.stdin.readline().strip().split()
        d = Sensor(s_n, a, b, c)
        r.append(d)
        x += int(a)
        y += int(b)
        z += int(c)
    x /= n
    y /= n
    z /= n
    for sensor in r:
        sensor.d_f_av = distance_3D(float(sensor.x),x,float(sensor.y),y,float(sensor.z),z)
    r.sort(key=lambda x : x.d_f_av)
    print(f'{r[0].name} {reg_round(x,3):.3f} {reg_round(y,3):.3f} {reg_round(z,3)}')

count = int(sys.stdin.readline().strip())
for i in range(count):
    solve(i+1, i == count-1)