

class SuccessMessages:
    def message(self, status, message):
        return {
            "status": status,
            "message": message
        }

    def success_response(self, msg, code):
        scc = self.message(False, msg)
        return scc, code

