# Entry point: runs the workflow (scrape → summarize → email)
from scraper import open_daily_dev
from utils import get_random_articles, open_and_read_article
from summarizer import summarize_text
from emailer import send_email
import markdown
import os




open_daily_dev()
result = ""


links = get_random_articles(count=2)
for link in links:
    text, read_more_link = open_and_read_article(link)
    if not text:   # if text is None or empty
        print(f"⚠️ Skipping article {link} because no content was found.")
        continue
    
    result += summarize_text(text)
    result += f"\n\n[Read more]({read_more_link})\n\n\n"

html_content = markdown.markdown(result, extensions=["extra", "sane_lists"])

emails = os.getenv("EMAIL_LIST", "").splitlines()
for recipient in emails:
    send_email(
            subject="Daily AI Report",
            body=html_content,
            recipient=recipient
        )





