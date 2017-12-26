import logging
import sqlite3

from flask import Flask
from flask import jsonify, abort

from python.src.main.db import DB
from python.src.main.parser import create_person, create_item
from python.src.main.Person import Person

#
logging.basicConfig(filename='present_app.log', level=logging.DEBUG)
conn = sqlite3.connect("person_and_item.db")
cursor = conn.cursor()
db = DB(cursor, conn)
db.create_person_table()
db.create_item_table()


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'boo, World!'


@app.route('/present/api/v1/person/<string:email>')
def put_person(email):
    # db.insert_person(Person(email, "JOHN", "CRAGG"))
    logging.info("Put person with email '%s'" % email)
    return "cat %s" % email


# @app.route('/present/api/v1/person/<string:email>', methods=['GET'])
# def get_person(email):
#     person_from_db = db.get_person(email)
#     if len(person_from_db) > 1:
#         logging.error("Multiple people with email '%s'" % email)
#         return KeyError("multiple primary keys for key '%s'" % email)
#     elif len(person_from_db) == 0:
#         logging.error("Couldn't find person with email '%s'" % email)
#         abort(404)
#     else:
#         logging.info("Fetched person with email '%s'" % email)
#         return jsonify({'person': create_person(person_from_db[0])})

# @app.route('/present/api/v1/item/<string:email>', methods=['GET'])
# def get_person(email):
#     items_from_db = db.get_items(email)
#     items = []
#     if len(items_from_db) == 0:
#         abort(404)
#     else:
#         for i in items_from_db:
#             items += create_item(i)
#         return jsonify({'items': items})


if __name__ == '__main__':
    app.run(debug=True, port=9000, host='127.0.0.1')
    # conn.close()
