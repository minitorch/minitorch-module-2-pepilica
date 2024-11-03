"""Collection of the core mathematical operators used throughout the code base."""

import math

# ## Task 0.1
from typing import Any, Callable, List, Iterable, Tuple

#
# Implementation of a prelude of elementary functions.

# Mathematical functions:
# - mul
# - id
# - add
# - neg
# - lt
# - eq
# - max
# - is_close
# - sigmoid
# - relu
# - log
# - exp
# - log_back
# - inv
# - inv_back
# - relu_back
#
# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$


def mul(a: float, b: float) -> float:
    return 0.0 + a * b


def id(a: float) -> float:
    return 0.0 + a


def add(a: float, b: float) -> float:
    return 0.0 + a + b


def neg(a: float) -> float:
    return float(-a)


def lt(a: float, b: float) -> bool:
    return a < b


def eq(a: float, b: float) -> bool:
    return a == b


def max(a: float, b: float) -> float:
    if lt(a, b):
        return 0.0 + b
    return 0.0 + a


def is_close(a: float, b: float) -> bool:
    return abs(a - b) < 1e-2


def sigmoid(x: float) -> float:
    return (
        (1.0 / (1.0 + math.exp(-x))) if x >= 0 else (math.exp(x) / (1.0 + math.exp(x)))
    )


def relu(x: float) -> float:
    return 0.0 if x < 0 else 0.0 + x


def log(x: float) -> float:
    return math.log(x)


def exp(x: float) -> float:
    return math.exp(x)


def inv(x: float) -> float:
    return 1.0 / x


def log_back(x: float, c: float = 1) -> float:
    return c / x


def inv_back(x: float, c: float = 1) -> float:
    return -c / x**2


def relu_back(x: float, c: float = 1) -> float:
    if x == 0:
        return 0.5 * c
    return 0.0 + c if x > 0 else 0.0


# TODO: Implement for Task 0.1.


# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
# - zipWith
# - reduce
#
# Use these to implement
# - negList : negate a list
# - addLists : add two lists together
# - sum: sum lists
# - prod: take the product of lists


# TODO: Implement for Task 0.3.


def map(iter: Iterable[Any], func: Callable[[Any], float]) -> Iterable[float]:
    for i in iter:
        yield func(i)


def zipWith(
    iter1: Iterable[float], iter2: Iterable[float]
) -> Iterable[Tuple[float, float]]:
    iter2_iterator = iter(iter2)
    i2: float = 0.0
    is_second_exhausted = False
    for i1 in iter1:
        try:
            i2 = next(iter2_iterator)
        except StopIteration:
            is_second_exhausted = True
        if is_second_exhausted:
            break
        yield (i1, i2)


def reduce(
    iter: Iterable[float], func: Callable[..., float], init_value: float = 0.0
) -> float:
    cur_value = init_value
    for i in iter:
        cur_value = func(cur_value, i)
    return cur_value


def negList(arr: List[float]) -> List[float]:
    return list(map(arr, lambda x: -x))


def addLists(arr1: List[float], arr2: List[float]) -> List[float]:
    a = zipWith(arr1, arr2)
    b = map(a, lambda x: x[0] + x[1])
    return list(b)


def sum(arr: List[float]) -> float:
    return reduce(arr, add, 0)


def prod(arr: List[float]) -> float:
    return reduce(arr, mul, 1)
