import requests 
from bs4 import BeautifulSoup
'''
all_jobs = []

#페이징 페이지가 있으므로 스크랩 기능을 함수로 만들어서 사용
def scrape_page(url):
  response = requests.get(url)#페이지 요청
  soup = BeautifulSoup(response.content, "html.parser",)#페이지 내용을 파싱
  jobs = soup.find("section", class_="jobs").find_all("li")[1:-1]#페이지 내용에서 필요한 정보를 추출

  for job in jobs:
    title = job.find("span", class_="title").text#제목
    company, position, region = job.find_all("span", class_="company")#회사, 직위, 지역
    url = job.find("div", class_="tooltip--flag-logo").next_sibling["href"]#링크
    job_data = {
      "title": title,
      "company": company.text,
      "position": position.text,
      "region": region.text,
      "url" : f"https://weworkremotely.com{url}",
    }
    all_jobs.append(job_data)#모든 정보를 리스트에 저장

#페이징 개수를 가져오는 함수
def get_pages(url):
  response = requests.get(url)#페이지 요청
  soup = BeautifulSoup(response.content, "html.parser",)#페이지 내용을 파싱
  return len(soup.find("div", class_="pagination").find_all("span",class_="page"))#페이지 개수를 리턴

total_pages = get_pages("https://weworkremotely.com/remote-full-time-jobs?page=1")#페이지 개수를 가져오는 함수를 호출

#페이지 개수를 가져와 스크랩 함수에 개수를 넣어 반복 호출
for x in range(total_pages):
  url = f"https://weworkremotely.com/remote-full-time-jobs?page={x+1}"#페이지를 가져오는 url
  scrape_page(url)#페이지를 스크랩하는 함수를 호출


print(len(all_jobs))#모든 정보를 가져왔으므로 개수를 출력
'''

keyword = [
  "flutter",
  "phthon",
  "golang"
]

all_jobs = []

def scrape_page(url,x):
  r = requests.get(
    "https://remoteok.com/remote-golang-jobs",headers={
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
    })

  soup = BeautifulSoup(r.text, "html.parser")
  jobs = soup.find("table", id="jobsboard").find_all("tr", class_="job")

  for job in jobs:
    print("----------------------------------")
    title = job.find("td", class_="company").find("h2", itemprop="title").text.replace('\n', '')
    company = job.find("td", class_="company").find("h3", itemprop="name").text.replace('\n', '')
    job_data = {
      "language":x,
      "title": title,
      "company": company
    }
    all_jobs.append(job_data)#모든 정보를 리스트에 저장

for x in keyword:
  url = f"https://remoteok.com/remote-{x}-jobs"#페이지를 가져오는 url
  scrape_page(url,x)#페이지를 스크랩하는 함수를 호출

print(all_jobs)