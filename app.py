from flask import Flask,request,jsonify,render_template,redirect
from flask_cors import CORS
from database import db
from encriptador import bcrypt
from flask_migrate import Migrate
from config import BaseConfig
from sqlalchemy import exc
from models import Usuario,Venta,Proveedor,Producto

app = Flask(__name__)
app.config.from_object(BaseConfig)
CORS(app)
bcrypt.init_app(app)
db.init_app(app)
migrate = Migrate()
migrate.init_app(app,db)

@app.route('/')
@app.route('/inicio')
@app.route('/inicio.html')
def inicio():
    return render_template('inicio.html')

@app.route("/login")
def login():
    return render_template("login.html")



@app.route('/auth/registro',methods=['POST'])
def registro():
    user= request.get_json()
    userExist=Usuario.query.filter_by(correo=user['correo']).first()
    if not userExist:
        usuario=Usuario(nombreUsuario=user["nombreUsuario"],correo=user["correo"],contraseña=user["contraseña"],edad=["edad"])
        try:
            db.session.add(usuario)
            db.session.commit()
            mensaje="Usuario creado"
        except exc.SQLAlchemyError as e:
            mensaje="Error"
    else:
        mensaje="El usuario ya existe"
    return jsonify({"mensaje":mensaje})