#!/usr/bin/env python
# coding=utf-8

import fire
import numpy as np
import OptimizationFuncs as of
import matplotlib.pyplot as plt
from Particle import OptimizerPSO
import matplotlib.animation as animation

class Visualizer:
    """Класс для визуализации работы алгоритма PSO"""

    def __init__(self, optimizer, num_elements=100):
        # Формирование сетки для рисования функции
        [xmin, xmax, ymin, ymax] = optimizer.objective.limits
        xlist = np.linspace(xmin, xmax, num_elements)
        ylist = np.linspace(ymin, ymax, num_elements)
        self.X, self.Y = np.meshgrid(xlist, ylist)
        # Создаем картинку для функции
        self.fig = plt.figure(figsize=(6, 5))
        left, bottom, width, height = 0.1, 0.1, 0.8, 0.8
        self.ax = self.fig.add_axes([left, bottom, width, height])
        self.cmap = plt.cm.terrain
        # Задаем оптимизатор
        self.optimizer = optimizer
        self.Z = self.optimizer.objective(self.X, self.Y)

    def init(self):
        """Рисует функцию при старте анимации"""
        self.ax.clear()
        cp = self.ax.contourf(self.X, self.Y, self.Z, cmap=self.cmap)
        plt.colorbar(cp)

    def draw_particles(self):
        """Рисует частицы на графике"""
        swarm_position = [[p.x, p.y] for p in self.optimizer.particles]
        particles_x, particles_y = list(zip(*swarm_position))
        line = self.ax.scatter(particles_x, particles_y, marker="*", color="black")

    def decorator(func):
        """Декартор, выводящий точку минимума

        Args:
            func (Callable): декорируемая функцция
        """

        def wrapper(self, i):
            func(self, i)
            if self.verbose:
                print(
                    "Swarm min: ({0}, {1}) : {2}".format(
                        round(self.optimizer.best_x, 3),
                        round(self.optimizer.best_y, 3),
                        round(self.optimizer.best_val, 3),
                    )
                )

        return wrapper

    def prepare_plot(self):
        """Рисует график функции и добавляет подписи к нему"""
        self.ax.clear()
        cp = self.ax.contourf(self.X, self.Y, self.Z, cmap=self.cmap)

        # Добавляем название функции
        self.ax.set_title("{0} function".format(self.optimizer.objective))
        # Подписываем оси координат
        self.ax.set_xlabel("x")
        self.ax.set_ylabel("y")

    @decorator
    def update_plot(self, i):
        """Рисует целевую функцию и положение частиц при обновлении анимации,
        выводит целевую точку в консоль

        Args:
            i (int): номер вызова функции
        """
        # Рисуем график
        self.prepare_plot()

        # Рисуем частицы на графике
        self.draw_particles()

        # Делаем шаг алгоритма
        self.optimizer.step()

    def run_animation(self, frames=30, interval=300, verbose=True):
        self.verbose = verbose
        ani = animation.FuncAnimation(
            self.fig,
            self.update_plot,
            init_func=self.init,
            frames=frames,
            interval=interval,
        )
        plt.show()


def run_cli(num_particles=15, verbose=False):
    """Запускает алгоритм PSO вместе с визуализацией

    Args:
        num_particles (int, optional): количество частиц в рое. Defaults to 15.
        verbose (bool, optional): вывод информации о текущем найденном минимуме. Defaults to False.
    """
    # Создаем тестовую функцию
    objective = of.Rastrigin()
    # Создаем PSO оптимизатор
    pso_optimizer = OptimizerPSO(optimization_func=objective)
    # Генерируем рой частиц
    pso_optimizer.generate_particles(num_particles=num_particles)
    # Создаем визуализатор
    vis = Visualizer(pso_optimizer)
    # Запускаем анимацию оптимизации
    vis.run_animation(verbose=verbose)


if __name__ == "__main__":
    fire.Fire(run_cli)
