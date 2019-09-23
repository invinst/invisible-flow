import tempfile

from flask import Flask
from flask_sqlalchemy import SQLAlchemy  # type:ignore

from invisible_flow.app_factory import app
from invisible_flow.constants import JOB_DB_BIND_KEY, COPA_DB_BIND_KEY

job_db_file = tempfile.NamedTemporaryFile(suffix='.db')
job_db_filename = f'sqlite:///{job_db_file.name}'

copa_db_file = tempfile.NamedTemporaryFile(suffix='.db')
copa_db_filename = f'sqlite:///{copa_db_file.name}'


def setup_db(_app: Flask) -> SQLAlchemy:
    db_config = {
        'SQLALCHEMY_BINDS': {
            JOB_DB_BIND_KEY: job_db_filename,
            COPA_DB_BIND_KEY: copa_db_filename
        },
        # 'SQLALCHEMY_DATABASE_URI':        <-- WAS IST DASS ADEOLU?
    }

    _app.config.update(db_config)

    return SQLAlchemy(_app)


db = setup_db(app)
