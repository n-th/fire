import reverse_geocoder as rg 
import pprint 

def reverseGeocode(coordinates): 
    result = rg.search(coordinates) 
    
    return result 
