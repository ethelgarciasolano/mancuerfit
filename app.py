
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

@app.route('/articulo1')
def articulo1():
    return render_template( 'articulo1.html')

@app.route('/articulo2')
def articulo2():
    return render_template('articulo2.html')

@app.route('/articulo3')
def articulo3():
    return render_template( 'articulo3.html')

@app.route('/articulo4')
def articulo4():
    return render_template( 'articulo4.html')

@app.route('/articulo5')
def articulo5():
    return render_template( 'articulo5.html')

@app.route('/articulo6')
def marticulo6():
    return render_template( 'articulo6.html')

@app.route('/articulo7')
def articulo7():
    return render_template( 'articulo7.html')

@app.route('/articulo8')
def articulo8():
    return render_template( 'articulo8.html')

@app.route('/articulo9')
def articulo9():
    return render_template( 'articulo9.html')

@app.route('/articulo10')
def articulo10():
    return render_template( 'articulo10.html')

@app.route('/articulo11')
def articulo11():
    return render_template( 'articulo11.html')

@app.route('/articulo12')
def articulo12():
    return render_template( 'articulo12.html')

@app.route('/articulo13')
def articulo13():
    return render_template( 'articulo13.html')

@app.route('/articulo14')
def articulo14():
    return render_template( 'articulo14.html')

@app.route('/articulo15')
def articulo15():
    return render_template( 'articulo15.html')

@app.route('/articulo16')
def articulo16():
    return render_template( 'articulo16.html')

@app.route('/articulo17')
def articulo17():
    return render_template( 'articulo17.html')

@app.route('/articulo18')
def articulo18():
    return render_template( 'articulo18.html')

if __name__ == '__main__':
    app.run()