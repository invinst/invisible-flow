Goal: 
To be able to update a running database of police complaints managed by the Invisible Institute, based on the prior work at [the original repo](https://github.com/invinst/chicago-police-data)

If you want to get started, feel free to pick up a story at the top of [the Rearchitecting Data Pipeline Project](https://github.com/invinst/invisible-flow/projects/1) or any story directly underneath a __ that doesn't already have someone assigned to it.

The stories are organized from top to bottom as dependencies. That is, if you see story A above story B, then story B depends on story A. When you see a __ mark that starts a new set of stories that are self contained.
Further, any story tagged "can be done in parallel" can also be done out of order. 

If you don't see anything to do but still want to do something, feel free to pick one of the later stories and use stubs to interact with dependencies.

Most of the background you need to complete these stories will be in the "definitions" card, but if you find yourself in need of more information here are some important links: 
* [Important links](https://docs.google.com/document/d/1fGi61CmjcWeY6xFlV0qHKrPLH4AqJkDkd70YWtOaQIg/edit?usp=sharing) including an overview of the current data pipeline
* [Onboarding notes](https://docs.google.com/document/d/1QIxJwsO7xY1-SbfmNyFxXGcDqBtex4QeeDGfRtrTMHA/edit?usp=sharing)

Setup:
1. Download [Conda](https://docs.conda.io/projects/conda/en/latest/) as miniconda (Conda + virtual environment) or as Anaconda (Conda + virtual environment + a ton of packages)
1. Run `conda env create -f environment.yml`

To activate the environment, run `conda activiate invisible-flow-env`
