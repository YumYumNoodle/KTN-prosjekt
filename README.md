# TTM4100: Communication – Services and Networks: Chat service

##Introduction

In this project you will create a chat service, consisting of both a chat server and a chat client. The client will communicate with the server over a TCP connection.
The main purpose of this project is to implement a protocol, so basically, we don’t require any certain programming language. A protocol is by definition a design that enables different systems, languages or endpoints communication with each other using a common, shared language.
However, since the curriculum (and textbook) is based on Python (Python 2.7), and the language is used throughout the course, the provided skeleton code is also written in Python 2.7. It is also very likely that the course staff will be able to provide the best help and assistance if you implement the project using Python 2.7.
The goal of this project is to have a practical and useful approach to network programming and modern concepts of programming with the use of application programming interfaces (API). Previously, the course has emphasized the importance of technical aspects of lower-level network programming. In the recent years, however, very good open source libraries have emerged, and we can focus on the fun parts of network programming.

##Requirements

You will implement a simple protocol for a command line interface chat client that communicates with a server backend. The client is supposed to be a “stupid” client and the logic will for the most part be placed server side. The communication between the server and clients will be using JSON as the format of the communicated information. JSON has become the standard in modern web applications through its heavy use within API’s.
The client is supposed to handle input from the user (through the keyboard), parse the input and send the payload to the server. The format of the payload is fixed (see next section). The server will, in turn, handle the received payload and take the required actions. The server must be able to handle several clients. After the server has performed the corresponding actions, it must send a response back to the client. Again, the format of these responses is fixed and detailed in the next section.
The goal is for you to implement a generic protocol. To test that, your client must communicate with other people’s servers, and other students’ clients must be able to communicate with your server. During the demonstration of the final program, the student assistants will test your code with their own implementation of both the server and client. If your code does not work against our implementation, the solution will not be accepted.
