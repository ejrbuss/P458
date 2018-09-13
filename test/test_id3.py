from P458.data import (
    read_arff,
)
from P458.id3 import (
    id3
)

weather_data = read_arff('./data/weather_data.arff')

def test_id3():
    print(id3(weather_data, 'play'))