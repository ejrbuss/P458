import sys
import math
import collections

def within_epsilon(n1, n2, epsilon=0.01):
    return abs(n1 - n2) < epsilon

def slog2(n):
    return math.log2(n) if n != 0 else 0

def avg(iterable):
    return sum(iterable) / len(list(iterable))

def entropy(*ps):
    return sum(map(lambda p: -p * slog2(p), ps))

def tuple_to_probability(t):
    denom = sum(t)
    return list(map(lambda numer: numer / denom, t))

def info(*ts):
    total = sum(map(lambda t: sum(t), ts))
    info  = sum(map(lambda t: tuple_info(t, total), ts))
    return info

def tuple_info(t, total):
    tuple_total = sum(t)
    probability = tuple_to_probability(t)
    return entropy(*probability) * tuple_total / total

def gain(before, after):
    return info(*before) - info(*after)