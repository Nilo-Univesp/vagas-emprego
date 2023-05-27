"""
Routes and views for the flask application.
"""

import sqlite3
import os
from datetime import datetime
from flask import render_template, request, jsonify
from werkzeug.utils import secure_filename
from LatidosMiadosPerdidos import app
from LatidosMiadosPerdidos.pet_database import PetDatabase

# Set the path to the database file in the temporary directory
db_path = 'pets.db' #os.path.join(app.config['UPLOAD_FOLDER'], 'pets.db')

@app.route('/')
@app.route('/home')
def home():

    pet_db = PetDatabase(db_path)
    pet_db.connect()
    pet_db.create_table()
    pet_db.disconnect()

    # connect to the database
    conn = sqlite3.connect(db_path)

    # create a cursor
    c = conn.cursor()

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
    #pet_db = PetDatabase('pets.db')
    #pet_db.connect()
    #pet_db.delete_pet(5)
    #pet_db.disconnect()
    """Renders the formpet page."""
    return render_template(
        'formpet.html',
        title='Cadastre um Pet',
        year=datetime.now().year
    )

@app.route('/register-pet', methods=['POST'])
def register_pet():
    pet_data = {
        'name': request.form['pet-name'],
        'breed': request.form['pet-breed'],
        'description': request.form['pet-description'],
        'contact': request.form['contact']
    }

    if 'pet-image' in request.files:
        image_file = request.files['pet-image']
        if image_file.filename != '':
            filename = secure_filename(image_file.filename)
            image_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            pet_data['photo'] = filename
        else:
            pet_data['photo'] = 'blank.png'
    else:
        pet_data['photo'] = 'blank.png'

    pet_db = PetDatabase(db_path)
    pet_db.connect()
    pet_db.add_pet(pet_data)
    pet_db.disconnect()

    # Return a JSON response indicating success
    return jsonify({'success': True})
