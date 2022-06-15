"""A simple flask web app"""
import os
from flask import Flask, render_template
import flask_login
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf.csrf import CSRFProtect
from app.simple_pages import simple_pages

def page_not_found(e):
    return render_template("404.html"), 404

def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    bootstrap = Bootstrap5(app)
    app.register_blueprint(simple_pages)

    return app