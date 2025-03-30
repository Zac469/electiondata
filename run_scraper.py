from scrapers.aus_2025 import Aus2025Scraper
from scrapers.aus_2022 import Aus2022Scraper

def main():
    year = input("Enter election year (2025, 2022): ").strip()

    if year == "2025":
        scraper = Aus2025Scraper()
    elif year == "2022":
        scraper = Aus2022Scraper()
    else:
        print("Election year not supported.")
        return

    data = scraper.extract_tables()
    for i, df in enumerate(data):
        print(f"\nPolling Table {i}:")
        print(df.head())

if __name__ == "__main__":
    main()