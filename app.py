
import flask
from flask import (Flask, render_template)

app = Flask(__name__)
app.debug = True
app.title = 'Mancuerfit'


@app.route('/')
def index():
    return render_template( 'index.html')

@app.route('/contacto')
def contacto():
    return render_template( 'contacto.html')

@app.route('/about')
def about():
    return render_template( 'about.html')

@app.route('/productos')
def productos():
    return render_template( 'productos.html')

@app.route('/blog')
def blog():
    return render_template( 'blog.html')

@app.route('/tamanomancuerna')
def tamanomancuerna():
    return render_template( 'articulo1.html')

@app.route('/costomancuerna')
def costomancuerna():
    return render_template('articulo2.html')

@app.route('/beneficiosmancuernas')
def beneficiosmancuernas():
    return render_template( 'articulo3.html')

@app.route('/cuidadomancuernas')
def cuidadomancuernas():
    return render_template( 'cuidadomancuernas.html')

@app.route('/ejerciciosmancuernas')
def ejerciciosmancuernas():
    return render_template( 'articulo5.html')

@app.route('/pesasrusas')
def pesasrusas():
    return render_template( 'articulo6.html')

@app.route('/pesopesasrusas')
def pesopesasrusas():
    return render_template( 'articulo7.html')

@app.route('/beneficiospesasrusas')
def beneficiospesasrusas():
    return render_template( 'articulo8.html')

@app.route('/ejericiospesasrusas')
def ejericiospesasrusas():
    return render_template( 'articulo9.html')

@app.route('/cuidadopesasrusas')
def cuidadopesasrusas():
    return render_template( 'articulo10.html')

@app.route('/pesodepesasrusas')
def pesodepesasrusas():
    return render_template( 'articulo11.html')

@app.route('/discosgimnasio')
def discosgimnasio():
    return render_template( 'articulo12.html')

@app.route('/discoshierro')
def discoshierro():
    return render_template( 'articulo13.html')

@app.route('/pesodiscos')
def pesodiscos():
    return render_template( 'articulo14.html')

@app.route('/discosbarra')
def discosbarra():
    return render_template( 'articulo15.html')

@app.route('/usarmancuernas')
def usarmancuernas():
    return render_template( 'articulo16.html')

@app.route('/materialesmancuernas')
def materialesmancuernas():
    return render_template( 'articulo17.html')

@app.route('/mancuernasajustables')
def mancuernasajustables():
    return render_template( 'articulo18.html')

@app.route('/pesasbarranquilla')
def pesasbarranquilla():
    return render_template( 'articulo19.html')

@app.route('/mancuernasbaratas')
def mancuernasbaratas():
    return render_template( 'articulo20.html')

if __name__ == '__main__':
    app.run()