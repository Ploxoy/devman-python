import requests

url_template = 'https://wttr.in/{}'
params = {
    'n':'',  # narrow version (only day and night)
    'T':'',  # switch terminal sequences off (no colors)
    'q':'',  # quiet version (no "Weather report" text)
    'm':'',  # metric (SI) (used by default everywhere except US)
    'M':'',  # show wind speed in m/s
    'lang': 'ru',
}

cities = ['Лондон', 'Шереметьево', 'Череповец']
for city in cities:
    url = url_template.format(city)
    response = requests.get(url, params=params, timeout=5)
    response.raise_for_status()
    print(response.text)
