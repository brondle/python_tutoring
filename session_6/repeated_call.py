import requests
import repeating

#r = repeating.Repeat(8, requests.get(url='http://localhost:5000/rhyme', params={'word': '"cat"'}))
print(requests.get('http://localhost:5000/rhyme', params={'word': '"cat"'}).content)
#r.start()

