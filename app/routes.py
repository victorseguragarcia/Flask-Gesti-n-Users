from flask import render_template, redirect, url_for, flash, session, request
from app import app, db
from app.models import Usuario

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        usuario = Usuario.query.filter_by(email=email).first()
        if usuario.email and usuario.check_password(password):
            session['user_id'] = usuario.id
            flash('Inicio de sesión exitoso.', 'success')
            return redirect(url_for('tablecontent'))  # Redirigir a 'tablecontent' después de iniciar sesión
        else:
            flash('Credenciales incorrectas. Inténtalo de nuevo.', 'danger')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('Has cerrado sesión.', 'info')
    return redirect(url_for('login'))

@app.route('/')
def index():
    if 'user_id' not in session:
        flash('Por favor, inicia sesión para continuar.', 'warning')
        return redirect(url_for('login'))
    usuarios = Usuario.query.all()
    return render_template('index.html', usuarios=usuarios)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        email = request.form['email']
        password = request.form['password']

        if Usuario.query.filter_by(email=email).first():
            flash('El correo electrónico ya está registrado.', 'danger')
            return redirect(url_for('register'))

        nuevo_usuario = Usuario(nombre=nombre, apellido=apellido, email=email)
        nuevo_usuario.set_password(password)
        db.session.add(nuevo_usuario)
        db.session.commit()
        flash('Registro exitoso. Ahora puedes iniciar sesión.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/tablecontent')
def tablecontent():
    if 'user_id' not in session:
        flash('Por favor, inicia sesión para continuar.', 'warning')
        return redirect(url_for('login'))
    
    # Aquí puedes añadir la lógica que necesitas para mostrar datos
    usuarios = Usuario.query.all()
    return render_template('tablecontent.html', usuarios=usuarios)
