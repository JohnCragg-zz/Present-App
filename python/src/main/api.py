import logging
import sqlite3
from flask import jsonify, abort
from python.src.main.db import DB
from python.src.main.parser import create_person, create_item
from python.src.main.Person import Person
from python.src.main.Item import Item
from flask_restplus import Resource, Api
from flask import Flask, request

#
logging.basicConfig(filename='present_app.log', level=logging.DEBUG)
conn = sqlite3.connect("person_and_item.db")
cursor = conn.cursor()
db = DB(cursor, conn)
db.create_person_table()
db.create_item_table()
conn.close()
app = Flask(__name__)
api = Api(app)


@api.route('/api/v1/person/<string:email>/<string:first_name>/<string:last_name>')
class SignUp(Resource):
    def put(self, email, first_name, last_name):
        conn = sqlite3.connect("person_and_item.db")
        cursor = conn.cursor()
        db = DB(cursor, conn)
        person = Person(email, first_name, last_name)
        db.insert_person(person)
        logging.info("Put person with email '%s'" % email)
        conn.close()
        return 200


@api.route('/api/v1/person/<string:email>')
class People(Resource):
    def delete(self, email):
        conn = sqlite3.connect("person_and_item.db")
        cursor = conn.cursor()
        db = DB(cursor, conn)
        person = db.get_person(email)
        if len(person) == 0:
            logging.error("Couldn't find person with email '%s'" % email)
            abort(404)
        else:
            db.delete_person(email)
            logging.info("User with email id %s has been deleted" % email)
            return 410
        conn.close()

    def get(self, email):
        conn = sqlite3.connect("person_and_item.db")
        cursor = conn.cursor()
        db = DB(cursor, conn)
        person = db.get_person(email)
        conn.close()
        if len(person) == 0:
            logging.error("Couldn't find person with email '%s'" % email)
            abort(404)
        else:
            logging.info("Fetched person with email '%s'" % email)
            return jsonify({'person': create_person(person).serialize()})


@api.route('/api/v1/items/<string:person_email>/<string:name>/<string:price>/<int:priority>/<string:hyperlink>')
class Items(Resource):
     def put(self, person_email, name, price, priority, hyperlink):
        conn = sqlite3.connect("person_and_item.db")
        cursor = conn.cursor()
        db = DB(cursor, conn)
        item = Item(person_email, name, price, priority, hyperlink)
        db.insert_item(item)
        logging.info("Put item '%s'" % name)
        conn.close()
        return 200

@api.route('/api/v1/items/<string:person_email>/<string:name>')
class Itemz(Resource):
     def delete(self, person_email, name):
         conn = sqlite3.connect("person_and_item.db")
         cursor = conn.cursor()
         db = DB(cursor, conn)
         items = db.get_specific_item(person_email, name)
         if len(items) == 0:
             logging.info("Couldn't find item called '%s' listed by user with email id '%s'"
                          % (name, person_email))
             abort(404)
         else:
             db.delete_item(person_email, name)
             logging.info("Item called '%s' from user with email id '%s' has been deleted"
                          % (name, person_email))
             return 410
         conn.close()


if __name__ == '__main__':
    app.run(debug=True)
