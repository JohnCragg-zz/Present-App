import sqlite3
from sqlite3 import Error
from python.src.main.Person import Person

mark = Person(1, 'SparkyMark123@grinder.com', "Mark", "Holmes")
john = Person(2, "FredSaidIWasBoring@loser.com", "John", "Cragg")
people_mark_cares_about = [mark, john]


def create_person_table(c):
    c.execute(
        "CREATE TABLE IF NOT EXISTS Person(personal_id REAL, email TEXT, first_name TEXT, last_name TEXT)"
    )


def insert_person(c, conn, person):
    c.execute("INSERT INTO Person VALUES(%d, '%s', '%s', '%s')"
              % (person.personal_id, person.email, person.first_name, person.last_name))
    conn.commit()


def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        c = conn.cursor()
        create_person_table(c)

        for person in people_mark_cares_about:
            insert_person(c, conn, person)
            print("Inserted person, %s, into the database" % person.first_name)

        c.close()
        print("populated table")
        
    except Error as e:
        print(e)
    finally:
        conn.close()


if __name__ == '__main__':
    create_connection("person.db")
