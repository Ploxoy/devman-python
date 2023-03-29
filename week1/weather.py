import requests
url_template = 'https://wttr.in/{}'
params = {'n': None,  # narrow version (only day and night)
          'T': None,  # switch terminal sequences off (no colors)
          'q': None,  # quiet version (no "Weather report" text)
          'm': None,  # metric (SI) (used by default everywhere except US)
          'M': None,  # show wind speed in m/s
          'lang': 'ru'}
# так как ключи с нулевым параметром не передаются в requests, преобразуем словарь  в строку:
params = '&'.join([k if v is None else f"{k}={v}" for k, v in params.items()])
cityes = ['Лондон', 'Шереметьево', 'Череповец']
for city in cityes:
    url = url_template.format(city)
    response = requests.get(url, params=params)
    response.raise_for_status()
    print(response.text)
