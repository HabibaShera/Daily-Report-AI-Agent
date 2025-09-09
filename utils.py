# Helpers: logging, duplicate removal, formatting

import csv
import random
from playwright.sync_api import sync_playwright
import time


def get_random_articles(file_path="articles.csv", count=5):
    """
    Read links from a CSV file and return a random selection.

    Args:
        file_path (str): Path to the CSV file.
        count (int): Number of random articles to return.

    Returns:
        list: A list of randomly selected article links.
    """
    links = []

    # Read all links from the CSV (skip header)
    with open(file_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            links.append(row["link"])

    # Handle case when CSV has fewer links than requested
    if len(links) < count:
        return links

    return random.sample(links, count)





def open_and_read_article(article_link: str):
    """
    Open article link, extract the 'Read post' link, open it,
    wait 7 seconds, then close the browser.
    
    Args:
        article_link (str): The URL of the article page.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  # set headless=True if you don’t want UI
        page = browser.new_page()

        page.goto(article_link)

        try:
            read_post_selector = "a[aria-label='Read post'].btn.focus-outline.inline-flex.cursor-pointer.select-none.flex-row"
            read_post_href = page.get_attribute(read_post_selector, "href")

        except:
            print("⚠️ Could not find 'Read post' link!")
            browser.close()
            return

        # Step 3: Open the extracted link
        print(f"🔗 Opening post: {read_post_href}")
        page.goto(read_post_href, timeout=15000)  # wait up to 15 seconds for load

        # Extract all visible text
        text = page.inner_text("body")   # this grabs all *rendered* text inside <body>
        
        # Step 5: Close browser
        browser.close()
        return text, read_post_href



if __name__ == "__main__":
    links = get_random_articles()
    print(links[0])
    text = open_and_read_article(links[0])  # Open the first random article for demonstration
    
    with open('article_text.txt', 'w', encoding='utf-8') as f:
        f.write(text)
