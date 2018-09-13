import sys

from P458.data import (
    attributes,
    rows,
    classes,
    value,
    remove_attribute,
    filter_rows,
    hist,
)
from P458.stats import (
    info,
)

def id3(data, class_attribute, accept_info=0):
    if len(hist(data, class_attribute)) == 1:
        return hist(data, class_attribute)
    best_attribute, info = get_best_attribute(data, class_attribute)
    if info < 1 - accept_info:
        branches = list(map(
            lambda c: { 
                'if': c, 'then': id3(
                    subclass_data(data, best_attribute, c),
                    class_attribute,
                    accept_info,
                ),
            }, 
            classes(data, best_attribute),
        ))
        return { 'attribute': best_attribute, 'children': branches }
    return hist(data, class_attribute)

def get_best_attribute(data, class_attr):
    attrs = list(filter(lambda a: a != class_attr, attributes(data)))
    print(f' ---\nDetermining best attribute from: {", ".join(attrs)}')
    lowest_attr = attrs[0]
    lowest_info = 1
    for attr in attrs:
        print_info_calc(data, class_attr, attr)
        info = attr_info(data, class_attr, attr)
        if info < lowest_info:
            lowest_attr = attr
            lowest_info = info
    print(f'Lowest info attribute is: {lowest_attr}')
    return (lowest_attr, lowest_info)

def attr_info(data, class_attr, attr):
    return info(*attr_tuple(data, class_attr, attr))

def attr_tuple(data, class_attr, attr):
    return list(map(
        lambda c: tuple(hist(filter_rows(data, lambda r: value(data, r, attr) == c), class_attr).values()),
        classes(data, attr),
    ))

def subclass_data(data, attribute, class_value):
    print(f'subclassing {class_value}')
    return remove_attribute(filter_rows(data,
        lambda row: value(data, row, attribute) == class_value
    ), attribute)

def print_info_calc(data, class_attr, attr):
    print(f'info({attr}) = info({attr_tuple(data, class_attr, attr)}) = {attr_info(data, class_attr, attr)}')
