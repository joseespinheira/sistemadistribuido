# -*- coding: utf-8 -*-
# vim:ts=4:sw=4:et:tw=120:sm
#
# =============================================
# Trabalho de RDC
# CTDS Noite - Unibratec
# =============================================

import sys
import random
import socket
import matplotlib
matplotlib.use('Agg')
try:
    # for Python2
    import Tkinter
except ImportError:
    # for Python3
    import tkinter
from tkinter import *

from tkinter.filedialog import askopenfilename
from tkinter import filedialog
from tkinter import *
import tkinter.filedialog as fd
from tkinter import *

from tkinter import filedialog
from tkinter import *

host = "localhost"
DEFAULT_PORT = 3389
BUF_SIZE = 1024

def read_str(sock):
    buf = []
    while True:
        char = sock.recv(1)
        if char == '\0':
            break
        buf.append(char)
    return ''.join(buf)

class MainFrame(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.master.title("Cliente MD5")
        self.grid()

        self.welcome_socket = None
        self.message_socket = None

        self.server = StringVar()
        self.msg = StringVar()
        self.md5 = StringVar()
        self.msg_port = StringVar()

        self.server.set("localhost")

        Label(self, text="Servidor:").grid(row=1, sticky=W)
        Label(self, text="Mensagem:").grid(row=2, sticky=W)
        Label(self, text="MD5:").grid(row=3, sticky=W)

        Entry(self, textvariable=self.server).grid(row=1, column=1, sticky=W+E, columnspan=2)
        Entry(self, textvariable=self.msg).grid(row=2, column=1, sticky=W+E)
        Entry(self, textvariable=self.md5, state=DISABLED) \
             .grid(row=3, column=1, sticky=W+E, columnspan=2)
        Entry(self, textvariable=self.msg_port, state=DISABLED).grid(row=2, column=2, sticky=W+E)

        Button(self, text="Get Port", command=self.connect).grid(row=1,column=3,sticky=W+E)
        Button(self, text="Send", command=self.send).grid(row=2,column=3,sticky=W+E)
        Button(self, text="Quit", command=self.exit).grid(row=3,column=3,sticky=W+E)

    def connect(self):
        if self.welcome_socket:
            return

        try:
            self.welcome_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.welcome_socket.connect((self.server.get(), DEFAULT_PORT))
        except Exception as e:
            self.welcome_socket = None
            Dialog(self, title="Erro!", text="Servidor fora do ar!", \
                         bitmap='error', default=0, strings=('OK',))
            return

        self.msg_port.set(read_str(self.welcome_socket))

    def send(self):
        if not self.msg_port.get():
            Dialog(self, title="Erro!", text="Porta não definida", \
                         bitmap='error', default=0, strings=('OK',))
            return

        if self.message_socket is None:
            self.message_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.message_socket.connect((self.server.get(), int(self.msg_port.get())))

        self.message_socket.send("%s\0" % self.msg.get())
        md5 = read_str(self.message_socket)
        self.md5.set(md5)

        self.message_socket.close()
        self.message_socket = None
        self.welcome_socket = None
        self.msg_port.set("")


    def exit(self):
        if self.welcome_socket:
            self.welcome_socket.close()
        if self.message_socket:
            self.message_socket.close()
        self.quit()

if __name__=="__main__":
    myapp = MainFrame()
    myapp.mainloop()