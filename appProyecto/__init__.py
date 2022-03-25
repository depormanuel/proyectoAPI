from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
#Añadiendo esto, no es necesaria la barra del final en la URL
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/EventosDeportivos'
app.config['JSON_AS_ASCII'] = False
app.config["MYSQL_HOST"]="127.0.0.1"


db = SQLAlchemy(app)

import appProyecto.controllers
