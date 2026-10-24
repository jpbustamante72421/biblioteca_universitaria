from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/inicio')
def home():
    return render_template('index.html', titulo='Inicio', mensaje='Bienvenido a la Biblioteca Universitaria')

@app.route('/catalogo')
def catalogo():
    return render_template('catalogo.html', titulo='Catálogo', mensaje='Explora el catálogo de materiales disponibles')

@app.route('/servicios')
def servicios():
    return render_template('servicios.html', titulo='Servicios', mensaje='Conoce los servicios que ofrece la biblioteca')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html', titulo='Contacto', mensaje='Comunicarse con la biblioteca universitaria')

if __name__ == '__main__':
    app.run(debug=True, port=5050)