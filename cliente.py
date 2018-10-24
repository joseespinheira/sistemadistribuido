### cliente
import socket
import time
import timeit
import sys


#loop de 5 veses para calcular a media

#vetor para armazenar os 5 valores do RTT
meuVetor = []

for x in range(1, 6):
    #enviando mensagem
    HOST = '127.0.0.1'      # Endereco IP do Servidor
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
    
    msg, cliente = udp.recvfrom(1024)
    print ''
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
print('\nMedia: %sms' % (sum(meuVetor) / float(len(meuVetor))))
#print(  )
#print mean(meuVetor)