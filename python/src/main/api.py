from flask import Flask, jsonify, abort
from python.src.main.db import DB
# from python.src.main.parser import Parser

app = Flask(__name__)


class Api(object):
    def __init__(self, db):
        self.db = db

    @app.route('/present/api/v1/person/<str:email>', methods=['GET'])
    def get_person(self, email):
        person_from_db = self.db.create_person(email)
        if len(person_from_db) > 1:
            return KeyError("multiple primary keys for key '%s'" % email)
        elif len(person_from_db) == 0:
            abort(404)
        else:
            return jsonify({'person': Parser(person_from_db[0]).create_person()})

    #     @app.route('/present/api/v1/person/<str:email>', methods=['GET'])
    # def get_person(self, email):
    #     person_from_db = self.db.create_person(email)
    #     return jsonify({'task': task[0]})
    #     # return db.read_person_table(email)  #
#     def create_item_from_table(self, email):
#         items_from_db = self.get_items(email)
#         items = []
#         for row in items_from_db:
#             item = Parser(row).create_item()
#             items.append(item)
#         return items
