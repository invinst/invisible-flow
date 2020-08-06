import requests
import os

from invisible_flow.constants import SCRAPE_URL, ALLEGATION_BASE_URL, OFFICER_BASE_URL


def scrape_data():
    base_query = ".csv?$query=SELECT%20log_no,beat,race_of_involved_officers,sex_of_involved_officers,"\
                       + "age_of_involved_officers,years_on_force_of_officers"
    url = generate_url(SCRAPE_URL, base_query)

    response = requests.get(url=url)
    if response.status_code == 200:
        return response.content
    else:
        raise ConnectionError(response.content)


def scrape_allegation_data():
    allegation_query = "query=SELECT%20log_no,beat"
    url = generate_url(ALLEGATION_BASE_URL, allegation_query)

    response = requests.get(url=url)
    if response.status_code == 200:
        return response.content
    else:
        raise ConnectionError(response.content)


def scrape_officer_data():
    officer_query = "query=SELECT%20log_no,complaint_date,finding_code,current_status,age_of_involved_officer,\
            sex_of_involved_officer,race_of_involved_officer,years_on_force_of_involved_officer"
    url = generate_url(OFFICER_BASE_URL, officer_query)

    response = requests.get(url=url)
    if response.status_code == 200:
        return response.content
    else:
        raise ConnectionError(response.content)


def scrape_crids():
    crid_query = "query=SELECT%20log_no"
    url = generate_url(ALLEGATION_BASE_URL, crid_query)

    response = requests.get(url=url)
    if response.status_code == 200:
        return response.content
    else:
        raise ConnectionError(response.content)


def get_num_rows(num_rows_query_url):
    response = requests.get(url=num_rows_query_url)
    if response.status_code == 200:
        num_rows_csv = response.content
        num_rows = num_rows_csv.decode('utf-8').split('\n')[1]
        return num_rows
    else:
        raise ConnectionError(response.content)

def generate_url(base_url, query):
    if os.environ.get("ENVIRONMENT") == 'local' or os.environ.get('ENVIRONMENT') == 'travis': # or os.environ.get('ENVIRONMENT') == 'docker':
        if base_url == SCRAPE_URL:
            num_rows = get_num_rows(SCRAPE_URL + ".csv?$query=SELECT%20count(log_no)").replace("\"", "")
        else:
            num_rows = get_num_rows(base_url + "query=SELECT%20count(log_no)").replace("\"", "")
        url = base_url + query + "%20LIMIT%20" + num_rows
    else:
        url = base_url + query
    return url
