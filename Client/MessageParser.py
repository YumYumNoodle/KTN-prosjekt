import json


class MessageParser:
    # TODO: Finish this class
    def __init__(self):

        self.possible_responses = {
            'error': self.parse_error,
            'info': self.parse_info,
            'message': self.parse_message,
            'history': self.parse_history
        }

    def parse(self, payload):

        payload = json.loads(payload)  # decode the JSON object
        if payload['response'] in self.possible_responses:
            return self.possible_responses[payload['response']](payload)
        else:
            return "Error in JSONobject recieved from server"

    def parse_error(self, payload):
        return "["+payload["sender"]+" @ " + payload["timestamp"] + "] Error: " + payload["content"]

    def parse_info(self, payload):
        return "["+payload["sender"]+" @ " + payload["timestamp"] + "] " + payload["content"]

    def parse_message(self, payload):
        return "["+payload["sender"]+" @ " + payload["timestamp"] + "] " + payload["content"]

    def parse_history(self, payload):
        history_message = ""
        history_dict = payload['content']

        for i in range(0, len(history_dict)):
            response = history_dict[str(i)]
            history_message += "["+response["sender"]+" @ " + response["timestamp"] + "] " + response["content"]+"\n"

        history_message = history_message[:-1]  # Remove last newline
        return history_message



