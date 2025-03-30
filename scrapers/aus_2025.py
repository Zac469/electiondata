from scrapers.base_scraper import BaseScraper
import pandas as pd

class Aus2025Scraper(BaseScraper):
    def __init__(self):
        super().__init__("https://en.wikipedia.org/wiki/Opinion_polling_for_the_2025_Australian_federal_election")

    def extract_tables(self):
        """Extracts polling tables for the 2025 election."""
        self.fetch_page()
        
        headers = self.soup.find_all(["h2", "h3", "h4"])
        polling_tables = []
        found_top = False

        top_headers = ["Voting Intention", "National Polling"]
        bottom_headers = ["Preferred Prime Minister", "Leadership Polling"]

        for header in headers:
            header_text = self.clean_text(header.get_text(strip=True)).lower()
            if any(top.lower() in header_text for top in top_headers):
                found_top = True
                continue
            if found_top and any(bottom.lower() in header_text for bottom in bottom_headers):
                break  
            if found_top:
                table = header.find_next("table", class_="wikitable")
                if table:
                    polling_tables.append(table)

        all_dataframes = [pd.read_html(str(table))[0] for table in polling_tables]

        # Clean column headers and remove footnotes
        for i, df in enumerate(all_dataframes):
            df.columns = [self.clean_text(col) for col in df.columns]
            all_dataframes[i] = df.applymap(self.clean_text)

        return all_dataframes