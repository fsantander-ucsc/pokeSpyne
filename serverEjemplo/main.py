from spyne import Application, rpc, ServiceBase, Iterable, Integer, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from baseDatos import baseDatos
import sqlite3
import json

platita = 0

#Metodo para transformar valores en tabla de tipo a los reales
def transformadorMultiplicador(valorTabla):
    if valorTabla == 0:
        return 0.0
    elif valorTabla == 1:
        return 0.5
    elif valorTabla == 2:
        return 1.0
    elif valorTabla == 3:
        return 2.0
    else:
        return 1.0

#Metodo que devuelve 1 si le pego y 0 si misseo
def hitChance():
    import random
    fallo = random.randint(0,100)
    if fallo >= 70:
        return 0
    else:
        return 1


#Clase principal, donde se inician los servicios (Objeto remoto)

class Pokemon(ServiceBase):
    
    #Elemento para acceder a los servicios de las clase baseDatos
    elemento = baseDatos()   

    """Tres comillas para documentar"""
    #Servicio de Saludo
    #Servicio saludo
    #Unicode = String
    #_returns = return     
    @rpc(Unicode,_returns=Unicode)
    #ctx = context
    #name = parametro de entrada
    def say_hello(ctx,name):
        """
        @param name, nombre
        @return Saludo con el nombre indicado
        """
        #u para indicar que es unicode
        return u'hello, '+name

    @rpc(Integer, Integer, _returns=Integer)
    def sum(ctx, x, y):
        """
        @param x valor a sumar
        @param y valor a sumar
        @return El resultado de la suma de x con y
        """
        return x+y

    #Servicio lista
    @rpc(Unicode, Integer, _returns = Iterable(Unicode))
    def list_hello(ctx, name, times):
        
        for i in range(times):
            #yield = es como un return
            #no retorna automáticamente
            #se mantiene en el for y como que lo itera
            #cuando se tienen todos los datos listos lo retorna
            yield u'Hello, %s' % name   
    
    # Servicio horoscopo
   
    @rpc(Integer, _returns=Unicode)
    def pokehoroscopo(ctx,anho):
        bd = baseDatos()
        """
        @param anho, variable integer que representa el año de nacimiento del usuario
        @return Entrega el signo zodiacal del horoscopo pokemon de acuerdo al año
        """
        signos = ["Umbreon",
            "Pikachu",
            "Piplup",
            "Jinx",
            "Gengar",
            "Latios",
            "Dragonite",
            "Torracat",
            "Phanpy",
            "Bulbasaur",
            "Breloom",
            "Arceus"]
        num_signo = (abs(2020 - anho)) % 12;
        if anho<2020:
            num_signo = 12 - num_signo

        return bd.recuperaId(signos[num_signo].upper())

    @rpc(Unicode, _returns = Iterable(Unicode))
    def pokebatalla(ctx, pokemonIngresado):
        print("el pokemon ingresado es:"+str(pokemonIngresado))
        bd = baseDatos()

        pokemonIngresado = pokemonIngresado.upper()
        # list que contendra el desarrollo de la batalla
        resumenBatalla = []
        
        # Se encuentra al azar al pokemon oponente
        datosIngreso = bd.recuperaId(pokemonIngresado)
        #idPokemonIngresado = datosIngreso["id"]
        print(datosIngreso)
        import random
        idPokemonRandom = random.randint(1,721)
        nombrePokemonRandom = bd.recuperaNombrePokemon(idPokemonRandom)
        # Recuperar pokemon ingresado y otro recuperado al azar
        # En el orden: tipo_id, hp, attack, defense, specialAttack, specialDefense, speed. 

        # recuerda saltarte el total
        statsPokemonIngresado=bd.recuperaStatsPokemon(pokemonIngresado)
        statsPokemonOponente=bd.recuperaStatsPokemon(nombrePokemonRandom)

        # stats, se utilizan at1 y def1 como variables base de ataque y defensa, pero si sus valores SP son mayores se les asigna ese valor 
        # cada pkmn se defendera con su defensa del tipo correspondiente al ataque mas alto del otro
        #recuperar velocidades para decidir orden de turnos
        speedIngresado = statsPokemonIngresado["speed"]
        speedRandom = statsPokemonOponente["speed"]
#data_set = {'id':str(row[0]),'hp':str(row[4]),'attack':str(row[5]),
# 'defense':str(row[6]),'specialAttack':str(row[7]),'specialDefense':str(row[8]),'speed':str(row[9])}

        if speedIngresado>=speedRandom:
            #Se le pasan los stats del pokemon del entrenador al pokemon que parte
            nombre1 = pokemonIngresado
            #recuperar nombre del pokemon random
            nombre2 = nombrePokemonRandom

            hp1 = float(statsPokemonIngresado["hp"])
            hp2 = float(statsPokemonOponente["hp"])

            atk1 = float(statsPokemonIngresado["attack"])
            atk2 = float(statsPokemonOponente["attack"])
            spA1 = float(statsPokemonIngresado["specialAttack"])
            spA2 = float(statsPokemonOponente["specialAttack"])

            def1 = float(statsPokemonIngresado["defense"])
            def2 = float(statsPokemonOponente["defense"])
            spD1 = float(statsPokemonIngresado["specialDefense"])
            spD2 = float(statsPokemonOponente["specialDefense"])

            #Se recupera el multiplicador dependiendo de los dos tipo de los pokemon 
            #En el argumento del transformador ingresar el int reucperado correspondiente
            #Falta implementar lo de recuperar la ventaja de tipo
            multiplicador1 = transformadorMultiplicador(bd.ventajaTipo(statsPokemonIngresado["tipo_id"],statsPokemonOponente["tipo_id"])) # tipo 11 vs tipo 1 = grass vs water = 3
            multiplicador2 = transformadorMultiplicador(bd.ventajaTipo(statsPokemonOponente["tipo_id"],statsPokemonIngresado["tipo_id"])) # tipo 1 vs tipo 11 = water vs grass = 2
        else:
            #Se le pasan los stats del pokemon del entrenador al pokemon que parte
            #recuperar nombre del pokemon random
            nombre2 = nombrePokemonRandom
            nombre1 = pokemonIngresado

            hp1 = float(statsPokemonOponente["hp"])
            hp2 = float(statsPokemonIngresado["hp"])

            atk1 = float(statsPokemonOponente["attack"])
            atk2 = float(statsPokemonIngresado["attack"])
            spA1 = float(statsPokemonOponente["specialAttack"])
            spA2 = float(statsPokemonIngresado["specialAttack"])

            def1 = float(statsPokemonOponente["defense"])
            def2 = float(statsPokemonIngresado["defense"])
            spD1 = float(statsPokemonOponente["specialDefense"])
            spD2 = float(statsPokemonIngresado["specialDefense"])

            #Se recupera el multiplicador dependiendo de los dos tipo de los pokemon 
            #En el argumento del transformador ingresar el int reucperado correspondiente
            #Falta implementar lo de recuperar la ventaja de tipo
            multiplicador1 = transformadorMultiplicador(bd.ventajaTipo(statsPokemonOponente["tipo_id"],statsPokemonIngresado["tipo_id"]))
            multiplicador2 = transformadorMultiplicador(bd.ventajaTipo(statsPokemonIngresado["tipo_id"],statsPokemonOponente["tipo_id"]))
        
        # se evalua que tipo de ataque y defensa usar para cada uno
        if atk1<spA1:
            atk1 = spA1
            def2 = spD2
        if atk2 < spA2:
            atk2 = spA2
            def1 = spD1

        # Informacio inicial batalla
        resumenBatalla.append("¡Un " + nombrePokemonRandom +" salvaje ha aparecido!\n\n")  
        resumenBatalla.append("El pokemon mas rapido es: " + nombre1+"\n")
        resumenBatalla.append(nombre1 + " tiene " + str(hp1) + " puntos de vida totales\n")
        resumenBatalla.append(nombre2 + " tiene " + str(hp2) + " puntos de vida totales\n");   
        resumenBatalla.append(nombre1 + " tiene " + str(multiplicador1) + " como multiplicador de tipo\n")
        resumenBatalla.append(nombre2 + " tiene " + str(multiplicador2) + " como multiplicador de tipo\n\nCOMIENZA BATALLA!\n")

        contadorTurnos = 0
        while hp1>0.0 and hp2>0.0:
            contadorTurnos = contadorTurnos+1
            hit = hitChance()

            if contadorTurnos%2 != 0:
                
                calculoDano = (atk1 * multiplicador1 - def2)
                if calculoDano <=0:
                    calculoDano = 5.0
                
                hp2 = hp2 - hit*calculoDano
                if hp2 < 0.0:
                    hp2 = 0.0
                    
                resumenTurno = "--TURNO " + str(contadorTurnos) + "--\n"+"EXITO DE GOLPE de " + nombre1 + " es: " + str(hit) + "\n"+ "DAÑO A REALIZAR por " + nombre1 + " es: " + str(hit * calculoDano) + "\n"+ "A " + nombre2 + " le queda " + str(hp2) + " puntos de vida\n"
            else:

                calculoDano = (atk2 * multiplicador2 - def1)
                if calculoDano <=0:
                    calculoDano = 5.0

                hp1 = hp1 - hit*calculoDano
                if hp1 < 0.0:
                    hp1 = 0.0

                resumenTurno = "--TURNO " + str(contadorTurnos) + "--\n"+"EXITO DE GOLPE de " + nombre2 + " es: " + str(hit) + "\n"+ "DAÑO A REALIZAR por " + nombre2 + " es: " + str(hit * calculoDano) + "\n"+ "A " + nombre1 + " le queda " + str(hp1) + " puntos de vida\n"
            
            resumenBatalla.append(resumenTurno)

            if (hp1<=0.0 or hp2<=0.0):
                resumenTurno = "¡¡BATALLA TERMINADA!!"
                if hp1 > hp2:
                    resumenTurno = resumenTurno + " " + nombre1 + " ES EL GANADOR"
                    #Se agrega dinero si el pokemon1 coincide con el ingresado, en caso contrario se resta
                    if(nombre1==pokemonIngresado):
                        Pokemon.elemento.agregarMonto(100)
                    else:
                        Pokemon.elemento.quitarMonto(50)
                else:
                    resumenTurno = resumenTurno + " " + nombre2 + " ES EL GANADOR"
                    #Se agrega dinero si el pokemon1 coincide con el ingresado, en caso contrario se resta
                    if(nombre2==pokemonIngresado):
                        Pokemon.elemento.agregarMonto(100)
                    else:
                        Pokemon.elemento.quitarMonto(50)
                resumenBatalla.append(resumenTurno)
        resumenBatalla.append(statsPokemonIngresado["id"])   
        resumenBatalla.append(str(idPokemonRandom))


                
        for i in resumenBatalla:
            yield u''+i
    
    #Servicio de consulta pokemon en base a una ID
    @rpc(Integer, _returns = Unicode)
    def consultaPokemon(ctx,idPokemon):          
        return Pokemon.elemento.recuperarStatsPokemon(idPokemon)
        
    #---Inicio servicios safari ---    
    #Servicio para iniciar e inicializar el Safari
    @rpc( _returns = Unicode)
    def safariPokemon(ctx):
        return Pokemon.elemento.safariPokemon();
    @rpc(_returns = Unicode)
    def arrojarPokebola(ctx):    
        return Pokemon.elemento.arrojarPokebola();
    @rpc(_returns = Unicode)
    def arrojarBaya(ctx):    
        return Pokemon.elemento.arrojarBaya();
    @rpc(_returns = Unicode)
    def arrojarPiedra(ctx):    
        return Pokemon.elemento.arrojarPiedra();
    @rpc(_returns = Unicode)
    def huir(ctx):    
        return Pokemon.elemento.huir();
    @rpc( _returns = Iterable(Unicode))    
    def listaSafari(ctx):
        print(Pokemon.elemento.arrayPokemon)    
        for i in Pokemon.elemento.arrayPokemon:
            yield u''+i['nombre']

   #Esta funcionalidad regresa toda la información
    @rpc( _returns = Iterable(Unicode))    
    def listaSafariCompleto(ctx):
        print(Pokemon.elemento.arrayPokemon)     
        for i in Pokemon.elemento.arrayPokemon:
            yield u''+json.dumps(i)
    #--- Fin servicios Safari ----

    @rpc(_returns = Integer)
    def getBalance(ctx):
        return Pokemon.elemento.getBalance()
    
    @rpc(Integer, _returns = Integer)
    def agregarAlBalance(ctx, monto):
        return Pokemon.elemento.agregarMonto(monto)
    
    @rpc(Integer, _returns = Integer)
    def quitarAlBalance(ctx, monto):
        return Pokemon.elemento.quitarMonto(monto)

    
#hola
#Crear un ejemplar de la aplicación, indicando los protocolos de entrada y salidad.
application = Application([Pokemon],'spyne.examples.hello.soap',
                            in_protocol=Soap11(validator='lxml'),
                            out_protocol=Soap11())

#Servidor para modo debug
wsgi_application = WsgiApplication(application)

# Parámentros de inicio de la aplicación
if __name__ == '__main__':
    import logging
    from wsgiref.simple_server import make_server

    logging.basicConfig(level=logging.DEBUG)

    server = make_server('127.0.0.1',8000,wsgi_application)

    print("Ejecutando servidor")    
    server.serve_forever()
