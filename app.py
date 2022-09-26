from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:P\@ssword2022@localhost/postgres'
db = SQLAlchemy(app)



if __name__ == '__main__':
  app.run(debug=True)

class Pet(db.Model):
    __tablename__ = 'pets'
    id = db.Column(db.Integer, primary_key = True)
    pet_name = db. Column(db.String(100), nullable = False)
    pet_type = db.Column(db.String(100), nullable = False)
    pet_age = db.Column(db.Integer(), nullable = False)
    pet_description = db.Column(db.String(100), nullable = False)


    def __repr__(self):
        return "<Pet %r>" % self.pet_name

@app.route('/')
    def index():
        return jsonify({"message":"Welcome to my site"})