#!/usr/bin/env python
#coding=utf-8

import numpy as np
from Particle import OptimizerPSO, Particle
import OptimizationFuncs as of
import matplotlib.pyplot as plt
import matplotlib.animation as animation


# TODO: отделить визуализацию от алгоритма


ObjectiveFunc = of.Rastrigin()

# Формирование сетки для рисования функции
num_elements = 100
[xmin, xmax, ymin, ymax] = ObjectiveFunc.limits #[-5.0, 5.0, -5.0, 5.0]
xlist = np.linspace(xmin, xmax, num_elements)
ylist = np.linspace(ymin, ymax, num_elements)
X, Y = np.meshgrid(xlist, ylist)

# Создаем картинку для функции
fig = plt.figure(figsize=(6,5))
left, bottom, width, height = 0.1, 0.1, 0.8, 0.8
ax = fig.add_axes([left, bottom, width, height]) 


# Создаем рой частиц
num_particles = 10

# Минимальная точка, найденная роем
x_swarm = 1000
y_swarm = 1000
min_swarm = 100000

Z = ObjectiveFunc(X,Y)

pso = OptimizerPSO(num_particles, ObjectiveFunc)

def init():
    ax.clear()
    cp = ax.contourf(X, Y, Z, cmap = plt.cm.terrain)
    plt.colorbar(cp)

def update_plot(i):
    ax.clear()
    # Имя функции
    # TODO: переопределить метод str()
    ax.set_title('{0} function'.format(type(ObjectiveFunc).__name__))
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    cp = ax.contourf(X, Y, Z, cmap = plt.cm.terrain)
    
    swarm_position = [[p.x, p.y] for p in pso.particles]
    particles_x, particles_y = list(zip(*swarm_position))
    line = ax.scatter(particles_x, particles_y, marker='*', color='black')

    # TODO: только если выставлен флаг verbose
    print("Swarm min: ({0}, {1}) : {2}".format(pso.best_x, pso.best_y, pso.best_val))
    
    # Делаем шаг алгоритма
    pso.step()

if __name__ == "__main__":
    ani = animation.FuncAnimation(fig, update_plot, init_func=init, frames=30, interval=300)
    p = plt.show()




