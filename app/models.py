import datetime
from app import db
from app import bcrypt

class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)

    @property
    def password(self):
        return self.password
    
    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)

    def __repr__(self):
        return f'User {self.name}'


class File(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    file_number_format = db.Column(db.String(length=5), nullable=False)
    file_user_name = db.Column(db.String(length=100), nullable=False)
    file_user_dni = db.Column(db.String(length=8), nullable=False)
    file_user_phone = db.Column(db.String(length=12), nullable=False)
    file_user_email = db.Column(db.String(length=50), nullable=False)
    file_subject = db.Column(db.String(length=50), nullable=False)
    file_justification = db.Column(db.Text(length=255), nullable=False)
    file_date = db.Column(db.DateTime, default=datetime.datetime.now)

    @property
    def file_number(self):
        return self.file_number

    @file_number.setter
    def file_number(self, int_file_number):
        int_file_number += 1
        str_file_number = str(int_file_number)
        insert_file_number = '0' * (5-len(str_file_number)) + str_file_number
        self.file_number_format = insert_file_number

    def __repr__(self):
        return f'File {self.name_file}'