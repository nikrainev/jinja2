import requests
from jinja2 import Environment,  select_autoescape, FileSystemLoader

from flask import Flask

app = Flask(__name__)

env = Environment(
    loader=FileSystemLoader("templates/"),
    autoescape=select_autoescape()
)

template = env.get_template("template.txt")

r = requests.get('https://api.adviceslip.com/advice')
UserNikita = {'name': 'Nikita Krainev', 'usercode':'00001', 'age': 22,
         'skills':['TypeScript', 'WebRTC', 'Node.js', "React"],
         'position': 'Developer',
         'advice': r.json()['slip']['advice']}

UserElonMusk = {'name': 'Elon Musk', 'usercode':'00002', 'age': 52,
         'skills':["Math", "Physics"],
         'position': 'Entrepreneur',
         'advice': r.json()['slip']['advice']}

@app.route("/nikita")
def nikita_page():
    return template.render(UserNikita)

@app.route("/elon")
def elon_page():
    return template.render(UserElonMusk)
