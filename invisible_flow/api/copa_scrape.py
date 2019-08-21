import requests

from invisible_flow.constants import SCRAPE_URL


class CopaScrape:
    def scrape_data(self):
        url = SCRAPE_URL
        resp = requests.get(url=url)
        return resp.json()

    def scrape_copa_csv(self):
        query_string = ".csv?$where=assignment=\"COPA\""
        url = SCRAPE_URL + query_string
        return requests.get(url=url).content

    def scrape_not_copa_csv(self):
        query_string = ".csv?$where=assignment!=\"COPA\""
        url = SCRAPE_URL + query_string
        return requests.get(url=url).content

    def scrape_copa_ready_for_entity(self):
        query_string = ".csv?$select=log_no,complaint_date,beat&$where=assignment!=\"COPA\""
        url = SCRAPE_URL + query_string
        return requests.get(url=url).content

    def scrape_copa_not_in_entity(self):
        query_string = ".csv?$select=log_no,assignment,case_type,current_status,current_category," \
                       "finding_code,police_shooting,race_of_complainants,sex_of_complainants,age_of_complainants," \
                       "race_of_involved_officers,sex_of_involved_officers,age_of_involved_officers," \
                       "years_on_force_of_officers,complaint_hour,complaint_day,complaint_month&" \
                       "$where=assignment!=\"COPA\""
        url = SCRAPE_URL + query_string
        return requests.get(url=url).content
