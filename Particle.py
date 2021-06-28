#coding=utf-8
import numpy as np


class Particle:
    
    def generate_particles(number, xmin, xmax, ymin, ymax):
        particles = []
        # Генерируем частицы в случайных точках
        for i in range(number):
            p = Particle(xmin, xmax, ymin, ymax)
            particles.append(p)
        return particles
    def __init__(self, xmin, xmax, ymin, ymax):
        self.x = xmin + np.random.sample() * (xmax - xmin)
        self.y = ymin + np.random.sample() * (ymax - ymin)
        self.r_m = np.random.sample()
        self.r_g = np.random.sample()
        
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
        
    # Вычисление скорости        
    def calc_vel(self, x_swarm, y_swarm):
        vel_x = self.vel_x * self.w
        vel_x += self.f_m * self.r_m * (self.x_best - self.x)
        vel_x += self.f_g * self.r_g * (x_swarm - self.x)

        vel_y = self.vel_y * self.w
        vel_y += self.f_m * self.r_m * (self.y_best - self.y)
        vel_y += self.f_g * self.r_g * (y_swarm - self.y)

        self.vel_x = vel_x
        self.vel_y = vel_y

    def step(self, x_swarm, y_swarm, func):
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
               
