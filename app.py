from flask import Flask,request,jsonify
from flask_cors import CORS
from database import db
from encriptador import bcrypt
from flask_migrate import Migrate
from config import BaseConfig
from models import Usuario,Venta,Proveedor,Producto

app = Flask(__name__)
app.config.from_object(BaseConfig)
CORS(app)
bcrypt.init_app(app)
db.init_app(app)
migrate = Migrate()
migrate.init.app(app,db)
