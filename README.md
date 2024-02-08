## Application Overview

This application is designed to monitor the Durham ABC webpage for any changes, sending email alerts automatically when updates are detected. It provides an efficient solution for tracking content modifications on the website without the need for manual checks. With minimal adjustments, this application can be adapted to monitor other websites, offering a versatile tool for web change detection.

### Key Features

- **Automated Monitoring:** Continuously watches the Durham ABC page for changes.
- **Email Alerts:** Sends notifications directly to your email upon detecting updates.
- **Versatility:** Easily adaptable to monitor various websites with minor modifications.

### Use Case

This tool is particularly useful for individuals or organizations looking to stay informed about updates or changes to specific web pages, such as product listings, news updates, regulatory changes, or availability of new resources.

### Getting Started

For installation instructions, setup details, and how to adapt this application for other websites, please refer to the [Installation and Setup Instructions](#installation-and-setup-instructions) section.

---

By leveraging this application, users can save time and ensure they remain up-to-date with the latest website changes, enhancing their ability to respond to new information swiftly.
# Website Watcher Setup Guide

This guide will help you set up the `watcher.py` script to monitor a website and alert you via email about any changes. The instructions are for Windows users.

## Prerequisites

- Ensure Python is installed on your system.
- Basic familiarity with Command Prompt in Windows is helpful.

## Installation and Setup Instructions

### Step 1: Install Python

- Download the latest Python version from the [official Python website](https://www.python.org/downloads/).
- Run the installer and make sure to select "Add Python to PATH".

### Step 2: Download the Script

- Navigate to the GitHub repository where `watcher.py` is hosted.
- Click "Code" > "Download ZIP", and extract it to a folder, e.g., `C:\WebsiteWatcher`.

### Step 3: Create a `.env` File

Within the script's directory:

1. Create a file named `.env`.
2. Add your email credentials:

   ```plaintext
   EMAIL_USERNAME=your_email@example.com
   EMAIL_PASSWORD=your_password

### Step 4: Install Required Packages

1. Open Command Prompt as administrator.
2. Navigate to your script's directory:

    ```shell
    cd C:\WebsiteWatcher
    ```

3. Install the required packages:

    ```shell
    pip install requests python-dotenv
    ```

### Step 5: Run the Script

- Execute the script via Command Prompt:

    ```shell
    python watcher.py
    ```

- Monitor the output for any indications of the script's execution status.

### Automating the Script with Task Scheduler (Windows)

#### Step 6: Schedule the Script

1. Open **Task Scheduler** from the Start menu.
2. Click **Create Basic Task...** in the **Action** menu.
3. Name your task (e.g., "Website Watcher").
4. Choose **Daily** as the trigger, then click **Next**.
5. Set the start date and time. Select **Repeat task every 1 hour** and choose **Indefinitely**.
6. For the action, select **Start a program**, then click **Next**.
7. Browse and select your Python executable in **Program/script**. In **Add arguments (optional)**, input the path to your `watcher.py` script.
8. Finish the wizard. Your script will now run automatically at the set interval, alerting you to any website changes.
