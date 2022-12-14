from flask import Flask, render_template, request

app = Flask('Primera prueba con flask')

contador = 0

@app.route('/')
def index():
    global contador
    contador += 1
    return f'Hola, soy Flask! { contador }'


@app.route('/html')
def index_html():
    global contador
    contador += 1
    contenido = f"""<html>
            <head> <title> Titulo de la pagina </title> </head>
            <body>
            <H1> 1 nivel</H1>
            <H2> 2 nivel</H2>
            <p> un parrafo</p>
            <br/>
            <b> texto en negrita </b>
            <p> logo de flask </p>
            <img src = 'https://flask.palletsprojects.com/en/2.2.x/_images/flask-logo.png'>
            Visitas: { contador }
            </body>
            </html>
            """
    return contenido

@app.route('/html2')
def index_html2():
    global contador
    contador += 1
    contenido = render_template('index.html', contador = contador)
     
    return contenido

@app.route('/suma', methods = ['GET','POST'])
def suma():
    contenido = ''
    if request.method == 'GET':
        print('Peticion get')
        contenido = render_template('suma.html')
    elif request.method == 'POST':
        print('Peticion post')
        sumando1 = int(request.form.get('Sumando1'))
        sumando2 = int(request.form.get('Sumando2'))
        resultado = sumando1 + sumando2
        contenido = f'<html> {sumando1} + {sumando2} = {resultado}</html>'
    return contenido

if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0',port=5001)