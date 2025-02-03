import requests

parameters = {"MmnqT":"",
              "lang":"ru", }
locations = ['London', 'Cherepovets', 'svo']
url_template = 'https://wttr.in/{}'
for location in locations:
    url = url_template.format(location)
    response = requests.get(url, params=parameters)
    response.raise_for_status()
    print(response.text)