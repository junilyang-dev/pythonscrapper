from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup
import csv

class JobScrapper:
    def __init__(self, search_word):
        self.search_word = search_word

    def start(self):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            page.goto("https://www.wanted.co.kr/")
            time.sleep(3)
            page.click("button.Aside_searchButton__Xhqq3")
            time.sleep(3)
            page.get_by_placeholder("검색어를 입력해 주세요.").fill(self.search_word)
            time.sleep(3)
            page.keyboard.press("Enter")
            time.sleep(5)
            page.click("a#search_tab_position")
            for _ in range(5):
                time.sleep(5)
                page.keyboard.press("End")
            content = page.content()
            p.stop()
            self.scrape_jobs(content)

    def scrape_jobs(self, content):
        soup = BeautifulSoup(content, "html.parser")
        jobs = soup.find_all("div", class_="JobCard_container__FqChn")
        jobs_db = []
        for job in jobs:
            link = f"https://www.wanted.co.kr{job.find('a')['href']}"
            title = job.find("strong", class_="JobCard_title__ddkwM").text
            company_name = job.find("span", class_="JobCard_companyName__vZMqJ").text
            reward = job.find("span", class_="JobCard_reward__sdyHn").text
            job_data = {
                "title": title,
                "company_name": company_name,
                "reward": reward,
                "link": link
            }
            jobs_db.append(job_data)
        self.write_to_csv(jobs_db)

    def write_to_csv(self, jobs_db):
        file_name = f"{self.search_word}_jobs.csv"
        with open(file_name, "w", encoding="utf-8", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Title", "Company", "Reward", "Link"])
            for job in jobs_db:
                writer.writerow(job.values())

# 조회할 키워드 리스트
keywords = ["flutter", "next js", "kotlin"]

# 키워드 수만큼 반복하여 스크래핑 실행
for keyword in keywords:
    job_scrapper = JobScrapper(keyword)
    job_scrapper.start()