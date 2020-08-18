from flask import Flask, request, jsonify
import pronouncing
import random

app = Flask(__name__)

@app.route('/rhyme', methods=["GET"])
def transformed():
  text = request.args['text']
  output = list()
  words = text.split()
  for word in words:
    rhymes = pronouncing.rhymes(word)
    print('rhymes: ', rhymes)
    if len(rhymes) > 0:
      output.append(random.choice(rhymes))
    else:
      output.append(word)
    print('output: ', output)
  return jsonify({'response': output})

if __name__ == '__main__':
  app.run()
