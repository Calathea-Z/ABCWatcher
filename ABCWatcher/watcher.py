import requests
import hashlib
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

class WebsiteWatcher:
    def __init__(self, url):
        self.url = url
        load_dotenv()  # Load environment variables at the beginning of the initialization
        self.email_sender = os.getenv("EMAIL_USERNAME")
        self.email_receiver = os.getenv("EMAIL_USERNAME")  # Consider changing to "EMAIL_RECEIVER" if you intend to send the email to a different address
        self.email_password = os.getenv("EMAIL_PASSWORD")
        self.current_hash = self.load_last_hash()

    def fetch_webpage(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # This will raise an exception for HTTP errors
            return response.text
        except requests.exceptions.RequestException as e:  # This will catch errors such as connection errors
            print(f"Failed to fetch webpage: {e}")
            return ""

    def hash_content(self, content):
        if content:  # Ensure there is content to hash
            return hashlib.sha256(content.encode('utf-8')).hexdigest()
        else:
            return None

    def send_email(self, subject, body):
        try:
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
        except smtplib.SMTPException as e:
            print(f"Failed to send email: {e}")

    def save_hash(self, new_hash):
        if new_hash:  # Ensure there is a new hash to save
            os.makedirs("data", exist_ok=True)  # Ensure the data directory exists
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
        if webpage_content:  # Ensure there is content before proceeding
            new_hash = self.hash_content(webpage_content)
            if new_hash and new_hash != self.current_hash:
                print("Webpage has changed, sending email...")
                self.send_email("Webpage Update", "The webpage has been updated.")
                self.save_hash(new_hash)
                self.current_hash = new_hash
            else:
                print("No change detected.")

if __name__ == "__main__":
    target_url = "https://www.durhamabc.com/news"  # Change this URL to monitor a different website

    watcher = WebsiteWatcher(target_url)  # Simplified constructor call
    watcher.run()