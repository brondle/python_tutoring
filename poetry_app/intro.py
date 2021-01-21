from flask import Flask, render_template
import random

# to view this program in a browser, run it then go to a browser and enter: localhost:5000/hello
#refresh your browser to see the different random greeting choices
#customize the html/css in the template folder

app = Flask(__name__)

greets = ["Hello", "Hi", "Salutations", "Greetings", "Hey", "Sup"]
places = ["region", "continent", "world", "solar system",
  "galaxy"]

@app.route('/hello')
def hello():
    # return str(gen_rando())
    # return str(" ".join(b))
   greeting = random.choice(greets) + ", " + random.choice(places)
   return render_template("greetings2.html",
     greet=random.choice(greets), place=random.choice(places))

if __name__ == '__main__':
  app.run()