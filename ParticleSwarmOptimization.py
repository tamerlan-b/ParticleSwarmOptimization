import numpy as np
import OptimizationFuncs as of
num_elements = 100

ObjectiveFunc = of.Matyas()

[xmin, xmax, ymin, ymax] = ObjectiveFunc.limits #[-5.0, 5.0, -5.0, 5.0]
xlist = np.linspace(xmin, xmax, num_elements)
ylist = np.linspace(ymin, ymax, num_elements)
X, Y = np.meshgrid(xlist, ylist)

import matplotlib.pyplot as plt

fig = plt.figure(figsize=(6,5))
left, bottom, width, height = 0.1, 0.1, 0.8, 0.8
ax = fig.add_axes([left, bottom, width, height]) 


'''
ax.set_title('Contour Plot')
ax.set_xlabel('x')
ax.set_ylabel('y')
'''

import matplotlib.animation as animation

# Import particle class
from Particle import Particle
#from OptimizationFuncs import Functions


num_particles = 10
particles = Particle.generate_particles(num_particles, xmin, xmax, ymin, ymax)

x_swarm = 1000
y_swarm = 1000
min_swarm = 100000

def pso_step(func):
    global min_swarm, y_swarm, x_swarm
    # Находим лучшую точку роя
    for p in particles:
        value = func(p.x, p.y)
        if value < min_swarm:
            x_swarm = p.x
            y_swarm = p.y
            min_swarm = value

    # Делаем шаг роем
    for p in particles:
        p.step(x_swarm, y_swarm, func)

# ObjectiveFunc = Functions.Rastrigin
#ObjectiveFunc = of.Rastrigin()

Z = ObjectiveFunc(X,Y)

def init():
    ax.clear()
    cp = ax.contourf(X, Y, Z, cmap = plt.cm.terrain)
    plt.colorbar(cp)

def update_plot(i):
    ax.clear()
    ax.set_title('Contour Plot')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    cp = ax.contourf(X, Y, Z, cmap = plt.cm.terrain)

    # Рисуем частицы на графике
    particles_x = []
    particles_y = []
    for p in particles:
        particles_x.append(p.x)
        particles_y.append(p.y)
    line = ax.scatter(particles_x, particles_y, marker='*', color='black')

    print("Swarm min: (%d, %d) : %d"%(x_swarm, y_swarm, min_swarm))
    
    # Делаем шаг алгоритма
    pso_step(ObjectiveFunc)

'''
eps = 0.5
dist_to_min = np.sqrt(np.abs(x_swarm - ObjectiveFunc.x_min)**2 + np.abs(y_swarm - ObjectiveFunc.y_min)**2)

distances = []
iterations = 0
max_iterations = 500
while dist_to_min > eps and iterations <= max_iterations:
    pso_step(ObjectiveFunc)
    dist_to_min = np.sqrt(np.abs(x_swarm - ObjectiveFunc.x_min)**2 + np.abs(y_swarm - ObjectiveFunc.y_min)**2)
    distances.append(dist_to_min)
    iterations += 1
    print('Dist: ' + str(dist_to_min))
plt.grid(True)
plt.plot(np.arange(len(distances)), distances)
'''

ani = animation.FuncAnimation(fig, update_plot, init_func=init,interval=300)
p = plt.show()




