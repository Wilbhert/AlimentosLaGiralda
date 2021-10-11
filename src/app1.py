from logging import info
from flask import Flask, render_template, flash
from flask import request
from flask import redirect
from formularios import LogIn
from markupsafe import escape
import os


app1 = Flask(__name__)
app1.secret_key = os.urandom(24)  #Crear la clave secreta para csrf

# ----------------variables globales
sesion_iniciada = False   

# ----------------A partir de aqui las rutas -------------------
@app1.route('/')
@app1.route('/home/')
@app1.route('/index/')
def main():
    return render_template('home.html', titulo='Home::Alimentos la Giralda')


@app1.route("/login/", methods=["GET","POST"])
def login():
    frm = LogIn()
    global sesion_iniciada      #obliga a la asignaciones de sesion_iniciada buscar si existe la variable 

    if request.method == "GET":
        
        return render_template("login.html",form=frm, titulo='Login::Alimentos la Giralda')
    #Ingresa cuando se usa el method POST    
    else:
        sesion_iniciada = True
        #recuperar los datos del formulario
        log = escape(request.form['usr']) 
        cla = escape(request.form['pwd'])
        #validar los datos
        if len(log.strip())==0:
            flash('Por favor diligencie el usuario')
        if len(cla.strip())==0:
            flash('Por favor diligencie la clave')
        if log=='wilbhert' and cla=='123456789':
            flash('Acceso concedido')

            #return redirect("/usuario") # redirecciona a /usuario
            return "<h1>Parece que Entre</h1>"
        else:
            flash('Usuario o clave invalidos')
            return "<h1>Parece que Tienes un Usuario o contraseña equivocados</h1>"
        
        frm=LogIn() 

        ##return render_template("login.html",form=frm, titulo='Verificacion de acceso')
        #return redirect("/inicio") # redirecciona a /inicio


if __name__=='__main__':
    app1.run(debug=True, port=80)
