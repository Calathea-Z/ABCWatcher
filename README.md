The application is designed to automatically monitor changes on a specified webpage and send email notifications when updates are detected. Leveraging Python scripts, it provides a seamless way to keep users informed about new content or modifications on websites of interest, without the need for manual checking. Ideal for tracking updates on news sites, blogs, or any web page requiring regular surveillance, this tool streamlines the process of staying up-to-date with changes, ensuring users never miss important updates.


Setup Instructions:

Step 1: Downloading the Script from GitHub

Navigate to the GitHub Repository: Open your web browser and go to the GitHub page where the script is hosted.

Download the Repository: Look for a green button labeled “Code” near the top of the page. Click it, then select “Download ZIP”.

Extract the ZIP File: Once downloaded, navigate to your Downloads folder, right-click the ZIP file, and choose “Extract All…”. Choose where you want to extract the files and confirm. Step 2: Setting Up Gmail

Enable 2-Step Verification: Sign in to your Google Account. Go to the "Security" section. Find "2-Step Verification" and follow the prompts to enable it.

Create an App Password: Still in the "Security" section, find "App passwords" (you might need to sign in again). Select “Mail” as the app, choose “Other” for the device, and name it (e.g., “Python Script”). Click “Generate”. Google will provide a 16-character password. Note this down; you’ll need it soon.

Step 3: Setting Up Python and Required Packages

Install Python: Download Python from python.org. Run the installer. Ensure you check “Add Python to PATH” before installing.

Install Required Packages: Open Command Prompt and install the necessary packages by running:

Step 4: Creating a .env File for Configuration

Navigate to the Script’s Folder: Open the folder where you extracted the GitHub download.
Create the .env File: Right-click in the folder, select “New” > “Text Document”, and name it .env (ensure it’s not .env.txt). Open .env with Notepad, and add the following lines: Replace your_email@gmail.com with your Gmail address and the_16_character_password with the app password generated earlier. Save and close the file.
Step 5: Testing the Script

Open Command Prompt in the Script’s Folder: In the folder, hold Shift, right-click in an empty space, and choose “Open PowerShell window here” or “Open command window here”.

Run the Script: Type python watcher.py (replace watcher.py with the actual script name if different) and press Enter. Verify it runs successfully and sends an email.

Step 6: Scheduling the Script with Task Scheduler

Open Task Scheduler: Press Windows + R, type taskschd.msc, and press Enter.

Create a New Task: Click “Create Task…” in the right-hand pane. Name your task (e.g., “Website Watcher”).

Set the Trigger: Go to the “Triggers” tab, click “New…”. Set “Begin the task” to “On a schedule”. Choose “Daily” and set “Repeat task every” to “30 minutes” for a duration of “Indefinitely”. Click “OK”.

Set the Action: Go to the “Actions” tab, click “New…”. Set “Action” to “Start a program”. In “Program/script”, type python. In “Add arguments (optional)”, type the path to your script (e.g., C:\Users\YourName\Downloads\ScriptFolder\watcher.py). Click “OK”.

Finish and Test: Click “OK” to save the task. Right-click your task and select “Run” to test it.

Final Notes

Ensure the computer stays on for the script to run as scheduled. If the script or the environment changes (e.g., moving the script to a different folder), you’ll need to update the task in Task Scheduler accordingly. This guide assumes a Windows environment; steps may vary slightly
