import requests
print(requests.get('http://localhost:5000/rhyme', params={'word': '"beat"'}).content)