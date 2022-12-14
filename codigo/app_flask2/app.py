from flask import Flask, render_template, request

app = Flask('Primera aplicacion flask')

contador_visitas = 0

@app.route('/') # url desde la que se accedera
def index():
    global contador_visitas
    contador_visitas += 1
    return f'''<html>
            <body>
            <H1> titulo 1</h1>
            <p> Hola desde <b>negrita</b> </p>
            <p> Visitas: {contador_visitas} </p>
            
            <a href='/lorem'> lorem </a> </br>
            <a href='/2'> index 2 </a> </br>
            
            <img src='static/flask-logo.webp' alt='logo de flask'/>
            </body>
            </html>
            '''

@app.route('/2')
def index2():
    global contador_visitas
    contador_visitas += 1
    return render_template('index2.html', contador_visitas = contador_visitas)

@app.route('/lorem')
def lorem_ipsum():
    global contador_visitas
    contador_visitas += 1
    return f'''<html>
            <body>
            <H1> lorem ipsum</h1>
            <p> Visitas: {contador_visitas} </p>
            </body>
            </html>
            '''
@app.route('/suma',methods=['GET','POST'])
def suma():
    if request.method == 'GET':
        contenido = '''<html>
                <head><title>Suma - resultado</title></head> <body>
                <form action="/suma" method="POST">
                    <label>Sumando 1:</label>
                    <input type="text" name="Sumando1"/>
                    <label>Sumando 2:</label>
                    <input type="text" name="Sumando2"/><br/><br/>
                    <input type="submit"/>
                </form>
                <body><html>'''
    elif request.method == 'POST':
        sumando1 = int(request.form.get('Sumando1'))
        sumando2 = int(request.form.get('Sumando2'))
        resultado = sumando1+sumando2
        contenido = f'Suma: {sumando1} + {sumando2} = {resultado}'
    else:
        contenido = 'Metodo no permitido'
    return contenido

@app.route('/tabla/<int:numero>')
def tabla_multiplicar(numero):
    cabecera = f'''<html>
                <head><title>Tabla del {numero}</title></head>
                <body> <table> '''
    tabla = ''
    for i in range(1,11):
        fila = f'<tr> <td> {numero} x {i} </td> <td> <b>=</b> </td> <td> {numero*i} </td></tr>'
        tabla += fila
    pie = '</table></body></html>'
    contenido = cabecera + tabla + pie
    return contenido
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=8080)