# Wikipedia Scraper

The Wikipedia Scraper is a Python script that scrapes leader data from the Country Leaders API and extracts details about each leader from their Wikipedia page.

## Installation

## Cloning with GitHub and opening in Visual Studio Code

1. Open your web browser and navigate to the GitHub repository: https://github.com/mahsanazar/wikipedia-scraper

2. Click on the "Code" button and then click on the clipboard icon to copy the repository URL.

3. Open Visual Studio Code.

4. In Visual Studio Code, open the Command Palette by pressing `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (Mac) and type "Git: Clone" and press `Enter`.

5. Paste the copied repository URL and press `Enter`.

6. Choose the directory where you want to clone the repository and press `Enter`.

7. Once the repository is cloned, navigate to the project directory

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


