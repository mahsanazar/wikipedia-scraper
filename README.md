# Wikipedia Scraper

The Wikipedia Scraper is a Python script that scrapes leader data from the Country Leaders API and extracts details about each leader from their Wikipedia page.

## Installation

1. Clone the repository:

git clone https://github.com/your-username/your-repository.git

2. Navigate to the project directory:

cd your-repository

3. Install the required dependencies:

pip install -r requirements.txt

## Usage

1. Instantiate the `WikipediaScraper` class:

Myscraper = WikipediaScraper()

2. Retrieve the list of supported countries:

Myscraper.get_countries()

3. Get the leaders for each country:

Myscraper.get_leaders()

4. Extract the first paragraph of each leader's Wikipedia page:

Myscraper.get_first_paragraph()

5. Save the leader information to a JSON file:

Myscraper.to_json_file('leaders_data.json')

## Functionality

- The `WikipediaScraper` class provides methods to fetch leader data from the Country Leaders API, including their first and last names, Wikipedia URLs, and associated countries.

- It scrapes the first paragraph of each leader's Wikipedia page to provide additional details.

- The data is then serialized and stored in a JSON file named 'leaders_data.json'.

## Dependencies

- `requests`: Used for making HTTP requests to fetch data from the Country Leaders API.
- `BeautifulSoup`: Utilized for parsing HTML content retrieved from Wikipedia pages.
- `json`: Used for serializing Python objects into JSON format.


