# 📧 Daily AI Report with GitHub Actions

This project automatically fetches AI-related articles, summarizes them using **Groq AI**, formats them into **HTML (Markdown converted)**, and sends a daily **email report** through Gmail.

The script runs automatically **every day at 8:00 AM Egypt time (Sunday → Thursday)** using **GitHub Actions**.

---

## 🚀 Features

* ✅ Fetches random AI/tech articles.
* ✅ Uses **Playwright** to extract article content.
* ✅ Summarizes articles with **Groq API**.
* ✅ Converts Markdown to **HTML** for nice formatting in Gmail.
* ✅ Sends automated email reports.
* ✅ Runs daily with **GitHub Actions (cron jobs)**.

---

## 📂 Project Structure

```
Daily-Report-AI-Agent/
│
├── .github/
│   └── workflows/
│       └── daily.yml        # GitHub Actions workflow (schedules daily run)
│
├── main.py                  # Main script (fetch + summarize + send email)
├── summarizer.py            # Uses Groq API to summarize text
├── utils.py                 # Helper functions (fetch articles, scrape, etc.)
├── emailer.py               # Handles Gmail SMTP email sending
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

---

## 📧 How Emails Look

* Headline
* Key takeaways in **bullet points**
* Summarized content
* "Read more" link

Formatted using **Markdown → HTML** so Gmail displays **bold, lists, and titles** properly.

---

## 🛠️ Setup Locally (Optional)

If you want to test locally before pushing:

```bash
# clone repo
git clone https://github.com/HabibaShera/Daily-Report-AI-Agent.git
cd Daily-Report-AI-Agent

# install dependencies
pip install -r requirements.txt

# run manually
python main.py
```

Make sure you create a `.env` file if running locally:

```
SENDER_EMAIL=your_email@gmail.com
SENDER_PASSWORD=your_gmail_app_password
GROQ_TOKEN=your_groq_api_key
```

---

## 🗓️ Schedule & Timezone Notes

* GitHub Actions runs on **UTC timezone**.
* Egypt is **UTC+2 (or +3 during DST)**.
* To hit **8:00 AM Egypt time**, cron is set to `30 5 * * 0-4` (5:30 UTC).

---

## ✅ Future Improvements

* Add multiple article sources.
* Store reports in a database before sending.
* Support multiple recipients.
