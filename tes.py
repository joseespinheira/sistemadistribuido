# -*- coding: utf-8 -*-
# vim:ts=4:sw=4:et:tw=120:sm
#
# =============================================
# Trabalho de Redes de Computadores
# CTDS Noite - Unibratec
# =============================================

# SERVER

import sys
import random
import md5
from SocketServer import ThreadingMixIn, TCPServer, StreamRequestHandler

DEFAULT_HOST = ""
DEFAULT_PORT = 3389
BUF_SIZE = 1024

class MessageHandler(StreamRequestHandler):
    def handle(self):
        print "waiting msg..."
        buf = []
        while True:
            char = self.rfile.read(1)
            if char == '\0':
                break
            buf.append(char)
        msg = ''.join(buf)
        print "Recebi a mensagem:", msg

        md5_hex = md5.md5(msg).hexdigest()
        print "MD5 Hex:", md5_hex,

        self.wfile.write("%s\0" % (md5_hex))
        print "wrote."

class WelcomeHandler(StreamRequestHandler):
    def handle(self):
        print "Recebi uma conexão de:", self.client_address

        random_port = random.randint(1025, 0xFFFF)
        print "Ouvindo mensagem na porta:", random_port

        message_socket = TCPServer((DEFAULT_HOST, random_port), MessageHandler)
        self.wfile.write("%s\0" %(str(random_port)))

        message_socket.handle_request()

class MyServer(ThreadingMixIn, TCPServer):
    allow_reuse_address = 1

def main():
    welcome_sock = MyServer((DEFAULT_HOST, DEFAULT_PORT), WelcomeHandler)
    print "Ouvindo a porta:", DEFAULT_PORT
    welcome_sock.serve_forever()

if __name__ == '__main__':
    main()