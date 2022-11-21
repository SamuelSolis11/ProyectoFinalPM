from config import BaseConfig
from app import db

class Usuario(db.Model):
    idUsuario = db.Column(db.Integer,primary_key=True,autoincrement=True)
    nombreUsuario = db.Column(db.String(250))
    correo = db.Column(db.String(250),unique=True,nullable=False)
    contraseña = db.Column(db.String(250),nullable=False)
    edad = db.Column(db.Integer)

    def __str__(self) -> str:
        return ( f'idUsuario:{self.idUsuario},'
                f'nombreUsuario:{self.nombreUsuario},'
                f'correo:{self.correo},'
                f'contraseña:{self.contraseña},'
                f'edad:{self.edad}'

        )

class Venta(db.Model):
    idVenta = db.Column(db.Integer,primary_key=True,autoincrement=True)
    total = db.Column(db.Integer)

    def __str__(self) -> str:
        return ( f'idVenta:{self.idVenta},'
                f'total:{self.total}'

        )

class Proveedor(db.Model):
    idProveedor = db.Column(db.Integer,primary_key=True,autoincrement=True)
    nombreProveedor = db.Column(db.String(250))
    direccion = db.Column(db.String(250))

    def __str__(self) -> str:
        return ( f'idProveedor:{self.idProveedor},'
                f'nombreProveedor:{self.nombreProveedor},'
                f'direccion:{self.direccion}'
        )

class Producto(db.Model):
    idProducto = db.Column(db.Integer,primary_key=True,autoincrement=True)
    nombreProducto = db.Column(db.String(250))

    def __str__(self) -> str:
        return ( f'idProducto:{self.idProducto},'
                f'nombreProducto:{self.nombreProducto}'
        )



    
