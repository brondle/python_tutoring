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
  for word in words:
      if len(word) > 0:
          new_word_phrase = word + " is the time is the " + word + " is the motion " + word + " is the way we are feeling "\
          + '\n'
          output.append(new_word_phrase)
      else:
          output.append(word)
    # rhymes = pronouncing.rhymes(word)
    # if random.randrange(4) == 0 and len(rhymes) > 0:
    #   output.append(random.choice(rhymes))
    # else:
    #   output.append(word)
  return render_template("string_results.html",
    output=' '.join(output))

if __name__ == '__main__':
  app.run()