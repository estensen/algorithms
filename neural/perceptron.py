from random import uniform
from operator import add
from operator import mul


class Perceptron:
    def __init__(self, num_inputs):
        self.theta = uniform(-0.5, -0.5)
        self.theta = 0.2
        self.w = [uniform(-0.5, 0.5) for x in range(num_inputs)]
        self.w = [0.3, -0.1]

    def activate(self, x):
        s = sum(map(mul, x, self.w))
        if s - self.theta < -0.0000000001:
            return 0
        return 1

    def train(self, x, y_d, a):
        y = self.activate(x)
        e = y_d - y
        delta_w = [a * x[i] * e for i in range(len(self.w))]
        self.w = list(map(add, self.w, delta_w))
