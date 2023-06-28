import logging

from fastapi import HTTPException, status


class GenericError(HTTPException):
    def __init__(self, error) -> None:
        msg = "Unexpected Error"
        error_msg = f"{msg} - {error}"
        logging.error(error_msg)
        status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR
        detail: str = msg
        super().__init__(status_code, detail)
