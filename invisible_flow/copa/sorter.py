class Sorter:
    def __init__(self):
        self.old_crids = []
        self.new_crids = []

    def split_crids_into_new_and_old(self, scrape_results: list, existing_crids_string: str):
        existing_crids = set(existing_crids_string.split(','))
        scraped_results = set(scrape_results)
        self.new_crids = scraped_results - existing_crids
        self.old_crids = scraped_results.intersection(existing_crids)

    def get_new_crids(self):
        return self.new_crids

    def get_old_crids(self):
        return self.old_crids

    def get_new_copa_rows(self, scraped_data):
        new_rows = scraped_data[scraped_data['log_no'].isin(self.new_crids)]
        return new_rows