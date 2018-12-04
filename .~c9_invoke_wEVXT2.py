### cliente
import socket, pickle
import time
import timeit
import sys
from datetime import datetime
import datetime
import json
import os

#loop de 5 veses para calcular a media

#vetor para armazenar os 5 valores do RTT
meuVetor = []
print time.strftime('%d/%M/%Y %H:%M')
for x in range(1, 6):
    #enviando mensagem
    HOST = '198.199.112.176'      # Endereco IP do Servidor
    PORT = 8081             # Porta que o Servidor esta
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    dest = (HOST, PORT)

    msg = 'hora'
    udp.sendto (msg, dest)
    
    #Tempo em que a mensagem sai para o servidor.
    tempo_inicial = timeit.default_timer()
    print ('Enviando msg: %s,\n         Destino: %s,\n         Tempo inicio: %s\n' % (msg, dest, tempo_inicial))
    udp.close()
    
    #recebendo mensagem
    HOST = '127.0.0.1'              # Endereco IP de recebimento
    PORT = 8082                     # Porta de recebimento
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    orig = (HOST, PORT)
    udp.bind(orig)
    #recebendo data e tempo:
    data, cliente = udp.recvfrom(1024)
    data_arr = pickle.loads(data)
    #data_arr[1] significa o valor do tempo de execução do servidor
    #data_arr[1] significa o valor do tempo de execucao do servidor
    #data_arr[0] significa a data e hora que o srvidor enviou
    print 'Received', repr(data_arr)
    msg = data_arr[1]
    print 'estou aqui'
    print msg


    #print ('%s' % (dados,))
    
    #tempo que a mensagem chega no servidor
    tempo_final = timeit.default_timer()  #TS4
    print ('Recebendo msg: %s,\n         Do cliente: %s,\n         Tempo fim: %s\n' % (msg, cliente, tempo_final))
    
    
    media_rodada = tempo_final - tempo_inicial      #(ts4  ts1)
    #print((msg))
    #print((media_rodada))
    RTT = media_rodada - float(msg)
    print ('Rodada: %s\nTempo: %s\n' % (x,RTT))
    udp.close()
    meuVetor.append(RTT)
    #rtt_in_ms = round(recv_time_ms - send_time_ms, 3)
    #now = datetime.now()
    

print ('Media do RTT de ida e vinda: %sms' % ((sum(meuVetor) / float(len(meuVetor)))))

print ('Data e hora do servidor: %s' % (data_arr[0]))

print ('Microsegundo da data do servidor: %s' % (data_arr[0].microsecond ) )

data_arr[0] = data_arr[0]-datetime.timedelta(milliseconds=((sum(meuVetor) / float(len(meuVetor)))/2))
#dat.microsecond=data_arr[0].microsecond-((sum(meuVetor) / float(len(meuVetor)))/2)

dat = data_arr[0]
dat = dat-datetime.timedelta(microseconds=1)
print ('Microsegundo ajustado: %s' % (dat.microsecond ) )

print ('Data e hora do servidor ajustada para colocar no sistema do cliente: %s' % (data_arr[0]-datetime.timedelta(microseconds=1)))

print ('\nMedia do RTT de ida: %sms\n' % ((sum(meuVetor) / float(len(meuVetor)))/2))
#print ('O cliente deve ajustar a data e hora para: %s' % (data_arr[0]-((sum(meuVetor) / float(len(meuVetor)))/2)))


#Comando pra ajustar a data os.popen("date +%Y%m%d")

#Comando pra ajustar a hora os.popen("#date +%T -s "15:53:13" ")

   