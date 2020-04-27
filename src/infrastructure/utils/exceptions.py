from flask import Response, json
from marshmallow import ValidationError


class ApiException(Exception):
    message: str
    code: str
    status: int
    meta: dict

    def __init__(self, message: str, code: str, status: int = 500, meta=None):
        super().__init__(self)
        if meta is None:
            meta = dict({})
        self.message = message
        self.code = code
        self.status = status
        self.meta = meta


class BadRequest(ApiException):
    def __init__(self, message: str):
        ApiException.__init__(self, message, "BAD_REQUEST", 400)


class NotFound(ApiException):
    def __init__(self, message: str, meta: dict):
        ApiException.__init__(
            self,
            message,
            "NOT_FOUND",
            404,
            meta,
        )


class UnprocessableEntity(ApiException):
    def __init__(self, message: str, meta: dict = ()):
        ApiException.__init__(self, message, "UNPROCESSABLE_ENTITY", 422, meta)


class Unauthorised(ApiException):
    def __init__(self, message: str = "Unauthorised"):
        ApiException.__init__(self, message, "UNAUTHORISED", 401)


class Forbidden(ApiException):
    def __init__(self, message: str = "Forbidden"):
        ApiException.__init__(self, message, "FORBIDDEN", 403)


class RequestValidationError(ApiException):
    def __init__(self, message: str):
        ApiException.__init__(self, message, "REQUEST_VALIDATION_ERROR", 400)


class UnauthorisedError(ApiException):
    def __init__(self, message: str = "Unauthorised"):
        ApiException.__init__(self, message, "UNAUTHORISED_ERROR", 401)


class InternalServerError(ApiException):
    def __init__(self, message: str = "Internal Server Error"):
        ApiException.__init__(self, message, "INTERNAL_SERVER_ERROR")


def error_handler(error):
    if isinstance(error, ApiException):
        return build_response(error)
    elif isinstance(error, ValidationError):
        validation_error = RequestValidationError(error.messages)
        return build_response(validation_error)
    else:
        print(error)
        message = getattr(error, "description", None) or getattr(error, "message", None) or getattr(error, "name", None)
        message = "Internal Server Error" if message is None else message
        internal_server_error = InternalServerError(message)

        return build_response(internal_server_error)


def build_response(error: ApiException) -> Response:
    response_body = dict(message=error.message, code=error.code, meta=error.meta)
    return Response(response=json.dumps(response_body), status=error.status, mimetype="application/json;charset=utf8")
