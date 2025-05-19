# 💼 Job Email Automation Toolkit

This repository provides a complete toolkit for automating the discovery, extraction, comparison, and management of job application emails—particularly useful when applying to Ausbildung (vocational training) positions across Germany.

## 📌 Features

- 🔍 **Scrape job listings** using Selenium
- 📧 **Extract emails** from structured or unstructured text
- 🧠 **Filter out known emails** and save new ones only
- 💾 Save job listings with emails for easy tracking
- 🔁 Easily combine & compare email datasets


🛠️ How to Use This Ausbildung.de Scraper
---
This script automates the process of:

Searching for jobs on ausbildung.de

Scrolling through all job listings

Visiting each job page

Extracting contact email, company name, and job title

Saving all results to a .txt file

🔧 Prerequisites
---
Python 3.x installed

Install required packages (if not already):


pip install selenium webdriver-manager

🚀 Usage Steps
---
Customize Your Search Term
Near the top of the script, change this line to whatever job you're looking for:


search_input.send_keys("Fachinformatiker/in")  # ← change this to your desired job keyword
---
Examples:

"Fachinformatiker/in für Systemintegration"

"Kaufmann/-frau für Büromanagement"

"Pflegefachmann/-frau"

Run the Script
---

It will:

Open Chrome

Search the term you specified

Scroll and load all results

Visit each listing

Extract contact emails

View the Results

After it finishes, check the generated file:

📁 emails_from_ausbildung.txt
Location: same folder as the script.

Each entry includes:

Email: [contact email]
Company: [company name]
Title: [job title]
Link: [link to job posting]

📌 Notes
---
Emails are de-duplicated automatically

If no email is found on a job page, that listing is skipped

If a “Mehr Ergebnisse laden” button appears, it is clicked automatically

You can tweak the script to filter by location or category later if needed
---
🙋‍♂️ Author
Amirhossein Estakhri
Freelance Developer | Automation Enthusiast 
---
💡 Future Improvements
---
📬 Automatically send personalized emails via Gmail API

☁️ Save results to Google Drive or Sheets

🧾 GUI for easier job management

📄 License
---
MIT License – feel free to use and modify.


Made with ❤️ to help automate job search for Ausbildung applications!
