from analyzer import analyze
from notifier import notify
from downloader import download

if __name__=="__main__": 
    CSV_URL = "https://firms.modaps.eosdis.nasa.gov/data/active_fire/viirs/csv/VNP14IMGTDL_NRT_South_America_24h.csv"


    data = download(CSV_URL)
    filtered_data = analyze(data)
    #notify(data, 'spaceapps.saci@gmail.com')