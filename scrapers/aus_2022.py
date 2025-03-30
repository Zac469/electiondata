from scrapers.base_scraper import BaseScraper
import pandas as pd

class Aus2022Scraper(BaseScraper):
    def __init__(self):
        super().__init__("https://en.wikipedia.org/wiki/Opinion_polling_for_the_2022_Australian_federal_election")

    def extract_tables(self):
        self.fetch_page()
        tables = self.soup.find_all("table", class_="wikitable")
        return [pd.read_html(str(table))[0] for table in tables]