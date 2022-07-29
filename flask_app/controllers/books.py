from flask import render_template, redirect, session, request, flash
from flask_app import app
from flask_app.models.book import Book
from flask_app.models.user import User

@app.route('/book/<int:id>')
def show_book(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data={
        'user_id': session['user_id'],
        'book_id': id
    }
    return render_template('one_book.html', user=User.get_by_id(data), one_book =Book.get_one(data))

@app.route('/delete/<int:id>')
def destroy_book(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "books_id": id
    }
    Book.destroy(data)
    return redirect('/')


@app.route('/create_book', methods = ['POST'])
def createbook():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Book.validate_book(request.form):
        return redirect(request.referrer)
    data = {
        "title": request.form["title"],
        "description": request.form["description"],
        "user_id": session["user_id"]
    }
    Book.save(data)
    return redirect('/')


@app.route('/update/book', methods=['POST'])
def update_book():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Book.validate_book(request.form):
        return redirect(request.referrer)
    data = {
        "title": request.form["title"],
        "description": request.form["description"],
        "book_id": request.form["id"]
    }
    Book.update(data)
    return redirect('/')