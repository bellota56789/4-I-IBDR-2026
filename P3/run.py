from flask import Flask, render_template, request, redirect, url_for, Response
from flask_mail import Mail, Message
import sqlite3
import csv
import io
import os

app = Flask(__name__, template_folder='app/templates')
app.secret_key = "llave_secreta_para_alertas"

# --- CONFIGURACIÓN DE GOOGLE GMAIL ---
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'lemospatatin@gmail.com'  # <--- Pon aquí tu correo real de Gmail
app.config['MAIL_PASSWORD'] = 'truhswxntjsglhjd'  # <--- Pon aquí la Contraseña de Aplicación de 16 letras
app.config['MAIL_DEFAULT_SENDER'] = 'lemospatatin@gmail.com' # <--- El mismo correo de arriba
mail = Mail(app)

ruta_db = r'C:\Users\romer\Desktop\Proyecto_escolar\control_escolar.db'

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return redirect(url_for('index'))
    return render_template("usuarios/login.html")

@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        correo = request.form.get("correo", "").strip()
        contrasena = request.form.get("contrasena", "").strip()
        
        if correo and contrasena:
            conn = sqlite3.connect(ruta_db, timeout=20)
            cursor = conn.cursor()
            try:
                cursor.execute("INSERT INTO usuarios (correo, contrasena) VALUES (?, ?)", (correo, contrasena))
                conn.commit()
                return redirect(url_for('login'))
            except sqlite3.IntegrityError:
                return "Este correo ya está registrado. <a href='/register'>Volver</a>"
            finally:
                conn.close()
        else:
            return "Por favor llene todos los campos. <a href='/register'>Volver</a>"
            
    return render_template("usuarios/register.html")

@app.route('/forget', methods=["GET", "POST"])
def forget():
    if request.method == "POST":
        correo = request.form.get("correo", "").strip()
        
        conn = sqlite3.connect(ruta_db, timeout=20)
        cursor = conn.cursor()
        cursor.execute("SELECT contrasena FROM usuarios WHERE correo = ?", (correo,))
        usuario = cursor.fetchone()
        conn.close()
        
        if usuario:
            contrasena_recuperada = usuario[0]
            
            msg = Message(
                "Recuperación de Contraseña - Control Escolar",
                recipients=[correo]
            )
            msg.body = f"Hola,\n\nHas solicitado recuperar tu contraseña de acceso al sistema.\nTu contraseña actual es: {contrasena_recuperada}\n\nPor favor, guarda tus datos de forma segura."
            
            try:
                mail.send(msg)
                
                return f"""
                <div style="font-family: 'Segoe UI', Roboto, Arial, sans-serif; max-width: 480px; margin: 80px auto; padding: 30px; border: 1px solid #c3e6cb; background-color: #d4edda; color: #155724; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); text-align: center;">
                    <div style="font-size: 40px; margin-bottom: 10px;">✉️</div>
                    <h3 style="margin-top: 0; font-size: 22px; font-weight: 600;">¡Correo Enviado Exitosamente!</h3>
                    <p style="font-size: 15px; line-height: 1.5; color: #1c5d2c;">Hemos enviado la contraseña a la dirección: <br><b>{correo}</b></p>
                    <p style="font-size: 13px; opacity: 0.9; margin-top: 15px;">Por favor, revisa tu bandeja de entrada o la carpeta de spam.</p>
                    <br>
                    <a href='/login' style="display: inline-block; background-color: #28a745; color: white; padding: 11px 22px; text-decoration: none; border-radius: 5px; font-weight: bold; font-size: 14px; transition: background 0.2s; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">Volver al Login</a>
                </div>
                """
            except Exception as e:
                return f"""
                <div style="font-family: 'Segoe UI', Roboto, Arial, sans-serif; max-width: 480px; margin: 80px auto; padding: 30px; border: 1px solid #c3e6cb; background-color: #d4edda; color: #155724; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); text-align: center;">
                    <div style="font-size: 40px; margin-bottom: 10px;">🔐</div>
                    <h3 style="margin-top: 0; font-size: 22px; font-weight: 600;">Solicitud Procesada</h3>
                    <p style="font-size: 15px; color: #1c5d2c;">La base de datos validó al usuario con éxito.</p>
                    <div style="background: white; padding: 12px; border-radius: 6px; margin: 15px 0; border: 1px solid #c3e6cb;">
                        <span style="font-size: 12px; color: #666; display: block;">CONTRASEÑA:</span>
                        <strong style="font-size: 24px; color: #28a745;">{contrasena_recuperada}</strong>
                    </div>
                    <br>
                    <a href='/login' style="display: inline-block; background-color: #28a745; color: white; padding: 11px 22px; text-decoration: none; border-radius: 5px; font-weight: bold; font-size: 14px;">Volver al Login</a>
                </div>
                """
        else:
            return f"""
            <div style="font-family: 'Segoe UI', Roboto, Arial, sans-serif; max-width: 480px; margin: 80px auto; padding: 30px; border: 1px solid #f5c6cb; background-color: #f8d7da; color: #721c24; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); text-align: center;">
                <div style="font-size: 40px; margin-bottom: 10px;">❌</div>
                <h3 style="margin-top: 0; font-size: 22px; font-weight: 600;">Usuario No Encontrado</h3>
                <p style="font-size: 15px; line-height: 1.5; color: #842029;">El correo electrónico <b>{correo}</b> no se encuentra registrado en nuestro sistema de control escolar.</p>
                <br>
                <a href='/forget' style="display: inline-block; background-color: #dc3545; color: white; padding: 11px 22px; text-decoration: none; border-radius: 5px; font-weight: bold; font-size: 14px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">Intentar de nuevo</a>
            </div>
            """
            
    # Regresa tu formulario original HTML si entra por GET
    return render_template("usuarios/forget.html")

            



@app.route('/', methods=["GET"])
def index():
    criterio = request.args.get("buscar", "").strip()
    
    conn = sqlite3.connect(ruta_db, timeout=20)
    cursor = conn.cursor()
    
    if criterio:
        cursor.execute("""
            SELECT id, nombre, correo, calificacion, grupo, materia FROM alumnos 
            WHERE nombre LIKE ? OR correo LIKE ? OR grupo LIKE ? OR materia LIKE ?
        """, (f"%{criterio}%", f"%{criterio}%", f"%{criterio}%", f"%{criterio}%"))
    else:
        cursor.execute("SELECT id, nombre, correo, calificacion, grupo, materia FROM alumnos")
        
    alumnos_filtrados = cursor.fetchall()
    conn.close()
    
    return render_template("usuarios/index.html", alumnos=alumnos_filtrados, criterio=criterio)

@app.route('/eliminar/<int:id>')
def eliminar(id):
    conn = sqlite3.connect(ruta_db, timeout=20)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM alumnos WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/editar/<int:id>', methods=["GET", "POST"])
def editar(id):
    conn = sqlite3.connect(ruta_db, timeout=20)
    cursor = conn.cursor()
    
    if request.method == "POST":
        nuevo_nombre = request.form['nombre']
        nuevo_correo = request.form['correo']
        nueva_calificacion = request.form['calificacion']
        
        cursor.execute("""
            UPDATE alumnos
            SET nombre = ?, correo = ?, calificacion = ?
            WHERE id = ?
        """, (nuevo_nombre, nuevo_correo, nueva_calificacion, id))
        
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
        
    else:
        cursor.execute("SELECT id, nombre, correo, calificacion, grupo, materia FROM alumnos WHERE id = ?", (id,))
        alumno = cursor.fetchone()
        conn.close()
        
        return render_template("usuarios/editar.html", alumno=alumno)

@app.route('/exportar')
def exportar():
    conn = sqlite3.connect(ruta_db, timeout=20)
    cursor = conn.cursor()
    cursor.execute("SELECT nombre, correo, calificacion FROM alumnos")
    alumnos = cursor.fetchall()
    conn.close()
    
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["Nombre", "Correo Electronico", "Calificacion"])
    
    for alumno in alumnos:
        writer.writerow(alumno)
        
    output.seek(0)
    return Response(
        output.getvalue(),
        mimetype="text/csv",
        headers={"Content-disposition": "attachment; filename=alumnos.csv"}
    )

if __name__ == '__main__':
    app.run(debug=True, port=5000)