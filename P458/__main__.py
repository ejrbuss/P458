from P458.data import (
    attributes,
    read_arff,
)
from P458.id3 import (
    id3,
)
from P458.tree import (
    str_tree,
    decide,
)

data          = read_arff('./data/contact-lenses.arff')
decision_tree = id3(data, 'contact-lenses')
row           = ['sunny', 'hot', 'high', False, False]
result        = decide(decision_tree, row, attributes(data))
print(' --- ')
print(str_tree(decision_tree))
print(f'For row: {row} id3 predicts: {result}')

