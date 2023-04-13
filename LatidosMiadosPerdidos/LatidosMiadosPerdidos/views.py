"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from LatidosMiadosPerdidos import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home',
        year=datetime.now().year
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contato',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='Saiba mais',
        year=datetime.now().year,
        message='Latidos e Miados perdidos - um projeto de alunos da UNIVESP.'
    )

@app.route('/formpet')
def formpet():
    """Renders the formpet page."""
    return render_template(
        'formpet.html',
        title='Cadastre um Pet',
        year=datetime.now().year
    )
