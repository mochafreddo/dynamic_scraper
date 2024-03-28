# WantedScraper

WantedScraper is a Python tool designed to scrape job listings from the website Wanted.co.kr based on a given keyword. It utilizes the Playwright library for web scraping and BeautifulSoup for parsing the scraped HTML content.

## Features

- Scrapes job listings based on a keyword.
- Extracts job title, company name, and job listing link.
- Saves the scraped data into a CSV file named `<keyword>_jobs.csv`.

## Requirements

- Python 3.x
- BeautifulSoup
- Playwright

## Installation

First, ensure you have Python installed. Then, install the required Python packages using pip:

```bash
pip install beautifulsoup4 playwright
```

You may need to run the Playwright install command to download the necessary browser binaries:

```bash
playwright install
```

## Usage

To use WantedScraper, run the `main.py` script with the desired keyword as an argument:

```bash
python main.py <keyword>
```

Replace `<keyword>` with the actual keyword you want to search for.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
