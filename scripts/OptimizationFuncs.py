#coding=utf-8
import numpy as np

class Function:
    def call(self, x,y):
        pass
    def __call__(self, x,y):
        z = self.call(x,y)
        return z
    def reset_counter(self):
        self.num_of_calls = 0

class Rastrigin(Function):

    def __init__(self):    
        [self.xmin,self.xmax,self.ymin,self.ymax] = [-5.12,5.12,-5.12,5.12]
        self.limits = [self.xmin,self.xmax,self.ymin,self.ymax]

        self.x_min = 0
        self.y_min = 0

        self.num_of_calls = 0
    
    def call(self, x, y):
        z = 20 + x**2 + y**2 - 10*(np.cos(2 * np.pi * x) + np.cos(2 * np.pi * y))
        self.num_of_calls += 1      
        return z

class Ackley(Function):

    def __init__(self):    
        [self.xmin,self.xmax,self.ymin,self.ymax] = [-5,5,-5,5]
        self.limits = [self.xmin,self.xmax,self.ymin,self.ymax]

        self.x_min = 0
        self.y_min = 0

        self.num_of_calls = 0
    
    def call(self, x, y):
        z = -20 * np.exp(-0.2 * np.sqrt(0.5*(x**2 + y**2)))
        z += -np.exp(0.5 * (np.cos(2*np.pi*x) + np.cos(2*np.pi*y)))
        z += np.e + 20
        self.num_of_calls += 1      
        return z

class Matyas(Function):

    def __init__(self):    
        [self.xmin,self.xmax,self.ymin,self.ymax] = [-10,10,-10,10]
        self.limits = [self.xmin,self.xmax,self.ymin,self.ymax]

        self.x_min = 0
        self.y_min = 0

        self.num_of_calls = 0
    
    def call(self, x, y):
        z = 0.26 * (x**2 + y**2) - 0.48 * x* y
        self.num_of_calls += 1      
        return z

class Rosenbrock(Function):

    def __init__(self):    
        [self.xmin,self.xmax,self.ymin,self.ymax] = [-10,10,-10,10]
        self.limits = [self.xmin,self.xmax,self.ymin,self.ymax]


        self.x_min = 1
        self.y_min = 1

        self.num_of_calls = 0
    
    def call(self, x, y):
        z = (1 - x)**2 + 100 * (y - x**2)**2
        self.num_of_calls += 1      
        return z

class Sphere(Function):

    def __init__(self):    
        [self.xmin,self.xmax,self.ymin,self.ymax] = [-10,10,-10,10]
        self.limits = [self.xmin,self.xmax,self.ymin,self.ymax]

        self.x_min = 0
        self.y_min = 0

        self.num_of_calls = 0
    
    def call(self, x, y):
        z = x**2 + y**2
        self.num_of_calls += 1      
        return z

