from flask import Flask, request
import pronouncing
import random
import repeating

app = Flask(__name__)
count = 0

@app.route('/rhyme')
def define():
    word_str = request.args['word']
    if len(word_str) == 0:
        return "no word specified!\n"
    else:
        rhymes = pronouncing.rhymes(word_str.lower())
        if len(rhymes) > 0:
            r = repeating.Repeat(3, define)
            return random.choice(rhymes) + "\n"


        else:
            return "no rhymes found :(\n"


if __name__ == '__main__':
    app.run(debug=True)


#http://localhost:5000/rhyme?word=x, replacing x with a word of your choice.



# r = repeating.Repeat(3, define)
r.start()