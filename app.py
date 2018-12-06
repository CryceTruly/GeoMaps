import requests


def get_formatted_address(add):
    '''

    :param add:
    :return:
    '''

    try:
        r = requests.get(
             "https://maps.googleapis.com/maps/api/geocode/json?address="+add+"&key=AbIzaSyDQQ3v45Vf1LVh2JZFwh4yHaM4ERoPf1M0")
        data = r.json()
        results= data['results']
        address=results[0]
        return  address['formatted_address']
    except Exception as identifier:
        return None



print(get_formatted_address('Jinja'));