# -*- coding: utf-8 -*-
import socket
import time
import json
from MessageReceiver import MessageReceiver
from MessageParser import MessageParser
from threading import Thread

class Client:
    """
    This is the chat client class
    """

    def __init__(self, host, server_port):
        """
        This method is run when creating a new Client object
        """
        self.host = host
        self.server_port = server_port
        # Set up the socket connection to the server
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        self.run()

    def run(self):
        # Initiate the connection to the server
        print 'Connecting to the server..'
        self.connection.connect((self.host, self.server_port))

        # Initialize a message reciver
        reciver = MessageReceiver(self, self.connection)
        reciver.start()

        # Wait a second for server response
        time.sleep(1)
        cin = str(raw_input())

        while cin != "exit":
            temp_dict = cin.partition(' ')
            payload = {"request": temp_dict[0], "content": temp_dict[2]}
            self.send_payload(json.dumps(payload))
            cin = str(raw_input())

        self.disconnect()

    def disconnect(self):
        self.connection.close()

    def receive_message(self, payload):
        # TODO: The code under is purely testing, and should be done in the message-parser class
        message = json.loads(payload)
        print("[" + message["sender"] + " at " + message["timestamp"] + "] " + message["content"])

    def send_payload(self, data):
        self.connection.send(data)
        
    # More methods may be needed!


if __name__ == '__main__':
    """
    This is the main method and is executed when you type "python Client.py"
    in your terminal.

    No alterations are necessary
    """
    client = Client('localhost', 9998)
