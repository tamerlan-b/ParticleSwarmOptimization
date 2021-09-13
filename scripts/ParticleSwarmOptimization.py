#!/usr/bin/env python
#coding=utf-8

import numpy as np
from Particle import OptimizerPSO, Particle
import OptimizationFuncs as of
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class Visualizer:
    def __init__(self, optimizer, num_elements=100):
        # Формирование сетки для рисования функции
        [xmin, xmax, ymin, ymax] = optimizer.objective.limits
        xlist = np.linspace(xmin, xmax, num_elements)
        ylist = np.linspace(ymin, ymax, num_elements)
        self.X, self.Y = np.meshgrid(xlist, ylist)
        # Создаем картинку для функции
        self.fig = plt.figure(figsize=(6,5))
        left, bottom, width, height = 0.1, 0.1, 0.8, 0.8
        self.ax = self.fig.add_axes([left, bottom, width, height])
        self.cmap = plt.cm.terrain
        # Задаем оптимизатор
        self.optimizer = optimizer
        self.Z = self.optimizer.objective(self.X,self.Y)


    def init(self):
        """Рисует функцию при старте анимации"""

        self.ax.clear()
        cp = self.ax.contourf(self.X, self.Y, self.Z, cmap = self.cmap)
        plt.colorbar(cp)

    def update_plot(self, i):
        """Рисует целевую функцию и положение частиц при обновлении анимации,
        выводит целевую точку в консоль

        Args:
            i (int): номер вызова функции
        """
        self.ax.clear()
        cp = self.ax.contourf(self.X, self.Y, self.Z, cmap = self.cmap)
        
        # Добавляем название функции
        self.ax.set_title('{0} function'.format(self.optimizer.objective))
        # Подписываем оси координат
        self.ax.set_xlabel('x')
        self.ax.set_ylabel('y')
        
        # Рисуем частицы на графике
        swarm_position = [[p.x, p.y] for p in self.optimizer.particles]
        particles_x, particles_y = list(zip(*swarm_position))
        line = self.ax.scatter(particles_x, particles_y, marker='*', color='black')

        # TODO: только если выставлен флаг verbose
        print("Swarm min: ({0}, {1}) : {2}".format(self.optimizer.best_x, self.optimizer.best_y, self.optimizer.best_val))
        
        # Делаем шаг алгоритма
        self.optimizer.step()

    def run_animation(self, frames=30, interval=300):
        ani = animation.FuncAnimation(self.fig, self.update_plot, init_func=self.init, frames=frames, interval=interval)
        plt.show()


if __name__ == "__main__":
    # Создаем тестовую функцию
    objective = of.Rastrigin()
    # Создаем PSO оптимизатор
    pso_optimizer = OptimizerPSO(num_particles=20, optimization_func=objective)
    # Создаем визуализатор
    vis = Visualizer(pso_optimizer)
    # Запускаем анимацию оптимизации
    vis.run_animation()




