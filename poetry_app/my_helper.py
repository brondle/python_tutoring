import os
import sys
import random
from flask import Flask, render_template



# sys.path.insert(1, '/Users/ademirji/PycharmProjects/NaturalLangage/Tuesdays/python_tutoring/poetry_app/helpers/basic')
# sys.path.insert(1, '/helpers')
# a = os.getcwd()
# h_directory = '/Users/ademirji/PycharmProjects/NaturalLangage/Tuesdays/python_tutoring/poetry_app/helpers'
# print(a)

# from basic import gen_random
#
# import gen_random

def my_function():
    n = random.random()
    return n

# print(my_function())
app = Flask(__name__)

greets = ["Hello", "Hi", "Salutations", "Greetings", "Hey", "Sup"]
places = ["region", "continent", "world", "solar system",
  "galaxy"]

@app.route('/hello')
def hello():
  greeting = random.choice(greets) + ", " + random.choice(places)
  return render_template("greetings.html",
    greet=random.choice(greets), place=random.choice(places))


