import requests

APOD_KEY = ''
APOD_SITE = f'https://api.nasa.gov/planetary/apod?api_key={APOD_KEY}'
SOLAR_SYSTEM_API = 'https://api.le-systeme-solaire.net/rest/bodies/'

def wiki(wiki_query):
    wiki_page = requests.get(f'https://en.wikipedia.org/wiki/{wiki_query}')
    print(wiki_page)

def space(space_query):
    if space_query.lower() == "apod":
        apod_response = requests.get(APOD_SITE)
        apod_card = apod(apod_response)
        return apod_card
    else:
        req = requests.get(SOLAR_SYSTEM_API + space_query)
        if req.json()[isPlanet]:
            output = space_planet(req)
        else:
            output = space_satellite(req)

def apod(data):
    data = data.json()

    Card = f'''
Astronomy Picture Of Day(APOD By NASA)

{data['title']}
copyright: {data['copyright']}\tDate : {data['date']}

{data['explanation']}
    '''

    return Card

# def space_planet(response):
#     data = response.json()
#     values = []

#     variables = [
#         'name', 'moons', 'mass', 'vol', 'gravity', 'equaRadius', 'discoveredBy', 'discoveryDate', 'alternativeName', 'axialTilt'
#         ]

#     for var in variables:
#         values.append(data[var])

print(space('apod'))
