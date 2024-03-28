import time

from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

from file import write_to_csv


class WantedScraper:
    def __init__(self, keyword):
        self.browser = None
        self.page = None
        self.keyword = keyword

    def start(self):
        with sync_playwright() as p:
            self.browser = p.chromium.launch(headless=False)
            self.page = self.browser.new_page()
            self.page.goto(
                f"https://www.wanted.co.kr/search?query={self.keyword}&tab=position"
            )

            for _ in range(5):
                time.sleep(1)
                self.page.keyboard.down("End")

            content = self.page.content()
            self.browser.close()

        soup = BeautifulSoup(content, "html.parser")
        jobs = soup.select("div.JobCard_container__FqChn")

        jobs_data = []
        for job in jobs:
            link = f"https://www.wanted.co.kr{job.find('a')['href']}"
            title = job.find("strong", class_="JobCard_title__ddkwM").text
            company_name = job.find("span", class_="JobCard_companyContent__zUT91").text
            jobs_data.append(
                {"title": title, "company_name": company_name, "link": link}
            )

        self.write_to_csv(jobs_data)

    def write_to_csv(self, jobs_data):
        write_to_csv(self.keyword, jobs_data)


if __name__ == "__main__":
    keywords = [
        "flutter",
        "nextjs",
        "kotlin",
    ]

    for keyword in keywords:
        scraper = WantedScraper(keyword)
        scraper.start()
