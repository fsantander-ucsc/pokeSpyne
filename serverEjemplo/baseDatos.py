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

<<<<<<< HEAD
    #Se define metodo necesario para recuperar el nombre de un pokemon de acuerdo a su id
    def recuperaNombrePokemon(self,idPokemon):
        con = sqlite3.connect("pokeBaseDatos.db")
        cur = con.cursor() 

        for row in cur.execute('SELECT * FROM pokemon WHERE id='+str(idPokemon)):
            data_set = {'nombre':str(row[1])}
            json_dump = json.dumps(data_set)
            y = json.loads(json_dump)
            return y["nombre"]

    def recuperaStatsPokemon(self, nombrePokemon):
        con = sqlite3.connect("pokeBaseDatos.db")
        cur = con.cursor() 

        statsPokemon = []
        nombrePokemon = nombrePokemon.upper()

        for row in cur.execute('SELECT * FROM pokemon WHERE pokemon.name="'+str(nombrePokemon)+'"'):
            data_set = {'id':str(row[0]),'tipo_id':str(row[2]),'hp':str(row[4]),'attack':str(row[5]),'defense':str(row[6]),'specialAttack':str(row[7]),'specialDefense':str(row[8]),'speed':str(row[9])}
            json_dump = json.dumps(data_set)
            statsPokemon = json.loads(json_dump)

            return statsPokemon

    def recuperaNombreTipo(self, id):
        con = sqlite3.connect("pokeBaseDatos.db")
        cur = con.cursor() 

        for row in cur.execute('SELECT * FROM tipo WHERE id='+str(id)):
            data_set = {'nombre':str(row[1])}
            json_dump = json.dumps(data_set)
            y = json.loads(json_dump)
            return y["nombre"].lower()


    def ventajaTipo(self, idTipoA, idTipoB):
        con = sqlite3.connect("pokeBaseDatos.db")
        cur = con.cursor() 

        nombreTipoB = baseDatos.recuperaNombreTipo(self, idTipoB)

        for row in cur.execute('SELECT * FROM tipo WHERE id='+str(idTipoA)):
            data_set = {'name':str(row[0]),'steel':str(row[1]),'water':str(row[2]),'bug':str(row[3]),'dragon':str(row[4]),'electric':str(row[5]),'ghost':str(row[6]),'fire':str(row[7]),'fairy':str(row[8]),'ice':str(row[9]),'fight':str(row[10]),'normal':str(row[11]),'grass':str(row[12]),'psychic':str(row[13]),'rock':str(row[14]),'dark':str(row[15]),'ground':str(row[16]),'poison':str(row[17]),'flying':str(row[18])}
            json_dump = json.dumps(data_set)
            y = json.loads(json_dump)
            return float(y[nombreTipoB])
    
    def recuperaId(self, nombrePokemon):
        con = sqlite3.connect("pokeBaseDatos.db")
        cur = con.cursor() 

        for row in cur.execute('SELECT * FROM pokemon WHERE name="'+str(nombrePokemon)+'"'):
            data_set = {'id':str(row[0]),'nombre':str(row[1])}
            json_dump = json.dumps(data_set)
            return json_dump

    
=======
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
>>>>>>> 671eb8febddcafc0446f88adcd3ac46a1a350a16
