# Web-Scraper-For-Google-News-Headlines

## Project Overview

This project involves developing a web scraper to extract trending news articles from Google News using BeautifulSoup and Requests in Python. The scraper fetches news articles, extracts relevant details, and saves them into a CSV file for further analysis or usage.

## Features

1. **Inspect HTML Page**: Initially inspect the HTML structure of the Google News search result page to determine the correct selectors.
2. **Scrape News Articles**: Extract article titles, links, and descriptions from the search results.
3. **Save to CSV**: Save the extracted news articles to a CSV file.
4. **Handle Pagination**: Automatically navigate and scrape multiple pages of search results.

## Dependencies

- Python 3.x
- BeautifulSoup4
- Requests
- CSV
- Re (Regular Expressions)


## Project Structure

- `inspect_html.py`: Script to inspect the HTML content of the search result page.
- `scraper.py`: Main script to scrape news articles and save them to a CSV file.
- `page_content.html`: Output HTML file for inspection (created by `inspect_html.py`).

## Code Explanation

### Inspect HTML Page

The `inspect_html.py` script fetches the HTML content of the specified Google News search result page and saves it to a file for inspection.


### Scrape News Articles

The `scraper.py` script fetches news articles, extracts titles, links, and descriptions, and saves them to a CSV file. It also handles pagination to scrape multiple pages of search results.


## Conclusion

This project demonstrates how to use Python, BeautifulSoup, and Requests to build a web scraper for extracting news articles from Google News. The extracted data can be used for further analysis or integrated into other applications. The project handles HTML inspection, data extraction, and pagination to ensure comprehensive scraping of news articles.
