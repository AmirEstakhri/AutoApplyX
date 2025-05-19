
# 💼 Job Email Automation Toolkit

A Python/Selenium toolkit to scrape, extract, filter, and manage job‑application emails for Ausbildung roles in Germany.

---

## 📌 Features
- 🔍 Scrape job listings on **ausbildung.de** & **azubica.de**  
- 📧 Extract emails, company names & job titles  
- 🧠 Filter out already‑known emails  
- 💾 Save new entries to text files  
- 🔁 Merge and compare multiple email datasets  

---

## 🔧 Requirements
````markdown
```bash
pip install selenium webdriver-manager
````

---

## 🚀 Usage
https://github.com/user-attachments/assets/cc143791-732b-40bd-a8e8-02d17e5f61b5
1. **Configure**

   * **Search term** (around line 30 in the script-you can change it to the job you want):

     ```python
     search_input.send_keys("Fachinformatiker/in")
     ```
   * **Target URL** (around line 10 in the script- change the url based on your needs):

     ```python
     url = "https://www.azubica.de/ausbildungsberufe/fachinformatiker-fachrichtung-systemintegration/"
     ```

2. **Run**

   ```bash
   python scraper.py
   ```

3. **Results**

   * Output file:

     * `emails_with_links.txt` (azubica.de version)
     * `emails_from_ausbildung.txt` (ausbildung.de version)
   * Entry formats:

```text
# azubica version:
email = someone@example.com | link = https://…

# ausbildung version:
Email: someone@example.com
Company: Company Name
Title: Job Title
Link: https://…
```

---

## 📌 Notes

* Scroll loop runs **10 times** by default (adjust `range(10)` if needed).
* Duplicates are automatically skipped.
* If the “Jetzt bewerben!” button (azubica) or “Mehr Ergebnisse laden” button (ausbildung) isn’t found, that listing is skipped or the button is clicked automatically.
* **This is not a spam tool — just a personal assistant to reduce time spent copy-pasting.**
* Script uses **visible Chrome** by default; enable headless mode by uncommenting:

```python
options.add_argument("--headless")
```

---

## 💡 Future Improvements

* 📬 Gmail API integration for auto‑sending personalized emails
* ☁️ Google Drive/Sheets export of results
* 🧾 GUI for non‑technical users
* 🗂️ CSV/Excel export option
* 🔍 Keyword & location filters built‑in

---

## 🛡️ License

**MIT License** © 2025 Amirhossein Estakhri

---

## 🙋‍♂️ Author

**Amirhossein Estakhri**
Freelance Backend Developer | Automation Enthusiast

```
```
