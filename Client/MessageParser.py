

class MessageParser():
    def __init__(self):

        self.possible_responses = {
            'error': self.parse_error,
            'info': self.parse_info,
	    # More key:values pairs are needed	
        }

    def parse(self, payload):
<<<<<<< HEAD
        payload = None # decode the JSON object
=======
        # payload = # decode the JSON object
>>>>>>> master

        if payload['response'] in self.possible_responses:
            return self.possible_responses[payload['response']](payload)
        else:
<<<<<<< HEAD
            return None
            # Response not valid

    def parse_error(self, payload):
        return None
    
    def parse_info(self, payload):
        return None
    
=======
            pass # Response not valid

    def parse_error(self, payload):
        pass
    def parse_info(self, payload):
        pass
>>>>>>> master
    # Include more methods for handling the different responses... 
