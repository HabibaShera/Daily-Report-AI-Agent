# Sends the final report to Gmail
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import markdown
#from settings import sender_email, sender_password


def send_email(subject: str, body: str, recipient: str):
    # create the email
    sender_email = os.getenv("sender_email")
    sender_password = os.getenv("sender_password")

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = recipient
    msg["Subject"] = subject

    # Attach parts into message container.
    part1 = MIMEText(body, "html")    # actual HTML for Gmail

    msg.attach(part1)

    # Send using Gmail SMTP (old way)
    # with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    #     server.login(sender_email, sender_password)
    #     server.sendmail(sender_email, recipient, msg.as_string())

    try:
        # connect to Gmail SMTP server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient, msg.as_string())
        server.quit()
        print(f"✅ Email sent to {recipient}")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")


if __name__ == "__main__":  
    text = """
**Headline:**  
🚀 “Docker MCP Toolkit: Run AI‑Powered Automation Locally in Minutes”

**Key Takeaways**

- 🏗️ **MCP Server = AI Bridge** – Lets AI tools talk to code, cloud, and apps.
- 🌐 **Many Servers Available** – GitHub, Terraform, Azure, Jira, Slack, and 100+ more.
- 🏠 **Run Locally with Docker** – No cloud costs, secrets stay on your machine, quick testing.
- 🛠️ **Docker MCP Toolkit** – One‑click install, searchable catalog, built‑in agent support (Copilo t, Claude, Cu
rsor).
- 🔒 **Secure Containers** – Each server runs isolated, keeping your data safe.
- 📊 **Unified Dashboard** – Manage all MCP servers from a single place.
- 🚀 **Get Started** – Install Docker Desktop → add MCP Toolkit → launch a server → connect your AI agent → automate!
- 🤝 **Future‑Proof** – Easy, safe building blocks for agentic AI teams and enterprises.
"""

    html_content = markdown.markdown(text, extensions=["extra", "sane_lists"])
    #print(html_content)

    send_email(
        subject="Daily AI Report",
        body=html_content,
        recipient="habibashera128@gmail.com"
    )
