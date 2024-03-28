# JobScrapper

JobScrapper is a Flask web application designed to scrape job listings from Wanted.co.kr based on user input keywords. It uses Playwright for web scraping and BeautifulSoup for parsing HTML content.

## Features

- Web interface for entering search keywords.
- Scrapes job listings from Wanted.co.kr based on the keyword.
- Displays job title, company name, and a link to the job listing.
- Option to export the scraped job listings into a CSV file.

## Requirements

- Python 3.x
- Flask
- BeautifulSoup
- Playwright

## Installation

Ensure Python is installed, then install the required packages:

```bash
pip install Flask beautifulsoup4 playwright
```

Run the Playwright install command to download necessary browser binaries:

```bash
playwright install
```

## Usage

To start the web application, run:

```bash
python main.py
```

Navigate to `http://localhost:3000` in your web browser, enter a search keyword, and view the results.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
