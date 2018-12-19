import datetime
from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client

def today(data):
    print(data.__class__)
    print(datetime.datetime(data))
    
    converted = datetime.datetime.strptime(data.value, "%Y%m%dT%H:%M:%S")
    print("Today: %s" % converted.strftime("%d.%m.%Y, %H:%M:%S"))
    print(datetime.datetime.today() - data )
    agora = datetime.datetime.today() - data.date
    print("Agora %s" % agora)
    today = datetime.datetime(2018,10,5,13,9,56,601120)#datetime.datetime.today() 
    return xmlrpc.client.DateTime(today)

server = SimpleXMLRPCServer(("localhost", 8000))
print("Listening on port 8000...")
server.register_function(today, "today")
server.serve_forever()