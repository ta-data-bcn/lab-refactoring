def from_address_to_coords_question():
    import requests
    address = input('What address?')
    print(address)

    key1 = 'AIzaSyAhQ0sPyYIxdsxrVOOmDONOoaxoXqGUiT4'
    url = 'https://maps.googleapis.com/maps/api/geocode/json'
    params1 = {'address':address,
                'key':key1}
    # todo check if request is error free
    r   = requests.get(url, params=params1).json()
    lat = r['results'][0]['geometry']['location']['lat']
    lon = r['results'][0]['geometry']['location']['lng']  
    
    print('The lattitude and longitude of adress', address, ' is')
    print(lat,lon)
    return (lat,lon)

from_address_to_coords_question()