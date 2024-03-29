from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

simple_pages = Blueprint('simple_pages', __name__,
                        template_folder='templates')
@simple_pages.route('/')
def index():
    try:
        return render_template('index.html')
    except TemplateNotFound:
        abort(404)

@simple_pages.route('/about')
def about():
    try:
        return render_template('about.html')
    except TemplateNotFound:
        abort(404)

@simple_pages.route('/projects')
def projects():
    try:
        return render_template('projects.html')
    except TemplateNotFound:
        abort(404)

@simple_pages.route('/contact')
def contact():
    try:
        return render_template('contact.html')
    except TemplateNotFound:
        abort(404)

@simple_pages.route('/cool_stuff')
def coolStuff():
    try:
        return render_template('testing_cool_things.html')
    except TemplateNotFound:
        abort(404)