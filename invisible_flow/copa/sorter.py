from invisible_flow.copa.existing_crid import ExistingCrid
from sqlalchemy.orm.exc import NoResultFound


class Sorter:
    def __init__(self):
        self.old_crids = []
        self.new_crids = []

    # sorter queries existing_crid table
    def query_existing_crid_table(self):
        try:
            existing_crids = ExistingCrid.query.one().existing_crids
        except NoResultFound:
            existing_crids = ''
        return existing_crids

    # sorter sorts scraped_crids into old and new crids
    def parse_existing_crids(self, scrape_results: list):
        # call query_existing_crids
        return

    # sorter saves new crids to existing_crid table
