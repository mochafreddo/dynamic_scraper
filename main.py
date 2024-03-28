import time

from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

p = sync_playwright().start()

browser = p.chromium.launch(headless=False)

page = browser.new_page()

page.goto("https://www.wanted.co.kr/search?query=flutter&tab=position")

# page.goto("https://www.wanted.co.kr/")

# time.sleep(5)

# page.click("button.Aside_searchButton__Xhqq3")

# time.sleep(5)

# page.get_by_placeholder("검색어를 입력해 주세요.").fill("flutter")

# time.sleep(5)

# page.keyboard.down("Enter")

# time.sleep(5)

# page.click("a#search_tab_position")

for x in range(5):
    time.sleep(5)
    page.keyboard.down("End")

content = page.content()

p.stop()

soup = BeautifulSoup(content, "html.parser")

jobs = soup.select("div.JobCard_container__FqChn")

jobs_db = []

for job in jobs:
    link = f"https://www.wanted.co.kr{job.find('a')['href']}"
    title = job.find("strong", class_="JobCard_title__ddkwM").text
    company_name = job.find("span", class_="JobCard_companyContent__zUT91").text
    # location = job.find("span", class_="JobCard_location__2EOr5").text
    # reward = job.find("span", class_="JobCard_reward__sdyHn").text
    job = {"title": title, "company_name": company_name, "link": link}
    jobs_db.append(job)

print(jobs_db)
print(len(jobs_db))
