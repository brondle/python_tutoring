from flask import Flask, request, render_template
import pronouncing
import random

app = Flask(__name__)

@app.route('/')
def home():
  return render_template("rhyme_home.html")

@app.route('/rhyming', methods=["POST"])
def transformed():
  text = request.form['text']
  output = list()
  words = text.split()
  for word in words:
    rhymes = pronouncing.rhymes(word)
    if random.randrange(4) == 0 and len(rhymes) > 0:
      output.append(random.choice(rhymes))
    else:
      output.append(word)
  return render_template("rhyme_results.html",
    output=' '.join(output))

if __name__ == '__main__':
  app.run()