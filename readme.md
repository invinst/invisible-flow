Goal: 
To be able to update a running database of police complaints managed by the Invisible Institute, based on the prior work at [the original repo](https://github.com/invinst/chicago-police-data)

If you want to get started, feel free to pick up a story [the Rearchitecting Data Pipeline Project](https://github.com/invinst/invisible-flow/projects/1) 
RFP means Ready for pickup! Pick up stories that have this at the end.

The stories are organized from top to bottom as dependencies. That is, if you see story A above story B, then story B depends on story A. When you see a __ mark that starts a new set of stories that are self contained.
Further, any story tagged "can be done in parallel" can also be done out of order. 

If you don't see anything to do but still want to do something, feel free to pick one of the later stories and use stubs to interact with dependencies.

Most of the background you need to complete these stories will be in the "definitions" card, but if you find yourself in need of more information here are some important links: 
* [Important links](https://docs.google.com/document/d/1fGi61CmjcWeY6xFlV0qHKrPLH4AqJkDkd70YWtOaQIg/edit?usp=sharing) including an overview of the current data pipeline
* [Onboarding notes](https://docs.google.com/document/d/1QIxJwsO7xY1-SbfmNyFxXGcDqBtex4QeeDGfRtrTMHA/edit?usp=sharing)

Setup:
1. Download [Conda](https://docs.conda.io/projects/conda/en/latest/) as miniconda (Conda + virtual environment) or as Anaconda (Conda + virtual environment + a ton of packages)
1. Download [Docker](https://hub.docker.com/editions/community/docker-ce-desktop-mac) and ensure it's running locally. You will need to create a Docker account. 
1. Run `conda env create -f environment.yml`
1. Activate the environment by running `conda activate invisible-flow-env`
1. Import and switch project interpreter to Python 3.7 (invisible-flow) in the IDE.
1. Before you can bootstrap and run the app, you will need the /data files. Once you have these, you can run `docker-compose up`. The first time this runs, it will dump the schema and test data into your docker postgis container, which may take a few minutes. You can also run the container in the background with `docker-compose up -d`. 

You can verify that the data has been migrated successfully by connecting to the docker container and exploring the database:

```
$ docker exec -it invisible-flow_cpdb_1 bash
$ psql invisible cpdb
$ \dt # To list all tables
$ SELECT * FROM data_allegation LIMIT 10; # To show some data.  
``` 
