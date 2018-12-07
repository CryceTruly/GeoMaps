import requests


def get_formatted_address(add):
    '''

    :param add:
    :return:
    '''

    try:
        r = requests.get(
             "https://maps.googleapis.com/maps/api/geocode/json?address="+add+"&key=AIzaSyDQQ3v45Vf1LVh2JZFwh4yHaM4ERoPf1M0")
        data = r.json()
        results= data['results']
        address=results[0]
        return  address['formatted_address']
    except Exception as identifier:
        return None

def get_latlng(add):
    '''

    :param add:
    :return:
    '''

    try:
        r = requests.get(
             "https://maps.googleapis.com/maps/api/geocode/json?address="+add+"&key=yourkey")
        data = r.json()
        results= data['results']
        address=results[0]
        # Geometry
        geometry= address['geometry']
        return geometry['location']
    except Exception as identifier:
        return {'lat': 37.06250000000001, 'lng': -95.677068}

def get_dest(add):
    '''

    :param add:
    :return:
    '''

    try:
        r = requests.get(
             "https://maps.googleapis.com/maps/api/geocode/json?address="+add+"&key=yourkey")
        data = r.json()
        results= data['results']
        address=results[0]
        # Geometry
        geometry= address['geometry']
        return geometry['location']
    except Exception as identifier:
        return {'lat': 0.3475964, 'lng': 32.5825197}






print(get_latlng('Kampala'));