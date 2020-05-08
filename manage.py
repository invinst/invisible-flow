import os
import tempfile
from typing import Optional

from flask import Flask
from flask_sqlalchemy import SQLAlchemy  # type:ignore

from invisible_flow.app_factory import app
from invisible_flow.constants import JOB_DB_BIND_KEY, COPA_DB_BIND_KEY

from flask_migrate import Migrate

job_db_file = tempfile.NamedTemporaryFile(suffix='.db')
job_db_filename = f'sqlite:///{job_db_file.name}'


"""


The following section should write the env variable to fs.
use os.environ.get('MY_ENVIRONMENT_VARIABLE') to set some stuff based on env.
use some sort of file system writer to write a file to this directory.


"""


if os.environ.get('ENVIRONMENT') == 'heroku':
    credentials_file = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
    credentials_content = os.environ.get("GOOGLE_CREDENTIALS")

    with open("/app/invisible_flow/{credentials_file}".format(credentials_file=credentials_file), "w") as writer:
        writer.write("{credentials_content}".format(credentials_content=credentials_content))


copa_db_filename: Optional[str] = ''
if os.environ.get("ENVIRONMENT") == 'local' or os.environ.get('ENVIRONMENT') == 'travis':
    copa_db_filename = 'postgres+psycopg2://invisible_flow@localhost:5432/invisible_flow_testing'
elif os.environ.get("ENVIRONMENT") == 'docker':
    copa_db_filename = 'postgres+psycopg2://invisible_flow_testing@localhost:5432/invisible_flow_testing'
elif os.environ.get("ENVIRONMENT") == 'development':
    copa_db_filename = 'postgres+psycopg2://invisible_flow_testing@localhost:5432/invisible_flow_testing'
elif os.environ.get('ENVIRONMENT') == 'heroku':
    heroku_db_url = str(os.environ.get('DATABASE_URL'))
    split_heroku_db_url = heroku_db_url.split(':', 1)
    copa_db_filename = split_heroku_db_url[0] + '+psycopg2:' + split_heroku_db_url[1]
else:
    raise Exception('Unable to determine environment when setting database URL')


def setup_db(_app: Flask) -> SQLAlchemy:
    db_config = {
        'SQLALCHEMY_BINDS': {
            JOB_DB_BIND_KEY: job_db_filename,
            COPA_DB_BIND_KEY: copa_db_filename
        },
        'SQLALCHEMY_DATABASE_URI': copa_db_filename,
        'SQLALCHEMY_TRACK_MODIFICATIONS': False
    }

    _app.config.update(db_config)

    return SQLAlchemy(_app)


db = setup_db(app)

migrate = Migrate(app, db)
