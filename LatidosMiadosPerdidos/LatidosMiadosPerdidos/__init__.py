"""
The flask application package.
"""

import os
from flask import Flask
app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB
app.config['UPLOAD_FOLDER'] = '/tmp' if os.name == 'posix' else os.environ.get('TEMP')

import LatidosMiadosPerdidos.views
