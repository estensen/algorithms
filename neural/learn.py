from perceptron import Perceptron
from _operator import or_
from _operator import and_


def run(op):
    p = Perceptron(2)
    alpha = 0.1
    epoch = 1
    inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]

    for i in range(100):
        print("Epoch: %i" % epoch)
        for x_n in inputs:
            p.train(x_n, op(x_n[0], x_n[1]), alpha)

        print("Final weights: %.2f, %.2f" % (p.w[0], p.w[1]))
        epoch += 1

if __name__ == '__main__':
    print("OR")
    run(or_)
    print("\nAND")
    run(and_)
