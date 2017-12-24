from flask import Flask
from db import read_person_table

app = Flask(__name__)


@app.route('/present/api/v1/person/', methods=['GET'])
def get_person(person):
    return read_person_table(person)
