import sqlite3
import json

class baseDatos:

    URL = "pokeBaseDatos.db"

    def recuperarStatsPokemon(self,idPokemon):
        con = sqlite3.connect("pokeBaseDatos.db")
        cur = con.cursor()
        
        for row in cur.execute('SELECT * FROM pokemon WHERE id='+str(idPokemon)):            
            print(row)
            print(row[0])
            data_set = {'id':str(row[0]),'nombre':str(row[1]),'total': str(row[3]),'hp':str(row[4]),'attack':str(row[5]),'defense':str(row[6]),'specialAttack':str(row[7]),'specialDefense':str(row[8]),'speed':str(row[9]),'generation':str(row[10])}
            json_dump = json.dumps(data_set)
            print(json_dump)
            y = json.loads(json_dump)
            print(y["nombre"])
            return json_dump
