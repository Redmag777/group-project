from unittest import result
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Book:
    db = 'Book_Club'
    def __init__(self, data):
        self.id = data['id']
        self.name = data['title']
        self.ingredients=data['description']
        self.order_id= data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM books LEFT JOIN users on books.user_id = users.id;"
        return connectToMySQL(cls.db).query_db(query)



    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM books WHERE id = %(book_id)s LEFT JOIN users on books.user_id = users.id;"
        return connectToMySQL(cls.db).query_db(query,data)



    @classmethod
    def save(cls, data):
        query = 'INSERT INTO books (title, description, user_id ) VALUES ( %(title)s, %(description)s, %(user_id)s );'
        return connectToMySQL(cls.db).query_db(query, data)
    


    @classmethod
    def update(cls, data):
        query = 'UPDATE books SET title = %(title)s, description = %(description)s  WHERE id=%(book_id)s;'
        return connectToMySQL(cls.db).query_db(query, data)



    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM books WHERE id = %(books_id)s;"
        return connectToMySQL(cls.db).query_db(query,data)


    @staticmethod
    def validate_book(book):
        is_valid = True
        if len(book['title'])<3:
            flash('Name of the book must be at least 3 characters', "book")
            is_valid=False
        if len(book['description'])<5:
            flash('Description must be at least 5 characters', "book")
            is_valid=False
        return is_valid
    