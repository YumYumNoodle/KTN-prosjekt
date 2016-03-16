# -*- coding: utf-8 -*-
import SocketServer
import json
import datetime
import time
"""
Variables and functions that must be used by all the ClientHandler objects
must be written here (e.g. a dictionary for connected clients)
"""

connected_users = {}
history = {}

def broadcast_to_all(sender, response, message):
    for user in connected_users.values():
        user.send_response(sender, response, message)
    if response == "message":
        history[len(history)] = {"timestamp": str(datetime.datetime.now().strftime("%H:%M:%S %d-%m-%y")),
                                 "sender": sender,"response": response, "content": message}


class ClientHandler(SocketServer.BaseRequestHandler):
    """
    This is the ClientHandler class. Everytime a new client connects to the
    server, a new ClientHandler object will be created. This class represents
    only connected clients, and not the server itself. If you want to write
    logic for the server, you must write it outside this class
    """
    def __init__(self, request, client_address, serv):
        self.ip = None
        self.port = None
        self.connection = None
        self.is_logged_in = False
        self.username = ""

        self.possible_requests = {
            'login': self.login,
            'logout': self.logout,
            'msg': self.msg,
            'names': self.get_names,
            'help': self.get_help
        }

        SocketServer.BaseRequestHandler.__init__(self, request, client_address, serv)

    def handle(self):
        """
        This method handles the connection between a client and the server.
        """
        self.ip = self.client_address[0]
        self.port = self.client_address[1]
        self.connection = self.request

        print('Client connected at ' + str(self.ip) + ':' + str(self.port))

        # Sends a response that the client is connected (only for test)

        self.send_response("Server", "info", "Connection successfully established.")

        # Loop that listens for messages from the client
        while True:
            received_string = self.connection.recv(4096)
            if received_string:
                payload = json.loads(received_string)

                if payload['request'] in self.possible_requests:
                    self.possible_requests[payload['request']](payload['content'])
                else:
                    self.send_response("Server", "error", "Invalid request. Use 'help' "
                                                          "commmand for list of avaliable requests.")
            else:
                print 'Client disconnected at ' + str(self.ip) + ':' + str(self.port)
                break
            # TODO: Add handling of received payload from client

    def login(self, arg):

        if self.is_logged_in:
            self.send_response("Server", "error", "You are allready logged in.")
        elif arg == '':
            self.send_response("Server", "error", "Username can not be empty.")
        elif arg in connected_users:
            self.send_response("Server", "error", "Username taken.")
        else:
            self.is_logged_in = True
            self.username = arg
            connected_users[arg] = self
            self.get_history()
            broadcast_to_all("Server", "info", arg + " logged in.")  # Broadcast to all
            print('Client ' + str(self.ip) + ':' + str(self.port) + " logged in as: " + self.username)

    def logout(self, arg):
        if self.is_logged_in and self.username in connected_users:
            broadcast_to_all("Server", "info", self.username + " logged out.")
            del connected_users[self.username]
            self.is_logged_in = False
            print('Client ' + str(self.ip) + ':' + str(self.port) + " logged out as: " + self.username)
            self.username = ""

        else:
            self.send_response("Server", "error", "Logout failed. You are not logged in.")

    def msg(self, arg):
        # TODO: Uses broadcast_to_all to send a message, remember to update the history variable
        if not self.is_logged_in:
            self.send_response("Server", "error", "Unauthorized! To login write: login [your username]")
        else:
            broadcast_to_all(self.username, "message", arg)

    def get_history(self):
        if len(history) > 0:
            self.send_response("Server", "history", history)

    def get_names(self, arg):
        if not self.is_logged_in:
            self.send_response("Server", "error", "Unauthorized! To login write: login [your username]")
        else:
            users = ""
            for user in connected_users.keys():
                users += user + "\n"

            users = users[:-1]  # Remove the last newline
            self.send_response("Server", "info", "Connected users:\n"+users)

    def get_help(self, arg):
        self.send_response("Server", "info", "Commands:\n\nlogin [username]\t\tLog in your user\nlogout\t\t\t\t\tLog "
                                             "out your user\nmsg [message]\t\t\tSend a message to all connected "
                                             "users\nnames\t\t\t\t\tGet all connected usernames\nhelp\t\t\t\t\tList of "
                                             "avaliable commands")

    def send_response(self, sender, response, content):
        payload = {"timestamp": str(datetime.datetime.now().strftime("%H:%M:%S %d-%m-%y")), "sender": sender,
                   "response": response, "content": content}
        self.connection.send(json.dumps(payload))


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
