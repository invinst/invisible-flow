from flask import Flask


class AppFactory:
    _instance = None
    _celery = None

    @staticmethod
    def create_app():
        if AppFactory._instance is None:
            AppFactory._instance = Flask(__name__,
                                         static_folder="../frontend/build/static",
                                         template_folder="../frontend/build")

            AppFactory._celery = AppFactory._instance

        return AppFactory._instance


from celery import Celery


def make_celery(app):
    celery = Celery(
        app.import_name,
        # move this to a celery config
        backend=app.config['CELERY_RESULT_BACKEND'],
        broker=app.config['CELERY_BROKER_URL']
    )
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            print("calling with app context")
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery

app = AppFactory.create_app()
