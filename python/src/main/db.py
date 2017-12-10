import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to a SQLite database """

    try:
        conn = sqlite3.connect(db_file)
        c = conn.cursor()

        def create_table():
            c.execute(
                "CREATE TABLE IF NOT EXISTS Person(personal_id REAL, email TEXT, first_name TEXT, last_name TEXT)"
            )

        def data_entry():
            c.execute("INSERT INTO Person VALUES(1, 'mark@aol.com', 'Mark', 'Holmes')")
            conn.commit()
            c.close()

        create_table()
        data_entry()
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        conn.close()


if __name__ == '__main__':
    create_connection("mark.db")
