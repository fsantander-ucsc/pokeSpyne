from wtforms import Form
from wtforms import DecimalField, IntegerField, StringField, FieldList, TextField, SelectField
from flask import request
class HelloForm(Form):
    """docstring for HelloForm."""
    name = StringField('name')

class SumForm(Form):
    """docstring for SumForm."""
    param1 = IntegerField('param1')
    param2 = IntegerField('param2')

class ListHelloForm(Form):
    """docstring for SumForm."""
    name = StringField('name')
    times = IntegerField('times')

class consultaPokemon(Form):
    """docstring for SumForm."""
    pokemon = IntegerField('pokemon')

class pokeHoroscopoForm(Form):
    anho = IntegerField('año')

def pokeBatallaForm(listaPokemonActualizada):
    class MyForm(Form):
        pokemonIngresado = SelectField(u'Selecciona tu Pokemon', choices = listaPokemonActualizada)
    return MyForm(request.form) 

#class pokeBatallaForm2(Form):
 #   listaPokemon=["EEVEE"]
  #  def actualizaLista(self, listaActualizada):
   #     self.listaPokemon = listaActualizada

    #pokemonIngresado = SelectField(u'Selecciona tu Pokemon', choices = listaPokemon)




