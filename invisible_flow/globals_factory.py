from datetime import datetime

from flask import Request, request


class GlobalsFactory:

    @staticmethod
    def get_request_context() -> Request:
        return request

    @staticmethod
    def get_current_datetime_utc() -> datetime:
        return datetime.utcnow()
