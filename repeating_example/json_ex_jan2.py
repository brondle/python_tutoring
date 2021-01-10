import json

# Opening JSON file
f = open('cole_transcript.json', 'r')

# returns JSON object as
# a dictionary
data = json.load(f)

# Iterating through the json
# list
for i in data['transcripts'][:10]:
    print(i)

# Closing file
f.close()