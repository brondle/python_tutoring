from flask import Flask, request, render_template
import pronouncing
import random

app = Flask(__name__)

@app.route('/')
def home():
  return render_template("string_home.html")

@app.route('/stringing', methods=["POST"])
def transformed():
    text = request.form['text']
    output = list()
    words = text.split()
    # if len(words) == 3:
    #     l1 = words[0] + ' is the time ' + '\n'
    #     l2 = words[1] + ' is the place ' + '\n'
    #     l3 = words[2] + ' is the motion ' + '\n'
    #     l4 = l1, l2, l3
    #     output.append(l4)
    # else:
    #     l4 = 'i said three words, ya dummy.'
    #     output.append(l4)

    return render_template("string_results.html",
                           output=' '.join(output))

    l1 = words[0] + ' is the time ' + '\n' + words[1] + ' is the place ' + '\n' + words[2] + ' is the motion'
    output.append(l1)

  # for i in range(len(words)-2):




          # new_word_phrase = word + " is the time is the " + word + " is the motion " + word + " is the way we are feeling " + '\n'


    # rhymes = pronouncing.rhymes(word)
    # if random.randrange(4) == 0 and len(rhymes) > 0:
    #   output.append(random.choice(rhymes))
    # else:
    #   output.append(word)


if __name__ == '__main__':
  app.run()