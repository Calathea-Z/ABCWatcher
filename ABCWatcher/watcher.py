import requests  # Library to make HTTP requests
import hashlib  # Library for hashing content
import smtplib  # Library for sending emails
import os  # Library for interacting with the operating system
from email.mime.text import MIMEText  # For creating emails
from email.mime.multipart import MIMEMultipart  # For creating multipart emails
from dotenv import load_dotenv 

class WebsiteWatcher:
    def __init__(self, url):
        self.url = url  # URL of the website to watch
        load_dotenv()  # Load environment variables

        # Retrieve email credentials and store them
        self.email_sender = os.getenv("EMAIL_USERNAME")  # Email address of the sender
        self.email_receiver = os.getenv("EMAIL_USERNAME")  # Intended receiver's email address
        self.email_password = os.getenv("EMAIL_PASSWORD")  # Email password for authentication
        self.current_hash = self.load_last_hash()  # Load the last saved hash of the webpage content

    def fetch_webpage(self):
        try:
            response = requests.get(self.url)  # Make a GET request to the specified URL
            response.raise_for_status()  # Raise an exception for HTTP errors
            return response.text  # Return the webpage content as text
        except requests.exceptions.RequestException as e:  # Catch any request-related errors
            print(f"Failed to fetch webpage: {e}")  # Print the error
            return ""  # Return an empty string in case of failure

    def hash_content(self, content):
        if content:  # Check if the content is not empty
            # Return the SHA-256 hash of the content encoded in utf-8
            return hashlib.sha256(content.encode('utf-8')).hexdigest()
        else:
            return None  # Return None if there's no content

    def send_email(self, subject, body):
        try:
            msg = MIMEMultipart()  # Create a MIMEMultipart message object
            msg['From'] = self.email_sender  # Set the sender's email
            msg['To'] = self.email_receiver  # Set the receiver's email
            msg['Subject'] = subject  # Set the email's subject

            msg.attach(MIMEText(body, 'plain'))  # Attach the email body as plain text

            server = smtplib.SMTP('smtp.gmail.com', 587)  # Create an SMTP server object for Gmail
            server.starttls()  # Start TLS encryption for security
            server.login(self.email_sender, self.email_password)  # Log in to the email server
            text = msg.as_string()  # Convert the message to a string
            server.sendmail(self.email_sender, self.email_receiver, text)  # Send the email
            server.quit()  # Quit the server
        except smtplib.SMTPException as e:  # Catch any SMTP-related errors
            print(f"Failed to send email: {e}")

    def save_hash(self, new_hash):
        if new_hash:  # Check if the new hash is not None
            os.makedirs("data", exist_ok=True)  # Create the data directory if it doesn't exist
            with open("data/last_hash.txt", "w") as file:  # Open the last_hash.txt file in write mode
                file.write(new_hash)  # Write the new hash to the file

    def load_last_hash(self):
        try:
            with open("data/last_hash.txt", "r") as file:  # Open the last_hash.txt file in read mode
                return file.read().strip()  # Read and return the hash, stripping any leading/trailing whitespace
        except FileNotFoundError:  # Catch the error if the file doesn't exist
            return ""  # Return an empty string if the file is not found

    def run(self):
        webpage_content = self.fetch_webpage()  # Fetch the current webpage content
        if webpage_content:  # Check if the content is not empty
            new_hash = self.hash_content(webpage_content)  # Hash the content
            # Check if the new hash is different from the current hash
            if new_hash and new_hash != self.current_hash:
                print("Webpage has changed, sending email...")
                # Send an email notification about the update
                self.send_email("Webpage Update", "The webpage has been updated.")
                self.save_hash(new_hash)  # Save the new hash
                self.current_hash = new_hash  # Update the current hash
            else:
                print("No change detected.")  # Print a message if no change is detected

if __name__ == "__main__":
    target_url = "https://www.durhamabc.com/news"  # URL to monitor for changes

    watcher = WebsiteWatcher(target_url)  # Create a WebsiteWatcher object
    watcher.run()  # Run the watcher
