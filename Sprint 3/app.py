import os
from flask import Flask, render_template
app=Flask(__name__)

app.secret_key=os.urandom(24)

@app.route('/login')
def login():
    #TODO
    return render_template('Mockup1.html')

@app.route('/registro')
def registro():
    #TODO
    return render_template('Mockup2.html')

@app.route('/productos')
def productos():
    #TODO
    return render_template('Mockup3.html')

@app.route('/producto/añadir ')
def añadirProducto():
    #TODO
    return render_template('Mockup4.html')

@app.route('/producto/editar')
def editarProducto():
    #TODO
    return render_template('Mockup5.html')

@app.route('/producto/eliminar')
def eliminarProducto():
    #TODO
    return render_template('Mockup6.html')

@app.route('/producto/calificar')
def calificarProducto():
    #TODO
    return render_template('Mockup7.html')

# @app.route('/login')
# def login():
#     #TODO
#     return render_template('Mockup1.html')

# @app.route('/login')
# def login():
#     #TODO
#     return render_template('Mockup1.html')

# @app.route('/login')
# def login():
#     #TODO
#     return render_template('Mockup1.html')

if __name__=='__main__':
    app.run(debug=True)