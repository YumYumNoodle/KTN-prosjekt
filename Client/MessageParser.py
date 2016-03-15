
import json
class MessageParser():
    # TODO: Finish this class
    def __init__(self):

        self.possible_responses = {
            'error': self.parse_error,
            'info': self.parse_info,
            'message': self.parse_message,
            'history': self.parse_history
        }

    def parse(self, payload):


        payload = json.loads(payload)# decode the JSON object
        if payload['response'] in self.possible_responses:
            print (self.possible_responses[payload['response']](payload))
        else:
            return("Error in JSONobject recieved from server")

    def parse_error(self, payload):
        return "error: " + payload['content']
    def parse_info(self, payload):
        return "info: " + payload['content']

    def parse_message(self, payload):
        username = "unknown"
        try:
            username = payload["sender"]
        finally:
            return username+ ": "  + payload['content']

    def parse_history(self, payload):
        history_message = ""
        history_dict = payload['content']


        for i in range(1, len(history_dict)+1):
            dict = history_dict[unicode(i)]
            history_message+= dict[unicode('sender')]+": " + dict[unicode('content')]  + "\n"
        return history_message
def test():
    m = MessageParser()

    #data = {'timestamp': "10:20", 'response': 'message', 'sender': 'hege', 'content': 'hei'}
    data = {'timestamp': "10:20", 'response': 'history', 'sender': 'hege', 'content': {1: {'timestamp': "10:20", 'response': 'message', 'sender': 'hege', 'content': 'hei'}, 2:{'timestamp': "10:20", 'response': 'message', 'sender': 'max', 'content': 'hei'}, 3: {'timestamp': "10:20", 'response': 'message', 'sender': 'nora', 'content': 'hei'}}}
    payload = json.dumps(data) #json object
    m.parse(payload)
    #json_decode = json.loads(json_encoded) #python dict


test()

