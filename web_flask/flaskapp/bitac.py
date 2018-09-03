#!/home/cadilla1/virtualenv/acaciastrain.cadillacabe.com_web__flask/3.6/bin/python
import requests


def dates_to_dict():
    r = requests.get('https://rest.bandsintown.com/artists/TheAcaciaStrain/events?app_id=81ea8566b2d409d49e6b17a253168c70')
    
    jso = r.json()

    shows = {}

    for i in jso:
        show_vals = []
        sd = {}
        sd['date'] = i['datetime'][:10]
        sd['venue'] = i['venue']['name']
        sd['city'] = i['venue']['city']
        show_vals.append(sd)
        shows[i['id']] = show_vals

    return shows

if __name__ == '__main__':
    dates_to_dict()



