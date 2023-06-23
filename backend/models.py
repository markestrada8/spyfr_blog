from extensions import db
from datetime import datetime

'''
class Recipe
id: int pk not null auto_increment
title: str
content: str
created_at: datetime
'''

class Blog(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Recipe {self.title}'

    def add(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self, title, content):
        self.title = title
        self.content = content
        db.session.commit()


'''
class User
    id: int
    username: str
    email: str
    password: str
'''

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

    def add(self):
        db.session.add(self)
        db.session.commit()
