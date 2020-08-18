import requests
import repeating

def getCat():
    r = requests.get(url='http://localhost:5000/rhyme', params={'text': 'cat'})
    print('returned data: ', r.json())
    return r.json()

r = repeating.Repeat(8, getCat)

#print(requests.get('http://localhost:5000/rhyme', params={'word': '"cat"'}).content)
r.start()

