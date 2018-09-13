from P458.data import (
    chunk,
    flatten,
    relation,
    attributes,
    rows,
    cols,
    classes,
    value,
    remove_attribute,
    filter_rows,
    hist,
    read_arff,
)

weather_data = read_arff('./data/weather_data.arff')

def test_chunk():
    assert list(chunk([1, 2, 3, 4], 2)) == [[1, 2], [3, 4]]
    assert list(chunk([1, 2, 3, 4], 3)) == [[1, 2, 3], [4]]

def test_flatten():
    assert flatten([[1], [2], [3], [4]]) == [1, 2, 3, 4]
    assert flatten([[1, 2], [3, 4]]) == [1, 2, 3, 4]

def test_relation():
    assert relation(weather_data) == 'weather.symbolic'

def test_attributes():
    assert attributes(weather_data) == ['outlook', 'temperature', 'humidity', 'windy', 'play']

def test_rows():
    assert rows(weather_data)[0] == ['sunny', 'hot',  'high', False, False]
    assert rows(weather_data)[7] == ['sunny', 'mild', 'high', False, False]

def test_cols():
    assert cols(weather_data)[0][:3] == ('sunny', 'sunny', 'overcast')
    assert cols(weather_data)[3][:3] == (False, True, False)

def test_classes():
    assert classes(weather_data, 'outlook') == set(('sunny', 'overcast', 'rainy'))
    assert classes(weather_data, 'temperature') == set(('hot', 'mild', 'cool'))
    assert classes(weather_data, 'humidity') == set(('high', 'normal'))
    assert classes(weather_data, 'windy') == set((True, False))
    assert classes(weather_data, 'play') == set((True, False))

def test_value():
    assert value(weather_data, rows(weather_data)[0], 'outlook') == 'sunny'
    assert value(weather_data, rows(weather_data)[7], 'humidity') == 'high'

def test_remove_attribute():
    data = remove_attribute(weather_data, 'outlook')
    assert relation(data) == 'weather.symbolic'
    assert attributes(data) == ['temperature', 'humidity', 'windy', 'play']
    assert rows(data)[0] == ['hot',  'high', False, False]
    assert rows(data)[7] == ['mild', 'high', False, False]

def test_filter_rows():
    data = filter_rows(weather_data, lambda r: value(weather_data, r, 'play'))
    assert relation(data) == 'weather.symbolic'
    assert attributes(data) == ['outlook', 'temperature', 'humidity', 'windy', 'play']
    assert rows(data)[0] == ['overcast', 'hot',  'high', False, True]

def test_hist():
    assert hist(weather_data, 'play') == { True: 9, False: 5 }