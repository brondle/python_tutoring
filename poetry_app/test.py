import os
import sys
from flask import Flask, render_template

# import my_helper
# h_directory = '/Users/ademirji/PycharmProjects/NaturalLangage/Tuesdays/python_tutoring/poetry_app/helpers/'
h_directory = './helpers/basic'
sys.path.append('h_directory')

# from application.app.folder.file import func_name
# sys.path.insert(1, '/Users/ademirji/PycharmProjects/NaturalLangage/Tuesdays/python_tutoring/poetry_app/helpers/basic')
# sys.path.insert(1, '/helpers')
# sys.path.append('../')
# from my_helper import my_function
from my_helper import my_function
# a = os.getcwd()
# print(a)
# from basic import gen_random
# import gen_random
print(my_function())
# print(gen_random())



