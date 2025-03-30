import requests
import pandas as pd
from bs4 import BeautifulSoup
import re
from datetime import datetime

class BaseScraper:
    def __init__(self, url):
        self.url = url
        self.soup = None

    def fetch_page(self):
        """Fetches the webpage and creates a BeautifulSoup object."""
        response = requests.get(self.url)
        response.raise_for_status()
        self.soup = BeautifulSoup(response.text, "html.parser")

    def clean_text(self, text):
        """Removes footnotes and extra spaces from text."""
        return re.sub(r"\[.*?\]", "", str(text)).strip()

    def parse_date_range(self, date_str):
        """Extracts start and end dates from date strings."""
        date_str = date_str.replace("–", "-").replace("—", "-")
        date_parts = date_str.split("-")

        try:
            if len(date_parts) == 2:
                year = date_parts[1].strip()[-4:]
                if any(char.isalpha() for char in date_parts[0]):
                    start_date = datetime.strptime(date_parts[0].strip() + " " + year, "%d %b %Y").strftime("%Y-%m-%d")
                else:
                    month_year = " ".join(date_parts[1].strip().split()[-2:])
                    start_date = datetime.strptime(date_parts[0].strip() + " " + month_year, "%d %b %Y").strftime("%Y-%m-%d")
                end_date = datetime.strptime(date_parts[1].strip(), "%d %b %Y").strftime("%Y-%m-%d")
            else:
                start_date = end_date = datetime.strptime(date_str.strip(), "%d %b %Y").strftime("%Y-%m-%d")
            return start_date, end_date
        except ValueError:
            return None, None

    def extract_tables(self):
        """Extracts all tables and converts them to Pandas DataFrames."""
        raise NotImplementedError("This method should be implemented in a subclass.")