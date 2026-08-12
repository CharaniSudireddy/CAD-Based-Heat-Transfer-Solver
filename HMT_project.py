import ezdxf 
import numpy as np
import matplotlib.pyplot as plt   
from matplotlib.path import Path   

filename=input("Enter your file name: ")
doc=ezdxf.readfile(filename)
msp=doc.modelspace()
points=[]   

for e in msp.query("LINE"):
    points.append([e.dxf.start.x, e.dxf.start.y])   
    points.append([e.dxf.end.x, e.dxf.end.y])

for e in msp.query("LWPOLYLINE"):
    for p in e.get_points():
        points.append([p[0], p[1]])

for e in msp.query("POLYLINE"):
    for v in e.vertices:
        points.append([v.dxf.location.x, v.dxf.location.y])  

for e in msp.query("SPLINE"):   
    for p in e.control_points:   
        points.append([p[0], p[1]])

for e in msp.query("CIRCLE"):
    cx = e.dxf.center.x
    cy = e.dxf.center.y
    r = e.dxf.radius
    for i in np.linspace(0, 2*np.pi, 50):
        x = cx + r*np.cos(i)
        y = cy + r*np.sin(i)
        points.append([x,y])

if len(points) == 0:
    print("No usable geometry detected.")
    exit()

points = np.array(points)

x_min, x_max = np.min(points[:,0]), np.max(points[:,0])
y_min, y_max = np.min(points[:,1]), np.max(points[:,1])

print("Box:", x_min, x_max, y_min, y_max)

n = int(input("Enter node grid size = "))

x = np.linspace(x_min, x_max, n)
y = np.linspace(y_min, y_max, n)

T = np.zeros((n,n))

top = float(input("Top temperature: "))
bottom = float(input("Bottom temperature: "))
left = float(input("Left temperature: "))
right = float(input("Right temperature: "))

T[0,:] = top
T[-1,:] = bottom
T[:,0] = left
T[:,-1] = right

for _ in range(4000):
    T_new = T.copy()
    for i in range(1,n-1):
        for j in range(1,n-1):
            T_new[i,j] = 0.25*(T[i+1,j] + T[i-1,j] + T[i,j+1] + T[i,j-1])
    T = T_new

node = 1
print("\nNode Temperatures")
for i in range(n):
    for j in range(n):
        print(f"Node {node}  T={T[i,j]:.2f}") 
        node += 1

Ty, Tx = np.gradient(T) 
grad_mag = np.sqrt(Tx**2 + Ty**2)  
polygon = Path(points) 
X, Y = np.meshgrid(x, y) 
inside = polygon.contains_points(
    np.vstack((X.flatten(), Y.flatten())).T 
)
inside = inside.reshape(X.shape)
T_masked = np.ma.array(T, mask=~inside) 
plt.contourf(X, Y, T_masked, levels=60, cmap="jet") 
plt.colorbar(label="Temperature")
plt.title("Temperature Distribution Inside Shape")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()