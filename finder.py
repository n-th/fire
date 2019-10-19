import reverse_geocoder as rg 
import pprint 

def reverseGeocode(coordinates): 
    result = rg.search(coordinates) 
      
    pprint.pprint(result)  

def find_dots_in_brazil(data):