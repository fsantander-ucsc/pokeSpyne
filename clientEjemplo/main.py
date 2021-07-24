#se importan bibliotecas y módulos
from flask import Flask
from flask import request
from flask import render_template
from zeep import Client, Settings
#se importan bibliotecas y módulos internos
import forms
import json

#conección con el servidor spyne
wsdl='http://localhost:8000/?wsdl'
settings = Settings(strict=True,xml_huge_tree=True)
rpc_client = Client(wsdl=wsdl,settings=settings)

#Ejemplar Flask para generar la app
app = Flask(__name__)

#Se definen las rutas del proyecto

#Página principal
@app.route('/')
def index():
    return render_template('index.html')

#Servicio saludo
@app.route('/service1',methods=['GET','POST'])
def service1():
    hello_form = forms.HelloForm(request.form)
    data=None
    if request.method == 'POST':
        data = rpc_client.service.say_hello(hello_form.name.data)
    return render_template('services/say_hello.html',form = hello_form, data = data)

#Servicio suma
@app.route('/service2',methods=['GET','POST'])
def service2():
    sum_form = forms.SumForm(request.form)
    data = None
    if request.method == 'POST':
        data = rpc_client.service.sum(sum_form.param1.data,sum_form.param2.data)
        print(data)
    return render_template('services/sum.html',form = sum_form, data = data)

#Servicio lista
@app.route('/service3',methods=['GET','POST'])
def service3():
    list_hello_form = forms.ListHelloForm(request.form)
    myList=[]
    if request.method == 'POST':
        myList = rpc_client.service.list_hello(list_hello_form.name.data,list_hello_form.times.data)
    return render_template('services/list_hello.html',form = list_hello_form, data = myList)

@app.route('/ConsultaPokemon',methods=['GET','POST'])
def consultaPokemon():
    consultaPokemon = forms.consultaPokemon(request.form)
    data=None
    if request.method == 'POST':
        data = rpc_client.service.consultaPokemon(consultaPokemon.pokemon.data)
        data = json.loads(data)
    return render_template('services/consulta_pokemon.html',form = consultaPokemon, data = data)

@app.route('/SafariPokemon',methods=['GET','POST'])
def safari():
    data=None
    if request.method == 'POST':
        mensaje = request.form["accion"]
        if mensaje =="init":
            data = rpc_client.service.safariPokemon()
        elif mensaje =="pokebola":
            data = rpc_client.service.arrojarPokebola()
        elif mensaje == "baya":
            data = rpc_client.service.arrojarBaya()
        elif mensaje == "piedra":
            data = rpc_client.service.arrojarPiedra()
        elif mensaje == "huir":
            data = rpc_client.service.huir()
       
        data = json.loads(data)        
        
    return render_template('services/safari_pokemon.html', data = data)

# Servicio pokehoroscopo
@app.route('/servicePokeHoroscopo', methods=['GET','POST'])
def servicePokeHoroscopo():
    horoscopo_form = forms.pokeHoroscopoForm(request.form)
    data = None

    if request.method=='POST':
        data = rpc_client.service.pokehoroscopo(horoscopo_form.anho.data)
        data = json.loads(data) 

    return render_template('services/pokehoroscopo.html', form = horoscopo_form, data=data)

# Servicio pokebatalla
@app.route('/servicePokeBatalla', methods=['GET','POST'])
def servicePokeBatalla():
    lista=["charmander","eevee"]
    batalla_form = forms.pokeBatallaForm(lista)#forms.pokeBatallaForm(request.form)
    myList=[]
    if request.method=='POST':
        myList = rpc_client.service.pokebatalla(batalla_form.pokemonIngresado.data) 

    return render_template('services/pokebatalla.html', form = batalla_form, data=myList)

# Parámentros de inicio de la aplicación
if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0')
