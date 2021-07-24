from wtforms import Form

from wtforms import DecimalField, IntegerField, StringField, FieldList, TextField

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
    pokemon = IntegerField('ID Pokémon')
class safariPokemon(Form):
    """docstring for SumForm."""
    opcion = IntegerField()
