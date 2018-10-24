### servidor
#from datetime import datetime
import socket
import time
import timeit
import sys

while True:
    
    HOST = '127.0.0.1'              # Endereco IP do Servidor
    PORT = 8081            # Porta que o Servidor esta
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
        
        print ('Diferenca: %s' % (tempo_gasto_servidor,))
        print ('-------------------------------')
        print ('Enviando a resposta para:')
        print dest, msg
        print ('-------------------------------')
        msg = str(tempo_gasto_servidor)
        #while msg <> '\x18':
        udp.sendto (msg, dest)
        udp.close()
    else: 
        if msg == 'sair':
            print ('bye, bye')
            sys.exit()
        else:
            print cliente, msg
        