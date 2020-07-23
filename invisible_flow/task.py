import os
from time import sleep

from celery.utils.log import get_task_logger
from flask import Flask

from invisible_flow.app_factory import make_celery, AppFactory
from invisible_flow.jobs.jobs_mapper import JobsMapper
from manage import db

flask_app = AppFactory.create_app()
# change to celery config
if os.environ.get('ENVIRONMENT') == 'docker':
    flask_app.config.update(
        CELERY_BROKER_URL='redis://docker-redis:6379',
        CELERY_RESULT_BACKEND='redis://docker-redis:6379'
    )
elif os.environ.get('ENVIRONMENT') == 'heroku':
    flask_app.config.update(
        CELERY_BROKER_URL='redis://redistogo:ffa1fcc9f5ee69a2a7f1d130d6dc51ab@tarpon.redistogo.com:10383/',
        CELERY_RESULT_BACKEND='redis://redistogo:ffa1fcc9f5ee69a2a7f1d130d6dc51ab@tarpon.redistogo.com:10383/'
    )
else:
    print("not sure what the environment is")
celery = make_celery(flask_app)

print("I'm up!")

# @celery.task()
# def add_together(a, b):
#     logger.info('i can log!')
#     print("entered")
#     return a + b


@celery.task()
def run_copa_scrape_and_monitor_progress(job_id):
    print('Child: disposing of old database connections')
    # doing this because: https://stackoverflow.com/questions/22752521/uwsgi-flask-sqlalchemy-and-postgres-ssl-error-decryption-failed-or-bad-reco # noqa: E501
    # Solution taken from here: https://stackoverflow.com/questions/45215596/flask-and-celery-on-heroku-sqlalchemy-exc-databaseerror-psycopg2-databaseerro # noqa: E501
    # Documentation for solution is here: https://docs.sqlalchemy.org/en/13/core/connections.html#engine-disposal
    # db.session.close()
    # db.engine.dispose()
    print('Child: starting scrape')
    copa_scrape()
    print('Child: scrape finished, updating job status')
    JobsMapper.update_job(job_id, 'COMPLETED')
    print('Child: exiting')

def copa_scrape():
    sleep(5)