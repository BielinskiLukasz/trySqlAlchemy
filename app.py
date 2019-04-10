from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class Visit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    count = db.Column(db.Integer)

    def __init__(self):
        self.count = 0

# Zad5.5
# Rozwiązać zadanie ze ścieżką /counter z zajęć nr 1 (Wykład 1 zadanie 5) wykorzystując Heroku PostgreSQL, SQLAlchemy
# i synchronizację na bazie.
# PROTIP - do tego zadania warto zmontować osobną aplikację, w następnych będziemy operować na innej bazie.
# Dokumentacja dla zapytania SELECT FOR UPDATE:
# https://www.postgresql.org/docs/current/static/sql-select.html (sekcja: The Locking Clause)
# http://docs.sqlalchemy.org/en/latest/orm/query.html#sqlalchemy.orm.query.Query.with_for_update
@app.route("/")
def hello():
    v = Visit.query.first()
    if not v:
        v = Visit()
        v.count += 1
        db.session.add(v)
    v.count +=1
    db.session.commit()
    return jsonify(counter=v.count)


if __name__ == '__main__':
    app.run(debug=True)
