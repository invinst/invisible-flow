[![Build Status](https://travis-ci.com/invinst/invisible-flow.svg?branch=master)](https://travis-ci.com/invinst/invisible-flow)

## Goal: To be able to update a running database of police complaints managed by the Invisible Institute, based on the prior work at [the original repo](https://github.com/invinst/chicago-police-data)

If you want to get started, feel free to pick up a story [the Rearchitecting Data Pipeline Project](https://github.com/invinst/invisible-flow/projects/1) RFP means Ready for pickup! Pick up stories that have this at the end.

The stories are organized from top to bottom as dependencies. That is, if you see story A above story B, then story B depends on story A. When you see a __ mark that starts a new set of stories that are self contained. Further, any story tagged "can be done in parallel" can also be done out of order.

If you don't see anything to do but still want to do something, feel free to pick one of the later stories and use stubs to interact with dependencies.

Most of the background you need to complete these stories will be in the "definitions" card, but if you find yourself in need of more information here are some important links:

- [Important links](https://docs.google.com/document/d/1fGi61CmjcWeY6xFlV0qHKrPLH4AqJkDkd70YWtOaQIg/edit?usp=sharing) including an overview of the current data pipeline
- [Onboarding notes](https://docs.google.com/document/d/1QIxJwsO7xY1-SbfmNyFxXGcDqBtex4QeeDGfRtrTMHA/edit?usp=sharing)

### Software Requirements:

2. Python 3.7+ 
3. An IDE (like PyCharm)

## Local environment setup:
Backend:
1. Make sure python 3 is installed
1. Activate the python virtual environment:
    1. `python3 -m venv venv`
    1. `source venv/bin/activate` 
1. `pip3 install -r requirements.txt`
1. `pre-commit install`
1. Switch project interpreter to the venv in your IDE
    - Pycharm instructions can be found [here](https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html)

You can run the app one of two ways:

1. To run it locally with flask as the [wsgi](https://flask.palletsprojects.com/en/1.1.x/deploying/)
```
$ cd invisible_flow
$ export FLASK_APP=app.py
$ export ENVIRONMENT=local
$ flask run
```
2. To run it the same way it's run on GAE, run `gunicorn -b :$PORT invisible_flow.app:app -c gunicorn.config.py`

Frontend:
1. To run it locally
```
$ cd frontend
$ npm start
```

### Running the tests
Backend:
* To run the tests execute `pytest tests`
* arguments
  * m [argument] - run tests with [argument] mark
     * To run the tests with a certain test focused, mark the focused test with `@pytest.mark.focus`
     * This uses the [pytest mark system](https://docs.pytest.org/en/latest/mark.html)

Frontend:
* To run the tests execute `npm run test`

### Google Cloud Bucket
Note: only needed for testing initiating scrape

Once onboard a team member will give download access, `json` file for testing purposes
1. rename JSON file to `googleCred.json` and place in root project directory
2. run the following commands in the root directory:
    ```
    $ export GOOGLE_APPLICATION_CREDENTIALS={your path here}/googleCred.json
    $ export GCS_BUCKET={bucket name here}
    $ export FLASK_APP=app.py
    $ export ENVIRONMENT=gae
    $ flask run
    ```
3. Navigate to *localhost:5000*

If set up properly, hitting scrape should output 'success' message in browser.

Note: JSON file has been added to the `.gitignore` as it **is not to be committed**, use naming convention as above

### Postgres Database
1. Install Postgres App and Postgres

2. Run the following commands to create DB:
    ```
   psql -c "create user invisible_flow;"
   psql -c "create database invisible_flow_testing with owner invisible_flow;"
    ```
3. Connect to invisible_flow_testing and run following command:
   ```
   CREATE EXTENSION postgis;
   ```
    Note: Sometimes after pulling most recent commits, you will need to recreate postgis extension

1. To load the beat information into the data_area table, connect to the database and run
    ```
   \copy data_area from '/path/to/project/cpdp_beats.sql';
    ```