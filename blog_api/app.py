from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///messages.db'
db = SQLAlchemy(app)

class Mensaje(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(100), nullable=False)
    mensaje = db.Column(db.Text, nullable=False)

    def to_dict(self):
        return {"id": self.id, "user": self.user, "mensaje": self.mensaje}

with app.app_context():
    db.create_all()

@app.route('/mensajes', methods=['GET'])
def obtener_mensajes():
    mensajes = Mensaje.query.all()
    return jsonify([m.to_dict() for m in mensajes])

@app.route('/mensajes/<int:id>', methods=['GET'])
def obtener_mensaje(id):
    mensaje = Mensaje.query.get_or_404(id)
    return jsonify(mensaje.to_dict())

@app.route('/mensajes', methods=['POST'])
def crear_mensaje():
    data = request.get_json()
    nuevo = Mensaje(user=data['user'], mensaje=data['mensaje'])
    db.session.add(nuevo)
    db.session.commit()
    return jsonify(nuevo.to_dict()), 201

@app.route('/mensajes/<int:id>', methods=['PUT'])
def actualizar_mensaje(id):
    mensaje = Mensaje.query.get_or_404(id)
    data = request.get_json()
    mensaje.user = data.get('user', mensaje.user)
    mensaje.mensaje = data.get('mensaje', mensaje.mensaje)
    db.session.commit()
    return jsonify(mensaje.to_dict())

@app.route('/mensajes/<int:id>', methods=['DELETE'])
def eliminar_mensaje(id):
    mensaje = Mensaje.query.get_or_404(id)
    db.session.delete(mensaje)
    db.session.commit()
    return jsonify({'mensaje': 'Eliminado correctamente'})

if __name__ == '__main__':
    app.run(debug=True)