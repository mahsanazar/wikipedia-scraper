
from src.scraper import WikipediaScraper # import class
# Create an instance of the WikipediaScraper
Myscraper= WikipediaScraper()
# Get the list of supported countries
Myscraper.get_countries()
Myscraper.get_leaders()
Myscraper.get_first_paragraph()
Myscraper.to_json_file('leaders_data')