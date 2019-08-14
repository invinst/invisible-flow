from invisible_flow.transformers.copa_scrape_transformer import CopaScrapeTransformer


class TestCopaScrapeTransformer:
    def test_split_passes(self):
        self.copa = False
        self.no_copa = False
        transformer = CopaScrapeTransformer()
        raw_data = transformer.split()
        for row in raw_data['copa']:
            if row['assignment'] != 'COPA':
                self.copa = True

        for row in raw_data['no_copa']:
            if row['assignment'] == 'COPA':
                self.no_copa = True

        assert not self.copa
        assert not self.no_copa

    def test_split_fails(self):
        self.copa = False
        self.no_copa = False
        transformer = CopaScrapeTransformer()
        raw_data = transformer.split()
        raw_data['copa'].append({'assignment': 'MOOOOOOOOOO'})
        raw_data['no_copa'].append({'assignment': 'COPA'})
        for row in raw_data['copa']:
            if row['assignment'] != 'COPA':
                self.copa = True

        for row in raw_data['no_copa']:
            if row['assignment'] == 'COPA':
                self.no_copa = True

        assert self.copa
        assert self.no_copa
