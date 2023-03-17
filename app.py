
import math
import flask
from flask import (Flask, render_template)
from dash import html

app = Flask(__name__)
app.debug = True
app.title = 'MAPA INTERACTIVO'


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

@app.route('/articulo1')
def articulo1():
    return render_template( 'articulo1.html')

@app.route('/articulo2')
def articulo2():
    return render_template('articulo2')

@app.route('/articulo3')
def articulo3():
    return render_template( 'articulo3')

@app.route('/articulo4')
def articulo4():
    return render_template( 'articulo4')

@app.route('/articulo5')
def articulo5():
    return render_template( 'articulo5')

@app.route('/articulo6')
def marticulo6():
    return render_template( 'articulo6')

@app.route('/articulo7')
def articulo7():
    return render_template( 'articulo7')

@app.route('/articulo8')
def articulo8():
    return render_template( 'articulo8')

@app.route('/articulo9')
def articulo9():
    return render_template( 'articulo9')

@app.route('/articulo10')
def articulo10():
    return render_template( 'articulo10')

@app.route('/articulo11')
def articulo11():
    return render_template( 'articulo11')

@app.route('/articulo12')
def articulo12():
    return render_template( 'articulo12')

@app.route('/articulo13')
def articulo13():
    return render_template( 'articulo13')

@app.route('/articulo14')
def articulo14():
    return render_template( 'articulo14')

@app.route('/articulo15')
def articulo15():
    return render_template( 'articulo15')


if __name__ == '__main__':
    app.run()