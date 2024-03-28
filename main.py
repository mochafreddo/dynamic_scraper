import csv
import time

from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.wanted.co.kr/search?query=flutter&tab=position")

        for _ in range(5):
            time.sleep(5)
            page.keyboard.down("End")

        content = page.content()
        browser.close()

    soup = BeautifulSoup(content, "html.parser")
    jobs = soup.select("div.JobCard_container__FqChn")

    jobs_data = []
    for job in jobs:
        link = f"https://www.wanted.co.kr{job.find('a')['href']}"
        title = job.find("strong", class_="JobCard_title__ddkwM").text
        company_name = job.find("span", class_="JobCard_companyContent__zUT91").text
        jobs_data.append({"title": title, "company_name": company_name, "link": link})

    write_to_csv(jobs_data)


def write_to_csv(jobs_data):
    fieldnames = ["Title", "Company", "Link"]
    with open("jobs.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(jobs_data)


if __name__ == "__main__":
    main()
