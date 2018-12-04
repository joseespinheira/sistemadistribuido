### servidor
#from datetime import datetime
import socket, pickle
import time
import timeit
import sys
import datetime
import json
import os
#os.getenv(PORT, 8080)
while True:
    
    #HOST = socket.gethostbyname('sisdistribuido-jose-espinheira.cs50.io')              # Endereco IP do Servidor
    HOST = 'localhost'   
    PORT = 8081                     # Porta que o Servidor esta
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    orig = (HOST, PORT)
    udp.bind(orig)
    print ('\n\nOuvindo... %s' % (orig,))
    #recebe a mensagem
    msg, cliente = udp.recvfrom(1024)
    if msg=='hora':
        tempo_servidor = timeit.default_timer()
        print ('Tempo inicial: %s' % (tempo_servidor,))
        udp.close()
        
        #porcessa alguma coisa
        print ('processando...')
        for i in range(1, 2):
            time.sleep(1)
        #imprimi o cliente
        print ('-------------------------------')
        print ('Enviado de:')
        print (cliente, msg)
        print ('-------------------------------')
        #Enviando mensagem de volta
        HOST = '127.0.0.1'  # Endereco IP do Servidor
        PORT = 8082            # Porta que o Servidor esta
        udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        dest = (HOST, PORT)
        
        tempo_saida_servidor = timeit.default_timer()
        print ('Tempo final: %s' % (tempo_saida_servidor,))
        tempo_gasto_servidor = tempo_saida_servidor - tempo_servidor
        data = datetime.datetime.now()
        minhadata = os.popen("date +%Y%m%d") #encaminhar o conteudo dessa variavel
        minhahora = os.popen("date +%T") #encaminhar essa variavel para o cliente
      
        msg = str(tempo_gasto_servidor)
        
        arr1 = [data,msg]
        #arr2 = [4,5,6]
        #someVar = 7
        data_string = pickle.dumps(arr1)
        #socket.send(data.encode())
        #data = json.dumps({"a": arr1, "b": arr2, "c": someVar})
        #socket.send(data.encode())
        
        print ('Diferenca: %s' % (tempo_gasto_servidor,))
        print ('-------------------------------')
        print ('Enviando a resposta para:')
        print dest, msg
        print ('-------------------------------')
        #while msg <> '\x18':
        udp.sendto (data_string,dest)
        udp.close()
    else: 
        if msg == 'sair':
            print ('bye, bye')
            sys.exit()
        else:
            print cliente, msg
            
# Comando pra pegar a hora  minhahora = os.popen("date +%Y%m%d")            