from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import re

# Setup WebDriver
options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Open the main job listing page
url = "https://www.azubica.de/ausbildungsberufe/fachinformatiker-fachrichtung-systemintegration/"
driver.get(url)

# Wait for job listings to load
try:
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href^="/ausbildungen/"][href*="?job="]'))
    )
    print("✅ Job cards loaded.")
except Exception as e:
    print("❌ Job cards not found in time.")
    driver.quit()
    exit()

# Scroll to load more jobs
for i in range(10):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1.5)

# Collect job links
job_cards = driver.find_elements(By.CSS_SELECTOR, 'a[href^="/ausbildungen/"][href*="?job="]')
job_links = []
for card in job_cards:
    href = card.get_attribute("href")
    if href.startswith("/"):
        full_url = "https://www.azubica.de" + href
    elif href.startswith("http"):
        full_url = href
    else:
        full_url = "https://www.azubica.de/" + href
    if full_url not in job_links:
        job_links.append(full_url)

print(f"🔍 Found {len(job_links)} job links.")

if not job_links:
    print("⚠️ No job links found.")
    driver.quit()
    exit()

# Collect emails with job links
email_data = []
for index, link in enumerate(job_links, 1):
    print(f"\n➡️ [{index}/{len(job_links)}] Visiting job: {link}")
    driver.get(link)

    try:
        bewerbung_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "bewirbdichbtn3"))
        )
        bewerbung_btn.click()
        print("✅ 'Jetzt bewerben!' clicked.")
        time.sleep(2)

        email_links = driver.find_elements(By.CSS_SELECTOR, 'a.btn-bewerbung[href^="mailto:"]')
        if email_links:
            mailto = email_links[0].get_attribute("href")
            match = re.search(r'mailto:([^?]+)', mailto)
            if match:
                email = match.group(1)
                entry = f"email = {email} | link = {link}"
                if entry not in email_data:
                    email_data.append(entry)
                    print(f"📧 {entry}")
            else:
                print("⚠️ Malformed mailto link.")
        else:
            print("❌ No email link found.")

    except Exception as e:
        print(f"⚠️ Error while processing: {e}")

# Save to file
if email_data:
    with open("emails_with_links.txt", "w", encoding="utf-8") as f:
        for line in email_data:
            f.write(line + "\n")
    print(f"\n💾 Saved {len(email_data)} email entries to 'emails_with_links.txt'")
else:
    print("⚠️ No emails collected.")

# Done
driver.quit()
