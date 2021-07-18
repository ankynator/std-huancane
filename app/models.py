from operator import length_hint
from app import db

class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)

    def __repr__(self):
        return f'User {self.name}'


class File(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    number_file = db.Column(db.String(length=5), nullable=False, unique=True)
    name_file = db.Column(db.String(length=30), nullable=False, unique=True)

    def __repr__(self):
        return f'File {self.name_file}'