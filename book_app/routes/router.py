
from flask import Blueprint
from .book import book_bp
from .user import user_bp

def register(app):
    app.register_blueprint(book_bp)
    app.register_blueprint(user_bp)