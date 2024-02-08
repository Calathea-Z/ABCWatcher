import requests
import hashlib
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

class WebsiteWatcher:
    def __init__(self, url, email_sender, email_receiver, email_password):
        self.url = url
        self.email_sender = os.getenv("EMAIL_USERNAME")
        self.email_receiver = os.getenv("EMAIL_USERNAME")
        self.email_password = os.getenv("EMAIL_PASSWORD")
        self.current_hash = self.load_last_hash()

    def fetch_webpage(self):
        response = requests.get(self.url)
        return response.text

    def hash_content(self, content):
        return hashlib.sha256(content.encode('utf-8')).hexdigest()

    def send_email(self, subject, body):
        msg = MIMEMultipart()
        msg['From'] = self.email_sender
        msg['To'] = self.email_receiver
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(self.email_sender, self.email_password)
        text = msg.as_string()
        server.sendmail(self.email_sender, self.email_receiver, text)
        server.quit()

def save_hash(self, new_hash):
    with open("data/last_hash.txt", "w") as file:  # Updated path
        file.write(new_hash)

def load_last_hash(self):
    try:
        with open("data/last_hash.txt", "r") as file:  # Updated path
            return file.read().strip()
    except FileNotFoundError:
        return ""

    def run(self):
        webpage_content = self.fetch_webpage()
        new_hash = self.hash_content(webpage_content)
        if new_hash != self.current_hash:
            print("Webpage has changed, sending email...")
            self.send_email("Webpage Update", "The webpage has been updated.")
            self.save_hash(new_hash)
            self.current_hash = new_hash
        else:
            print("No change detected.")

if __name__ == "__main__":
    load_dotenv()
    target_url = "https://www.durhamabc.com/news"  # Change this URL to monitor a different website
    email_sender = os.getenv("EMAIL_USERNAME")
    email_receiver = os.getenv("EMAIL_USERNAME")  # Update if necessary
    email_password = os.getenv("EMAIL_PASSWORD")

    watcher = WebsiteWatcher(target_url, email_sender, email_receiver, email_password)
    watcher.run()