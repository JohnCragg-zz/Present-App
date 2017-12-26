from flask import Flask, jsonify, abort

from python.src.main.parser import create_person, create_item

app = Flask(__name__)


class Api(object):
    def __init__(self, db):
        self.db = db

    @app.route('/present/api/v1/person/<str:email>', methods=['GET'])
    def get_person(self, email):
        person_from_db = self.db.get_person(email)
        if len(person_from_db) > 1:
            return KeyError("multiple primary keys for key '%s'" % email)
        elif len(person_from_db) == 0:
            abort(404)
        else:
            return jsonify({'person': create_person(person_from_db[0])})

    @app.route('/present/api/v1/item/<str:email>', methods=['GET'])
    def get_person(self, email):
        items_from_db = self.db.get_items(email)
        items = []
        if len(items_from_db) == 0:
            abort(404)
        else:
            for i in items_from_db:
                items += create_item(i)
            return jsonify({'items': items})
