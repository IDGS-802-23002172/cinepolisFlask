from flask import Flask, render_template, request
from flask import flash
from flask_wtf.csrf import CSRFProtect
import forms


app=Flask(__name__)
app.secret_key = 'Clave secreta Majo'
csrf = CSRFProtect(app)

@app.route('/')
def index():
    cine_class = forms.CineForm(request.form) 
    titulo = "Cinepolis"
    return render_template('index.html', titulo=titulo, form=cine_class)

@app.route("/cinepolis", methods=["GET", "POST"])
def cinepolis():
    nom, nCom, nBol, tCin = "", 0, 0, 0 
    total = 0
    cine_class = forms.CineForm(request.form)

    if request.method == "POST" and cine_class.validate():
        print("Datos recibidos:", request.form)
        nom = cine_class.nombre.data
        nCom = cine_class.nCompradores.data
        nBol = cine_class.nBoletos.data
        tCin = cine_class.tCineco.data
        limite = nCom * 7
        if nBol > limite:
            flash(f"Error: No puedes comprar más de 7 boletos por persona", "error")
            return render_template("index.html", form=cine_class, nom=nom)

        total = nBol * 12
        
        if nBol > 5:
            total = total * 0.85
        elif nBol >= 3:
            total = total * 0.90
        
        if tCin == 1:
            total = total * 0.90
            
    return render_template("index.html", form=cine_class, valor=total, nom=nom, nCom=nCom, nBol=nBol, tCin=tCin)

if __name__  == '__main__':

    app.run(debug=True)
