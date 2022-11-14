import requests
from bs4 import BeautifulSoup as bs

def tabla_conversion_monedas(moneda_origen = 'USD',moneda_destino = 'EUR',cantidad = 1.0):
    print(f'Tabla de conversion de monedas {moneda_origen} a {moneda_destino}')
    peticion = f'https://www.x-rates.com/table/?from={moneda_origen}&to={moneda_destino}&amount={cantidad}'
    respuesta = requests.get(peticion)

    if respuesta.status_code != 200:
        print('Se produjo un error')
        return
        
    contenido = respuesta.content

    soup = bs(contenido,'html.parser')
    
    span_fecha = soup.find_all('span',attrs={"class":"ratesTimestamp"})[0].text
    """if len(span_fecha) != 1:
        print('Error de parseado en in:',span_fecha)
        return"""
    texto_fecha = span_fecha#[1].text
    
    tablas_cambio = soup.find_all('table')
    tasas_cambio = {}
    
    for tasa_cambio in tablas_cambio:
        for tr in tasa_cambio.find_all('tr'):
            tds = tr.find_all('td')
            if tds:
                moneda = tds[0].text
                cambio = float(tds[1].text)
                tasas_cambio[moneda] = cambio
                
    print(f'Tasas de cambio del {texto_fecha} de {moneda_origen} a: ')   
    for moneda,tasa_cambio in tasas_cambio.items():
        print(moneda,'->',tasa_cambio)

def conversion_monedas(moneda_origen = 'USD',moneda_destino = 'EUR',cantidad = 1.0):
    print(f'Conversion de monedas {moneda_origen} a {moneda_destino}')
    peticion = f'https://www.x-rates.com/calculator/?from={moneda_origen}&to={moneda_destino}&amount={cantidad}'
    respuesta = requests.get(peticion)

    if respuesta.status_code != 200:
        print('Se produjo un error')
        return
        
    contenido = respuesta.content

    soup = bs(contenido,'html.parser')

    span_In_value = soup.find_all('span',attrs={"class":"ccOutputTxt"})
    if len(span_In_value) != 1:
        print('Error de parseado en in:',span_In_value)
        return
    
    texto_In = span_In_value[0].text

    span_Out_value = soup.find_all('span',attrs={"class":"ccOutputRslt"})
    if len(span_Out_value) != 1:
        print('Error de parseado en out:',span_Out_value)
        return
    
    texto_Out = span_Out_value[0].text
    
    span_fecha = soup.find_all('span',attrs={"class":"calOutputTS"})[0].text
    
    texto_fecha = span_fecha# [0].text
    
    print(f'{texto_In} -> {texto_Out}  -  {texto_fecha}') 
   
conversion_monedas()

tabla_conversion_monedas()