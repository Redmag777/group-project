from flask import render_template, redirect,session,request,flash
from flask_app import app

from flask_app.models.user import User
from flask_app.models.book import Book
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)
