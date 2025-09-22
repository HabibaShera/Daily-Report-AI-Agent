# Gets headlines & links from daily.dev (or page source)

from playwright.sync_api import sync_playwright
import csv


def open_daily_dev():
    url = "https://app.daily.dev/tags/ai-agents"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  # headless=False lets you see the browser
        context = browser.new_context()
        page = context.new_page()
        page.goto(url)

        # Wait for the page to load completely    
        page.wait_for_load_state("domcontentloaded")

        # Scroll down 2 times and wait for content to load
        for _ in range(2):
            page.mouse.wheel(0, 3000)   # scroll down by 3000 pixels
            page.wait_for_timeout(2000) 


        # Select all article elements by their class
        article_xpath = (
            "//article"
            "[contains(@class,'Card_post__S2J45') and contains(@class,'Card_card__BFnUM')]"
        )

        page.wait_for_selector(f"xpath={article_xpath}", timeout=10000)

        # Extract href from each article
        links = page.locator(f"xpath={article_xpath}").evaluate_all(
            "els => els.map(el => el.querySelector('a')?.href).filter(Boolean)"
        )

        # print("Extracted links:")
        # for link in links:
        #     print(link)



        # Keep browser open for a while so you can see it
        # page.wait_for_timeout(20000)  # 5 seconds

        browser.close()

    # print(f'Len of total links: {len(links)}')
    # print(f'Len after remove duplicates: {len(set(links))}')
    
    # Save to CSV
    with open("articles.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["link"])  # header
        for link in links:
            writer.writerow([link])

    print(f"✅ Extracted {len(links)} links and saved to articles.csv")
    
        

if __name__ == "__main__":
    open_daily_dev()
