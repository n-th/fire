import csv
import requests

def download(url):  
    with requests.Session() as s:
        download = s.get(url)

        decoded_content = download.content.decode('utf-8')

        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        my_list = list(cr)
        line_count = 0
        data = []
        for line in my_list:
            if line_count != 0 and line_count <10: #remover condicao de parada
                lat = float(line[0])
                lon = float(line[1])
                if lon > -73.99 and lon <-33.76 and lat>-35.73 and lat<5.24:
                    data.append((lat, lon))
            line_count+=1
    return data