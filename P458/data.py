import re

re_comment   = re.compile(r'%.*')
re_relation  = re.compile(r'@relation\s*([\w\.-]+)', re.I)
re_attribute = re.compile(r'@attribute\s+([\w\.`-]+)', re.I)
re_data      = re.compile(r'@data\s+(.*)', re.S)
re_true      = re.compile(r'true|yes', re.I)
re_false     = re.compile(r'false|no', re.I)

# Data Format
# {
#   'relation': 'relation_name',
#   'attributes': ['attr1', 'attr2', ..., 'attrN'],
#   'data': [
#       r1c1, r1c2, ..., r1cN,
#       r2c1, r2c2, ..., r2cN,
#       ...,
#       rMc1, rMc2, ..., rMcN,
#   ],
# }

def chunk(iterable, n):
    for i in range(0, len(iterable), n):
        yield iterable[i:i + n]

def flatten(iterable):
    return [item for sub_iterable in iterable for item in sub_iterable]

def relation(data):
    return data['relation']

def attributes(data):
    return data['attributes']

def rows(data):
    return list(chunk(data['data'], len(attributes(data))))

def cols(data):
    return list(zip(*rows(data)))

def classes(data, attribute):
    return set(cols(data)[attributes(data).index(attribute)])

def value(data, row, attribute):
    return row[attributes(data).index(attribute)]

def remove_attribute(data, attribute):
    attrs    = attributes(data)
    attr_idx = attrs.index(attribute)
    return {
        'relation':   relation(data),
        'attributes': attrs[:attr_idx] + attrs[attr_idx + 1:],
        'data':       flatten(map(
            lambda row: row[:attr_idx] + row[attr_idx + 1:],
            rows(data),
        ))
    }

def filter_rows(data, fn):
    return new_data(data, data=flatten(filter(fn, rows(data))))

def hist(data, attribute):
    result = {}
    for class_value in classes(data, attribute):
        result[class_value] = 0
    for row in rows(data):
        result[value(data, row, attribute)] += 1
    return result

def read_arff(path):
    with open(path) as stream:
        raw = stream.read()
        raw = re.sub(re_comment, '', raw)
        return {
            'relation':   re.findall(re_relation, raw)[0],
            'attributes': re.findall(re_attribute, raw),
            'data':       list(map(
                parse_data, 
                re.split(r',|\n', re.findall(re_data, raw)[0].strip()),
            )),
        }

def parse_data(value):
    value = value.strip()
    if (re.fullmatch(re_true, value)):
        return True
    if (re.fullmatch(re_false, value)):
        return False
    return value

def new_data(original, relation=None, attributes=None, data=None):
    return {
        'relation':   original['relation'] if relation is None else relation,
        'attributes': original['attributes'] if relation is None else attributes,
        'data':       original['data'] if data is None else data,
    }
