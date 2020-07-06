from invisible_flow.app import copa_scrape

job_ids = {}
counter = 0

def start_copa_job():
    counter = counter + 1

    copa_scrape()
