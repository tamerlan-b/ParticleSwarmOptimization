#!/usr/bin/env python
#coding=utf-8

import random

class Particle:
    """Частица роя"""

    def __init__(self, xmin, xmax, ymin, ymax):
        """Создаем частицу и инициализируем начальные значения

        Args:
            xmin (float): нижняя граница по x
            xmax (float): верхняя граница по y
            ymin (float): нижняя граница по x
            ymax (float): верхняя граница по y
        """
        self.x = random.uniform(xmax, xmin)
        self.y = random.uniform(ymax, ymin)
        self.r_m = random.random()
        self.r_g = random.random()
        
        self.f_m = 0.6
        self.f_g = 0.4
        self.w = 0.5
        
        self.x_best = self.x
        self.y_best = self.y
        
        self.vel_x = 0
        self.vel_y = 0

        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax
        
    def calc_vel(self, x_swarm, y_swarm):
        """Вычисляем скорость частицы

        Args:
            x_swarm (float): x-координата роевого минимума
            y_swarm (float): y-координата роевого минимума
        """
        vel_x = self.vel_x * self.w
        vel_x += self.f_m * self.r_m * (self.x_best - self.x)
        vel_x += self.f_g * self.r_g * (x_swarm - self.x)

        vel_y = self.vel_y * self.w
        vel_y += self.f_m * self.r_m * (self.y_best - self.y)
        vel_y += self.f_g * self.r_g * (y_swarm - self.y)

        self.vel_x = vel_x
        self.vel_y = vel_y

    def step(self, x_swarm, y_swarm, func):
        """Делаем шаг частицей роя

        Args:
            x_swarm (float): x-координата роевого минимума
            y_swarm (float): y-координата роевого минимума
            func (Function): оптимизируемая функция
        """
        # Вычисляем скорость
        self.calc_vel(x_swarm, y_swarm)
        # Вычисляем новое положение
        x_new = self.x + self.vel_x
        y_new = self.y + self.vel_y
        # Проверяем не выходит ли новая точка
        # за пределы области
        if x_new >= self.xmin and x_new <= self.xmax:            
            if y_new >= self.ymin and y_new <= self.ymax:
                old_value = func(self.x, self.y)
                new_value = func(x_new, y_new)
                # Перемещаемся в новое положение
                self.x = x_new
                self.y = y_new              
                # Обновляем значение лучшей точки
                if new_value <= old_value:
                    self.x_best = x_new
                    self.y_best = y_new

class OptimizerPSO:
    """PSO оптимизатор"""

    def generate_particles(self, num_particles):
        """Генерирует рой частиц

        Args:
            num_particles (int): количество частиц в рое
        """
        # Количество частиц
        self.num_particles = num_particles
        self.particles = []
        for i in range(self.num_particles):
            p = Particle(self.xmin, self.xmax, self.ymin, self.ymax)
            self.particles.append(p)

    def __init__(self, optimization_func):
        """Создает PSO оптимизатор

        Args:
            optimization_func (Function): оптимизируемая функция
        """
        # Оптимизируемая функция
        self.objective = optimization_func
        # Границы поиска
        [self.xmin, self.xmax, self.ymin, self.ymax] = self.objective.limits
        
        # Точка минимума
        self.best_x = float("inf")
        self.best_y = float("inf")
        self.best_val = float("inf")

    def step(self):
        """Делаем шаг алгоритма"""
        # Находим лучшую точку роя
        for p in self.particles:
            value = self.objective(p.x, p.y)
            if value < self.best_val:
                self.best_x = p.x
                self.best_y = p.y
                self.best_val = value
        # Делаем шаг роем
        for p in self.particles:
            p.step(self.best_x, self.best_y, self.objective)
