import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://quotes.toscrape.com"

# 1. Download the page
response = requests.get(url)
response.raise_for_status()

# 2. Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

quotes_data = []

# 3. Each quote block is in <div class="quote">
for block in soup.find_all("div", class_="quote"):
    text_el = block.find("span", class_="text")
    author_el = block.find("small", class_="author")
    tag_els = block.find_all("a", class_="tag")

    text = text_el.get_text(strip=True) if text_el else None
    author = author_el.get_text(strip=True) if author_el else None
    tags = ", ".join(t.get_text(strip=True) for t in tag_els)

    quotes_data.append({
        "Quote": text,
        "Author": author,
        "Tags": tags
    })

# 4. Put into DataFrame
df = pd.DataFrame(quotes_data)

# 5. Save as Excel file
excel_file = "quotes_toscrape.xlsx"
df.to_excel(excel_file, index=False, sheet_name="Quotes")

print(f"Scraped {len(df)} quotes and saved to {excel_file}")
print(df.head())
