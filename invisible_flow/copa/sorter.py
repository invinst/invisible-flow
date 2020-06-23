import collections

from invisible_flow.copa.existing_crid import ExistingCrid
from sqlalchemy.orm.exc import NoResultFound
from manage import db
import pandas as pd


class Sorter:
    def __init__(self):
        self.old_crids = []
        self.new_crids = []

    def query_existing_crid_table(self):
        try:
            existing_crids = ExistingCrid.query.one().existing_crids
        except NoResultFound:
            existing_crids = ''
        return existing_crids

    def split_crids_into_new_and_old(self, scrape_results: list):
        existing_crids = set(self.query_existing_crid_table().split(','))
        scraped_results = set(scrape_results)
        self.new_crids = scraped_results - existing_crids
        self.old_crids = scraped_results.intersection(existing_crids)

    def save_new_crids_to_db(self):
        old_crids_str = ','.join(self.old_crids)
        new_crids_str = ','.join(self.new_crids)
        concatenated_crids = f"{old_crids_str},{new_crids_str}"
        existing_crid = ExistingCrid.query.one()
        existing_crid.existing_crids = concatenated_crids
        db.session.add(existing_crid)
        db.session.commit()

    def get_grouped_crids(self, scrape_results: list):
        self.split_crids_into_new_and_old(scrape_results)
        GroupedCrids = collections.namedtuple('GroupedCrids', 'new_crids existing_crids')
        grouped_crids = GroupedCrids(new_crids=self.new_crids, existing_crids=self.old_crids)
        return grouped_crids

    def get_new_allegation_rows(self, fake_scraped_data):
        new_allegation_rows = fake_scraped_data[fake_scraped_data['log_no'].isin(self.new_crids)]
        return new_allegation_rows
