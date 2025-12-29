# Quotes to Excel: Web Scraper in Python

This project demonstrates how to build a simple web scraper in Python that:
- Downloads quotes from [https://quotes.toscrape.com](https://quotes.toscrape.com)
- Extracts the quote text, author, and tags with BeautifulSoup
- Saves the results into an Excel file using pandas

  ![How it looks like](Screenshot%202025-12-29%20at%2016.21.37.png)


## Features

- Scrapes all quote blocks on the first page of `quotes.toscrape.com`
- Collects:
  - Quote text
  - Author name
  - Comma‑separated list of tags
- Exports the data to `quotes_toscrape.xlsx`

## Requirements

- Python 3.9+
- `requests`
- `beautifulsoup4`
- `pandas`
- `openpyxl` (for writing `.xlsx` files)

## Usage

1. Clone or download this project.
2. Place the script (e.g. `quotes_to_excel.py`) in your project folder.
3. Run:


4. After it finishes, open `quotes_toscrape.xlsx` in Excel, LibreOffice, or another spreadsheet tool.

## Script outline

The script:

1. Sends an HTTP GET request to `https://quotes.toscrape.com`.
2. Parses the HTML with BeautifulSoup.
3. Finds all `<div class="quote">` blocks.
4. From each block, extracts:
   - `span.text` → quote text  
   - `small.author` → author  
   - `a.tag` → tags (joined by commas)
5. Stores everything in a pandas DataFrame.
6. Writes the DataFrame to `quotes_toscrape.xlsx`.

## Notes

- The site is specifically designed for scraping practice and is safe to use for learning.
- For production scraping on other sites, always check `robots.txt`, terms of service, and be respectful with request frequency.

