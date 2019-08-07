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

### Running the tests
* To run the tests execute `pytest tests`
* arguments
  * m [argument] - run tests with [argument] mark
     * To run the tests with a certain test focused, mark the focused test with `@pytest.mark.focus`
     * This uses the [pytest mark system](https://docs.pytest.org/en/latest/mark.html)
