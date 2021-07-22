import sqlite3
import json
from random import seed
from random import randint

class baseDatos:

    URL = "pokeBaseDatos.db"
    pokemonSafari = ""
    cantidadPokebola="10"
    probabilidadHuir="20"
    probabilidadCaptura="20"

    def recuperarStatsPokemon(self,idPokemon):
        con = sqlite3.connect("pokeBaseDatos.db")
        cur = con.cursor()
        
        for row in cur.execute('SELECT * FROM pokemon WHERE id='+str(idPokemon)):
            #imprime la linea completa            
            print(row)
            #imprime el elemento en la posición 0
            print(row[0])
            #se supone que creo un json
            data_set = {'id':str(row[0]),'nombre':str(row[1]),'total': str(row[3]),'hp':str(row[4]),'attack':str(row[5]),'defense':str(row[6]),'specialAttack':str(row[7]),'specialDefense':str(row[8]),'speed':str(row[9]),'generation':str(row[10])}
            #podría devolver esto y era
            json_dump = json.dumps(data_set)
            print(json_dump)
            #pruba para pasar el json a un array de python
            y = json.loads(json_dump)
            #creo que se crea un diccionario, supongoque de inicio podría crear uno  ¯\_(ツ)_/¯
            #imprimir el elemento que responde a nombre
            print(y["nombre"])
            #ya acá retorno el objeto para devolverlo al cliente
            #asd
            return json_dump

    def safariPokemon(self):
     
        seed(1)
        idPokemon = randint(0, 721)

        con = sqlite3.connect("pokeBaseDatos.db")
        cur = con.cursor()
        
        for row in cur.execute('SELECT * FROM pokemon WHERE id='+str(idPokemon)):
            data_set = {'id':str(row[0]),'nombre':str(row[1]),'msg':row[1]+' Salvaje ha aparecido!'} 
            json_dump = json.dumps(data_set)
        
        print("json_dump")
        return json_dump
