from models import Usuario
from functools import wraps
from flask import request,jsonify

def obtenerInfo(token):
    if token:
        resp = Usuario.decode_auth_token(token)
        usuario = Usuario.query.filter_by(id=resp).first()
        if  usuario:
            usu = {
                    'status': 'success',
                    'data': {
                        'idUsuario': usuario.idUsuario,
                        'correo': usuario.correo,
                        'admin': usuario.admin,
                        'registered_on': usuario.registered_on
                    }
                }
            return usu
        else:
            error = {
                'status': 'fail',
                'message': resp
            }
            return error


def tokenCheck(f):
   @wraps(f)
   def verificar(*args, **kwargs):
       token = None
       if 'token' in request.headers:
           token = request.headers['token']
 
       if not token:
           return jsonify({'message': 'token no encontrado'})
       try:
           info = obtenerInfo(token)
           print(info)
           if info['status'] == "fail":
            return jsonify({'message': 'token is invalid'})
       except:
           return jsonify({'message': 'token is invalid'})
       print("hi")
       return f(info['data'], *args, **kwargs)
   return verificar