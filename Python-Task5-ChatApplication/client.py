import threading
import socket
import argparse
import os
import sys
import tkinter as tk 

class Send(threading.Thread):

    #Listens for user input from command line

    #sock the connected sock object

    #name (str) : the username provided by the user 

    def __init__(self, sock, name):
        super().__init__()
        self.sock = sock
        self.name = name

    def run(self):
        #Listen for user input from command line and send it to the server 

        #Typing "Quit" will close the connection and exit the app

        while True:
            print('{}:'.format(self.name), end = '')
            sys.stdout.flush()
            message = sys.stdin.readline()[:-1]

            #if we type "Quit" we leave the clatroom

            if message == "Quit":
                try:
                    self.sock.sendall('Server: {} has left the chat.'.format(self.name).encode('ascii'))

                except OSError:
                    pass

                try:
                    self.sock.shutsown(socket.SHUT_RDWR)

                except OSError:
                    pass

                self.sock.close()
                break


                # send message to server for broadcasting
            else:
                self.sock.sendall('{}: {} '.format(self.name, message).encode('ascii'))

        print('\nQuitting....')
        self.sock.close()
   


class Receive(threading.Thread):
    def __init__(self, sock, name):
        super().__init__()
        self.sock = sock
        self.name = name
        self.messages  = None




    def run(self):

        while True:
            try:
                message = self.sock.recv(1024).decode('ascii')

                if message:
                    if self.messages:
                        self.messages.insert(tk.END, message)

                    print('\r{}\n{}:'.format(message, self.name), end='')

                else:
                    print("\nConnection closed by the server.")
                    break

            except (ConnectionAbortedError, ConnectionResetError, OSError):
                print("\nConnection closed.")
                break

        try:
            self.sock.close()
        except OSError:
            pass 


class Client:
    #Management of client-sever connection and integration of GUI
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.name = None
        self.messages = None

    def start(self):
        print('Trying to connect to {}:{}...'.format(self.host, self.port))
        self.sock.connect((self.host, self.port))

        print('Successfully Connected to {}:{}'.format(self.host, self.port))

        print()

        self.name = input('Your name: ')

        print()

        print('Welcome, {}! Getting ready to send and receive messages...'.format(self.name))

        #create send and receive threads

        send= Send(self.sock, self.name)
        receive = Receive(self.sock, self.name)

        #Start send and receive thread
        send.start()
        receive.start()

        self.sock.sendall('Server: {} has joined the chat. say whatsup!'.format(self.name,).encode('ascii'))
        print("\r Ready!! Leave the chat room anytime by typing 'Quit'\n")
        print('{}: '.format(self.name),end= '')

        return receive

    def send(self, textInput):
        # Sends text input data from the GUI

        self.message = textInput.get()
        textInput.delete(0, tk.END)
        self.messages.insert(tk.END, '{}: {}'.format(self.name, self.message))

        #Type 'Quit' to leave the chatroom
        if self.message == 'Quit':
            try:
                self.sock.sendall(f"Server: {self.name} has left the chat.".encode("ascii")
        )
            except OSError:
                pass

            print("\nQuitting...")

            try:
                self.sock.shutdown(socket.SHUT_RDWR)
            except OSError:
                pass

            self.sock.close()
            return
        

        #Send message to server for broadcasting
        else:
            self.sock.sendall('{}: {}'.format(self.name, self.message).encode('ascii'))

def main(host, port):
    #initilize and run GUI App
    client = Client(host, port)
    Receive = client.start()

    window = tk.Tk()
    window.title("Chatroom")

    fromMessage = tk.Frame(master=window)
    scrollbar = tk.Scrollbar(master=fromMessage)
    messages = tk.Listbox(master=fromMessage, yscrollcommand=scrollbar.set)

    scrollbar.pack(side=tk.RIGHT, fill= tk.Y,expand = False)
    messages.pack(side=tk.LEFT, fill= tk.BOTH, expand = True)


    client.messages = messages
    Receive.messages = messages

    fromMessage.grid(row = 0, column = 0, columnspan = 2, sticky = "nsew")
    fromEntry = tk.Frame(master = window)
    textInput = tk.Entry(master=fromEntry)

    textInput.pack(fill  = tk.BOTH, expand = True)
    textInput.bind("<Return>", lambda x: client.send(textInput))
    textInput.insert(0,'Write your message hare.')

    btnSend = tk.Button(
        master=window,
        text='Send',
        command=lambda: client.send(textInput)
    )

    fromEntry.grid(row=1, column=0, padx=10, sticky = "ew")
    btnSend.grid(row=1, column=1, pady=10, sticky = "ew")

    window.rowconfigure(0, minsize=500, weight= 1)
    window.rowconfigure(1, minsize=50, weight=0)
    window.columnconfigure(0, minsize=500, weight=1)
    window.columnconfigure(1, minsize=200, weight=0)

    window.mainloop()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Chatroom Server")
    parser.add_argument('host',help='Interface the server listens at')
    parser.add_argument('-p', metavar='PORT',type=int,default=1060, help="TCP port (default 1060)")

    args = parser.parse_args()

    main(args.host, args.p)
