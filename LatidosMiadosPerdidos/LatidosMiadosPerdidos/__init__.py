"""
The flask application package.
"""

from flask import Flask
app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB
app.config['UPLOAD_FOLDER'] = '/tmp'

import LatidosMiadosPerdidos.views
