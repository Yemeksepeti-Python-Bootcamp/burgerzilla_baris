
class Responses:
    """
    This class is used to create a response 
    object that will be returned to the client.
    """
    def createResponse(self):
        response = {}
        return response
    

    def success_response(self, status, message):
        response = self.createResponse()
        response["status"] = status
        response["message"] = message

        return response

    def error_response(self, status, message):
        response = self.createResponse()
        response["status"] = status
        response["message"] = message

        return response