from spyne import Application, rpc, ServiceBase, Iterable, Integer, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from baseDatos import baseDatos
import sqlite3
import json
#Clase principal, donde se inician los servicios (Objeto remoto)

class Pokemon(ServiceBase):
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
        """
        """
        for i in range(times):
            #yield = es como un return
            #no retorna automáticamente
            #se mantiene en el for y como que lo itera
            #cuando se tienen todos los datos listos lo retorna
            yield u'Hello, %s' % name   

    @rpc(Integer, _returns = Unicode)
    def consultaPokemon(ctx,idPokemon):
        elemento = baseDatos()        
        return elemento.recuperarStatsPokemon(idPokemon);

    @rpc( _returns = Unicode)
    def safariPokemon(ctx):
        print("entrada")
        elemento = baseDatos()        
        return elemento.safariPokemon();


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
