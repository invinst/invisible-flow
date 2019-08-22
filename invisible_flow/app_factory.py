from flask import Flask


class AppFactory:
    _instance = None

    @staticmethod
    def create_app():
        if AppFactory._instance is None:
            AppFactory._instance = Flask(__name__)

        return AppFactory._instance


app = AppFactory.create_app()
