from analyzer import analyze
from notifier import notify

if __name__=="__main__": 
    data = analyze("MODIS_C6_South_America_24h.csv")

    emails = find() #teste

    notify(data, emails)