from app import db
from werkzeug.security import generate_password_hash, check_password_hash  # Importar las funciones necesarias

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    apellido = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)  # Usando "email" en lugar de "electronicmail"
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        """Cifra la contraseña"""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Verifica la contraseña"""
        return check_password_hash(self.password_hash, password)
