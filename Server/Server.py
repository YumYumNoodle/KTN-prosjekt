# -*- coding: utf-8 -*-
import SocketServer
import json
"""
Variables and functions that must be used by all the ClientHandler objects
must be written here (e.g. a dictionary for connected clients)
"""


class ClientHandler(SocketServer.BaseRequestHandler):
    """
    This is the ClientHandler class. Everytime a new client connects to the
    server, a new ClientHandler object will be created. This class represents
    only connected clients, and not the server itself. If you want to write
    logic for the server, you must write it outside this class
    """

    def handle(self):
        """
        This method handles the connection between a client and the server.
        """
        possible_responses = {
            'login': self.login,
            'logout': self.logout,
            'msg': self.send_message,
            'names': self.get_names,
            'help': self.get_help
        }

        ip = self.client_address[0]
        port = self.client_address[1]
        connection = self.request

        print('Client connected at ' + str(ip) + ':' + str(port))

        # Sends a response that the client is connected (only for test)

        connection.send("Successfully established a connection to the server.")

        # Loop that listens for messages from the client
        while True:
            received_string = connection.recv(4096)
            if received_string:
                print received_string
            else:
                print 'Client disconnected at ' + str(ip) + ':' + str(port)
                break
            # TODO: Add handling of received payload from client

    def login(self):
        # TODO
        pass

    def logout(self):
        # TODO
        pass

    def send_message(self):
        # TODO
        pass

    def get_names(self):
        # TODO
        pass

    def get_help(self):
        # TODO
        pass


class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    """
    This class is present so that each client connected will be ran as a own
    thread. In that way, all clients will be served by the server.

    No alterations are necessary
    """
    allow_reuse_address = True

if __name__ == "__main__":
    """
    This is the main method and is executed when you type "python Server.py"
    in your terminal.

    No alterations are necessary
    """

    HOST, PORT = 'localhost', 9998

    # Allow restart of the server
    ThreadedTCPServer.allow_reuse_address = True

    server = ThreadedTCPServer((HOST, PORT), ClientHandler)

    # Set up and initiate the TCP server

    print "Serving forever at port "+str(PORT)
    try:
        server.serve_forever()
    except:
        print("Closing the server.")
        server.server_close()
        raise
