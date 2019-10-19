import csv

def analyze(name):
    data = []
    with open(name, "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for line in csv_reader:
            if line_count != 0:
                lat = line[0]
                lon = line[1]
                data.append((lat, lon))
            line_count+=1
    return data

