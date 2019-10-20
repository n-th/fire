import csv

from utils import reverseGeocode

def analyze(data):
    data = filter_brasil_data(data)

    return data

def filter_brasil_data(coordinates):
    data = []
    for item in coordinates:
        result = reverseGeocode(item)
        if result[0]['cc'] == 'BR':
            data.append([result[0]['lat'], result[0]['lon'], result[0]['name'], result[0]['admin1']])
    
    return data