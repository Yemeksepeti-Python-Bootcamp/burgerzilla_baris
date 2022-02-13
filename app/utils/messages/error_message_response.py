from app.utils.helpers.string_helper import StringHelper


class ErrorMessages:
    def message(self, status, message):
        return {
            "status": status,
            "message": message
        }

    def validation_error(self, status, errors):
        response_object = {"status": status, "errors": errors}
        return response_object


    def err_resp(self, msg, reason, code):
        err = self.message(False, msg)
        err["error_reason"] = reason
        return err, code


    def internal_err_resp(self):
        err = self.message(False, StringHelper.INTERNAL_SERVER_ERROR)
        err["errors_reason"] = StringHelper.SERVER_ERROR
        return err,500