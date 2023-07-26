from sqlalchemy_serializer import SerializerMixin
from config import db


class Book(db.Model, SerializerMixin):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'<Book id={self.id} title={self.title}>'
