import unittest
from perceptron import Perceptron

__author__ = 'estensen'


class TestActivate(unittest.TestCase):

    def test_activate(self):
        p = Perceptron(2)
        p.theta = 1.5
        p.w = [1, 1]
        self.assertEqual(p.activate([0, 0]), 0)
        self.assertEqual(p.activate([0, 1]), 0)
        self.assertEqual(p.activate([1, 0]), 0)
        self.assertEqual(p.activate([1, 1]), 1)
        self.assertEqual(p.activate([2, 0]), 1)
        self.assertEqual(p.activate([0, 2]), 1)

    def test_train(self):
        p = Perceptron(2)
        for i in range(100):
            p.train([1, 0], 0, 0.05)
            p.train([0, 1], 1, 0.05)
        self.assertAlmostEqual(p.activate([1, 0]), 0)
        self.assertAlmostEqual(p.activate([0, 1]), 1)

if __name__ == '__main__':
    unittest.main()
