"""STAR
Abhishek Anil Deshmukh <deshmukhabhishek369@gmail.com>
the simulations which is being monitored
"""
from numpy.random import uniform
from sympy.parsing.sympy_parser import eval_expr

import numpy

NUMPY_DICT = {a: getattr(numpy, a) for a in dir(numpy)}


def main(f: str, a: float, b: float, c: float, d: float, size: int):
    """Monte Carlo simulation"""
    xs = uniform(a, b, size)
    ys = uniform(c, d, size)

    area = (a - b) * (c - d)
    under = ys < eval_expr(f, {"xs": xs}, NUMPY_DICT)

    pi = sum(under) / size * area

    return pi


# just to check if the thing works
if __name__ == "__main__":
    from sys import argv

    f, a, b, c, d = argv[1:6]
    size = int(argv[6]) if len(argv) == 7 else 100
    a, b, c, d = map(int, (a, b, c, d))

    print(f"integrating {f} from {a} to {b} with {size} samples")
    result = main(f, a, b, c, d, size)
    print(f"approx= {result}")
