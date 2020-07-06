Copa jobs
Frontend expects:
- Backend should have the following endpoints:
  - /job_status/{jobID} endpoint that returns the status of a job as a JSON object with a "status" field,
   where status is any string
     - When a job is completed, status is expected to have the value `COMPLETED`
  - /start_copa_job endpoint that returns a job id for a copa job that is in progress as a json object with a "job_id" field,
    where job_id is any integer greater than 0.
  
