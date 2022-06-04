import googlemaps

def getloc(addr):
    gmaps = googlemaps.Client(key='구글키를 입력해주세요')
    geocode_result = gmaps.geocode(addr)
    n_lat = geocode_result[0]['geometry']['location']['lat']
    n_lng = geocode_result[0]['geometry']['location']['lng']
    return n_lat, n_lng
