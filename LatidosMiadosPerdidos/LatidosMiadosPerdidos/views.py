"""
Routes and views for the flask application.
"""

import sqlite3
from datetime import datetime
from flask import render_template
from LatidosMiadosPerdidos import app
from LatidosMiadosPerdidos.pet_database import PetDatabase

@app.route('/')
@app.route('/home')
def home():

    pet_db = PetDatabase('pets.db')
    pet_db.connect()
    pet_db.create_table()
    pet_db.disconnect()


    # connect to the database
    conn = sqlite3.connect('pets.db')

    # create a cursor
    c = conn.cursor()

    ## TESTE PARA ADICIONAR MANUALMENTE UMA LINHA NA TABELA PETS
    ## insert a new row into the 'pets' table
    #c.execute("INSERT INTO pets (name, breed, description, photo, contact) VALUES (?, ?, ?, ?, ?)",
    #          ('Max', 'German Shepherd', 'Encontrado no parque do jardim das flores', 'max.jpg', '(14) 98172-3820'))

    ### commit the changes to the database
    #conn.commit()

    # select all data from the 'pets' table
    c.execute("SELECT * FROM pets")

    # get the column names
    columns = [description[0] for description in c.description]

    # fetch all the data and print it
    pets = [dict(zip(columns, row)) for row in c.fetchall()]

    ## close the connection
    conn.close()

    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home',
        year=datetime.now().year,
        pets = pets
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
