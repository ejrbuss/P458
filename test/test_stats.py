import math
from P458.stats import (
    within_epsilon, 
    slog2,
    avg,
    entropy,
    tuple_to_probability,
    info,
    gain,
)

def test_within_epsilon():
    assert within_epsilon(0, 0)
    assert within_epsilon(1.0001, 1.0000)
    assert within_epsilon(4.5, 5, 1)

def test_slog2():
    assert slog2(42) == math.log2(42)
    assert slog2(0) == 0

def test_avg():
    assert avg((4, 4, 4)) == 4
    assert avg((1, 2)) == 1.5

def test_entropy():
    assert entropy(1/4, 1/4, 1/4, 1/4) == 2
    assert entropy(1/2, 1/4, 1/8, 1/8) == 1.75
    assert entropy(1/4, 1/4) == 1
    assert entropy(1, 0) == 0
    assert within_epsilon(entropy(2/5, 3/5), 0.971)
    assert within_epsilon(entropy(2/3, 1/3), 0.918)
    assert within_epsilon(entropy(3/4, 1/4), 0.811)

def test_tuple_to_probability():
    assert list(tuple_to_probability((2, 3))) == [2/5, 3/5]
    assert list(tuple_to_probability((4, 0))) == [4/4, 0/4]
    assert list(tuple_to_probability((9, 5))) == [9/14, 5/14]
    assert list(tuple_to_probability((7, 9, 3))) == [7/19, 9/19, 3/19] 

def test_info():
    assert info((2, 0)) == 0
    assert info((1, 1)) == 1
    assert within_epsilon(info((3, 4), (6, 1)), 0.788)
    assert within_epsilon(info((2, 2), (4, 2), (3, 1)), 0.911) 
    assert within_epsilon(info((6, 2), (3, 3)), 0.892)

def test_gain():
    assert within_epsilon(gain([(9, 5)], [(2, 3), (4, 0), (3, 2)]), 0.247)
    assert within_epsilon(gain([(9, 5)], [(2, 2), (4, 2), (3, 1)]), 0.029)
    assert within_epsilon(gain([(9, 5)], [(3, 4), (6, 1)]), 0.152)
    assert within_epsilon(gain([(9, 5)], [(6, 2), (3, 3)]), 0.048)