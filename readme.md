#  Invisible Flow 

This project aids in the process of data entry and tracking for the Citizens Police Data Project (CPDP), an initiative of the Invisible Institute. The [CPDP](https://cpdp.co/) is an interactive data tool for holding police accountable to the public they serve.
  
This tool cleans and stores data that is scraped from the Civilian Office of Police Accountability ([COPA](https://www.chicagocopa.org/about-copa/mission-history/)) API, which houses all allegations against the Chicago Police Department.


## Local environment setup
To set up this project on your local machine, please follow the rest of this document step by step.

### Install docker
##### Mac or Windows
[Download Docker here](https://www.docker.com/products/docker). 

**[ Note ]** Docker for Windows only supports Windows 10. If you have an earlier version of Windows you'll need to install  [docker toolbox](https://docs.docker.com/toolbox/toolbox_install_windows/)  instead.
##### Linux
On Linux, run  `apt-get install docker`. 

### Install PyCharm
We recommend using PyCharm for your IDE. 
[Download PyCharm](https://www.jetbrains.com/pycharm/download/#section=mac).

### Frontend Setup
Once you've cloned the repository, run the following from your local project folder:
  

      cd frontend
      npm install
  

Let **npm** do its thing. Once complete run:

      npm run build

To make sure that the frontend built successfully, check the `frontend` directory for a new folder named `build` and note that it also updates the `node_modules` folder.

### Add `dump.sql` to your root directory
The presence of the `dump.sql` file in our project ensures that all contributors have the same schema imported into their database when building the app with docker. 

 1. Download the .sql file from this [Dropbox link](https://www.dropbox.com/s/riixbrze6apmcrn/cpdp-apr-5-2019.sql?dl=0).

 2. Rename the file `dump.sql` 
 3. Add the file to your local project's root directory.

****[ Important! ]**** Before moving on, make sure that you've followed the instructions up until this point.

### Build app with docker

**[ Stop ]** If you haven't already added `dump.sql` to your root directory and set up your frontend, do so now by following instructions above.

Once the above steps are complete, return to your project's root directory `invisible-flow` and run in your terminal:

    docker build -t invisible_flow:latest .

### Run app locally with docker
This project outputs `.csv` files. In order to set this up: 

 1. Decide where you would like to store these files (it can be anywhere you choose). 
 2. Copy the absolute file path to this directory from your home directory (i.e, `~/Downloads`).
 3. Replace "$(pwd)" with the file path.

The command to **run the app locally** is:

    docker run -t -i -p5000:5000 -e PORT=5000 -v "$(pwd):/app/" invisible_flow:latest


#### Check if the app is running correctly
 1. When the app is running locally, open `http://0.0.0.0:5000/` in a browser to view.
 2. Click **Initiate Scrape**. This should update the database with data from COPA and may take a few minutes to complete.
 3. After the scape finishes, check that the `invisible_flow_testing` database in the docker container was updated by doing the following:


        docker ps
    
   Copy the `CONTAINER ID` from the output of that command (i.e., `274ff13bc055`) and run:
    
	    docker exec -it <INSERT_CONTAINER_ID> bash
	
Something like this will show up in your terminal: 

	    postgres@274ff13bc055:/app$

From there you can access the database running inside of the current docker container by entering: 
	 
		 psql invisible_flow_testing

Try querying:
		
		SELECT * FROM data_officerallegation;
If you see a populated table, you should be all set up!


### Tests 
##### Running Backend Tests:  
Backend tests should be run while the app is running locally. Open up a new terminal window and execute:

    docker ps
    
Copy the `CONTAINER ID` from the output of that command (i.e., `274ff13bc055`) and run:
    
	docker exec -it <INSERT_CONTAINER_ID> bash
	
Something like this will show up in your terminal:

    postgres@274ff13bc055:/app$  

You can then run: 

    pytest tests    
  
To run the tests with a certain test focused, mark the focused test with `@pytest.mark.focus`

##### Running Frontend Tests:  
* To run the tests execute `npm run test`

### Help

 If you need help with anything, feel free to contact a team member.