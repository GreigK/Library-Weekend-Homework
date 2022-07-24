from flask import render_template, request, redirect
from app import app
from models.book_list import books, add_book, remove_book
from models.book import Book

@app.route('/books')
def index():
    return render_template('books/index.html', title='Home', books=books)

@app.route('/books/new')
def new():
    return render_template('books/new_books.html', title='New Book')

@app.route('/books/<index>')
def view_book(index):
    fav = books[int(index)]
    return render_template('/books/index.html', book=fav)

@app.route('/books', methods=['POST'])
def create():
    title = request.form['title']
    author = request.form['author']
    genre = request.form['genre']
    new_book = Book(title, author, genre)
    add_book(new_book)
    return redirect('/books')

@app.route('/books/delete/<index>', methods=['POST'])
def delete_book_by_index(index):
    remove_book(int(index))
    return redirect('/books')