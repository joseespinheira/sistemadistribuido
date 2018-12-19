Comunicação cliente-servidor e sincronização:
Desenvolver um servidor para sincronização de relógios e um cliente para utilizar este servidor.
A cada vez que o cliente desejar sincronizar seu relógio com o servidor deverá primeiro verificar o tempo de tráfego das mensagens entre ambos.
Isto será feito com entre o cliente e o servidor executando uma troca de mensagens para verificar o RTT (Round Trip Time) entre ambos;

RTT
O cliente envia uma mensagem para o servidor inserindo o timestamp (tempo atual de seu relógio) – ts1;
O servidor verifica o seu timestamp ao receber a mensagem – ts2;
O servidor envia um mensagem de resposta para o cliente inserindo os timestamps já verificados e o timestamp do envio – ts3;
O cliente ao receber a mensagem do servidor verifica o seu timestamp – ts4;
O cliente calcula o tempo médio de tráfego de mensagens com o servidor por: ((ts4 – ts1) – (ts3 – ts2)) / 2;
O RTT é verificado 5 vezes e calculada uma média;


O cliente envia mensagem solicitando a hora do relógio do servidor;


O servidor verifica sua hora local e 
responde ao cliente com esta informação;
O cliente atualiza seu relógio com a 
hora informada pelo servidor somada ao 
tempo de comunicação verifica antes pelo RTT.


Os programas devem ser feitos em Python, utilizando sockets e comunicação via UDP.


# execultando:
Para fazer o teste é preciso excultar dois terminais e em cada um dele colocar os comandos a seguir:

- terminal 1:

$ python servidor.py

- terminal 2:

$ python cliente.py

o servidor deverá exibir:
    (em construção)
    
    Ouvindo... ('127.0.0.1', 8081)
    
    Quando receber a mensagem exibirá o tempo inicial
    
    vai processar algo, no momento é um seep.
    
    Irá responder para o cliente com o tempo gasto.
    
    
o cliente deverá exibir:
    (em construção)


# Melhoramentos futuros:

- Colocar controle para perda de pacote.
- 

--------------------------------------------------




#import socket
HOST = '0.0.0.0'            # Endereco IP do Servidor
PORT = 8082                 # Porta que so cliente
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print 'Resposta do servidor\n'
orig = (HOST, PORT)
udp.bind(orig)
while True:
    msg, cliente = udp.recvfrom(1024)
    print cliente, msg
    #tempo que a mensagem chega no servidor
    recv_time_ms = datetime.now()
udp.close()

#rtt_in_ms = round(recv_time_ms - send_time_ms, 3)
#now = datetime.now()


sudo apt-get install openmpi-bin openmpi-common openmpi-dev openmpi-libs0 libmpich1.0c2 libmpich-mpd1.0c2 mpich-bin mpich-mpd-bin mpi-doc
-------------------------------------------------------

Trabalho final

fazer a sincronização da hora via RPC

para isso estou usando o arquivo cerv.py como servidor da aplicação.
e o arquivo fient.py como cliente que quer atualizar a hora.
