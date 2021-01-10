import json

# Opening JSON file
f = open('cole_transcript.json', 'r')

# returns JSON object as
# a dictionary
data = json.load(f)

# Iterating through the json
# list

troops = 0
# for i in data['transcripts'][:10]:
#     print(i)

for i in data['transcripts'][:10]:
    for j in i['words']:
        if 'troops' in j['text']:
            print(j['start'])
            troops += 1
            print(troops)




# Closing file
f.close()