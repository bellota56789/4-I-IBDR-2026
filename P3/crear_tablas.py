from flask import Flask, render_template, request, redirect, url_for, Response
from flask_mail import Mail, Message
import sqlite3
import csv
import io

app = Flask(__name__, template_folder='app/templates')
app.secret_key = 'clave_secreta_para_alertas'

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'indigolemus4@gmail.com'
app.config['MAIL_PASSWORD'] = 'ezjqnjtjakdphakn'
app.config['MAIL_DEFAULT_SENDER'] = 'indigolemus4@gmail.com'

mail = Mail(app)

def inicializar_db():
    conn = sqlite3.connect('control_escolar.db', timeout=20)
    cursor = conn.cursor()
    

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS alumnos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            correo TEXT NOT NULL,
            calificacion REAL NOT NULL,
            grupo TEXT,
            materia TEXT
        )
    ''')
    
    # Tabla de usuarios del sistema
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            correo TEXT UNIQUE NOT NULL,
            contrasena TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

inicializar_db()

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        correo = (request.form.get('correo') or '').strip()
        contrasena = (request.form.get('contrasena') or '').strip()
        
        # 🛡️ Cuenta Maestra de Respaldo por cualquier emergencia
        if correo == 'admin@admin.com' and contrasena == '12345':
            return redirect(url_for('index'))
            
        conn = sqlite3.connect('control_escolar.db', timeout=20)
        cursor = conn.cursor()
        
        
        cursor.execute("SELECT * FROM usuarios WHERE correo = ? AND contrasena = ?", (correo, contrasena))
        usuario_valido = cursor.fetchone()
        conn.close()
        
        if usuario_valido:
            return redirect(url_for('index')) 
        else:
           
            return "<h1>Usuario o contraseña incorrectos.</h1><p>Verifica tus datos en DBeaver.</p><a href='/login'>Volver a intentar</a>"
            
    return render_template('usuarios/login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        correo = (request.form.get('correo') or '').strip()
        contrasena = (request.form.get('contrasena') or '').strip()
        
        if correo and contrasena:
            conn = sqlite3.connect('control_escolar.db', timeout=20)
            cursor = conn.cursor()
            try:
                cursor.execute("INSERT INTO usuarios (correo, contrasena) VALUES (?, ?)", (correo, contrasena))
                conn.commit()
                return redirect(url_for('login'))
            except sqlite3.IntegrityError:
                return "<h1>Ese correo ya está registrado.</h1><a href='/register'>Volver</a>"
            finally:
                conn.close()
        else:
            return "<h1>Por favor llena todos los campos.</h1><a href='/register'>Volver</a>"
        
    return render_template('usuarios/register.html')

@app.route('/', methods=['GET', 'POST'])
def index():
    conn = sqlite3.connect('control_escolar.db', timeout=20)
    cursor = conn.cursor()

    if request.method == 'POST':
        nombre = request.form.get('nombre')
        correo = request.form.get('correo')
        calificacion = request.form.get('calificacion')
        grupo = request.form.get('grupo')
        materia = request.form.get('materia')
        
        if calificacion is None or nombre is None:
            conn.close()
            return redirect(url_for('index'))
            
        cursor.execute("INSERT INTO alumnos (nombre, correo, calificacion, grupo, materia) VALUES (?, ?, ?, ?, ?)", 
                       (nombre, correo, calificacion, grupo, materia))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))

    cursor.execute("SELECT * FROM alumnos")
    alumnos_guardados = cursor.fetchall()
    conn.close()
    
    return render_template('usuarios/index.html', alumnos=alumnos_guardados)

@app.route('/eliminar/<int:id>')
def eliminar(id):
    conn = sqlite3.connect('control_escolar.db', timeout=20)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM alumnos WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    conn = sqlite3.connect('control_escolar.db', timeout=20)
    cursor = conn.cursor()

    if request.method == 'POST':
        nuevo_nombre = request.form['nombre']
        nuevo_correo = request.form['correo']
        nueva_calificacion = request.form['calificacion']
        nuevo_grupo = request.form['grupo']
        nueva_materia = request.form['materia']
        
        cursor.execute("""
            UPDATE alumnos 
            SET nombre = ?, correo = ?, calificacion = ?, grupo = ?, materia = ?
            WHERE id = ?
        """, (nuevo_nombre, nuevo_correo, nueva_calificacion, nuevo_grupo, nueva_materia, id))
        
        conn.commit()
        conn.close()
        return redirect(url_for('index'))

    cursor.execute("SELECT * FROM alumnos WHERE id = ?", (id,))
    alumno = cursor.fetchone()
    conn.close()
    
    return render_template('usuarios/editar.html', alumno=alumno)

@app.route('/exportar')
def exportar():
    conn = sqlite3.connect('control_escolar.db', timeout=20)
    cursor = conn.cursor()
    cursor.execute("SELECT nombre, correo, calificacion, grupo, materia FROM alumnos")
    alumnos = cursor.fetchall()
    conn.close()

    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(['Nombre', 'Correo Electronico', 'Calificacion', 'Grupo', 'Materia'])
    
    for alumno in alumnos:
        writer.writerow(alumno)
    
    output.seek(0)
    return Response(
        output.getvalue(),
        mimetype="text/csv",
        headers={"Content-disposition": "attachment; filename=lista_alumnos.csv"}
    )

@app.route('/forget', methods=['GET', 'POST'])
def forget():
    if request.method == 'POST':
        correo_destino = request.form.get('correo', '').strip()
        
        conn = sqlite3.connect('control_escolar.db', timeout=20)
        cursor = conn.cursor()
        cursor.execute("SELECT contrasena FROM usuarios WHERE correo = ?", (correo_destino,))
        resultado = cursor.fetchone()
        conn.close()
        
        if resultado:
            contrasena_olvidada = resultado[0]
            try:
                msg = Message("Recuperación de Contraseña - Control Escolar", recipients=[correo_destino])
                msg.body = f"Hola,\n\nTu contraseña registrada es: {contrasena_olvidada}"
                mail.send(msg)
                return render_template('usuarios/exito.html')
            except Exception as e:
                return f"<h1>Error al enviar el correo: {e}</h1>"
        else:
            return "<h1>Este correo electrónico no está registrado.</h1><a href='/forget'>Volver</a>"
            
    return render_template('usuarios/forget.html')

if __name__ == '__main__':
    app.run(debug=True)