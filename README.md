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
O servidor verifica sua hora local e responde ao cliente com esta informação;
O cliente atualiza seu relógio com a hora informada pelo servidor somada ao tempo de comunicação verifica antes pelo RTT.
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
    
    vai processar algo
    
    Irá responder para o cliente
    
    
o cliente deverá exibir:
    (em construção)



-
--
---
----
-----




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




     ,-----.,--.                  ,--. ,---.   ,--.,------.  ,------.
    '  .--./|  | ,---. ,--.,--. ,-|  || o   \  |  ||  .-.  \ |  .---'
    |  |    |  || .-. ||  ||  |' .-. |`..'  |  |  ||  |  \  :|  `--, 
    '  '--'\|  |' '-' ''  ''  '\ `-' | .'  /   |  ||  '--'  /|  `---.
     `-----'`--' `---'  `----'  `---'  `--'    `--'`-------' `------'
    ----------------------------------------------------------------- 


Welcome to your Python project on Cloud9 IDE!

To show what Cloud9 can do, we added a basic sample web application to this
workspace, from the excellent Python tutorial _Learning Python the Hard Way_.
We skipped ahead straight to example 50 which teaches how to build a web
application.

If you've never looked at the tutorial or are interested in learning Python,
go check it out. It's a great hands-on way for learning all about programming
in Python.

* _Learning Python The Hard Way_, online version and videos: 
http://learnpythonthehardway.org/book/

* Full book: http://learnpythonthehardway.org

## Starting from the Terminal

To try the example application, type the following in the terminal:

```
cd ex50
python bin/app.py
```

Alternatively, open the file in ex50/bin and click the green Run
button!

## Configuration

You can configure your Python version and `PYTHONPATH` used in
Cloud9 > Preferences > Project Settings > Language Support.

## Support & Documentation

Visit http://docs.c9.io for support, or to learn more about using Cloud9 IDE.
To watch some training videos, visit http://www.youtube.com/user/c9ide.