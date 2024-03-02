  from playwright.sync_api import sync_playwright
  import time
  from bs4 import BeautifulSoup
  import csv

  #함수
  def job_scrapper(search_word):
      #playwright 시작
      p = sync_playwright().start()
      #크롬 브라우저 생성(headless=True:브라우저를 안키고 동작/False:브라우저를 켜서 동작)
      browser = p.chromium.launch(headless=False)
      #새 창 생성
      page = browser.new_page()
      #페이지 이동
      page.goto("https://www.wanted.co.kr/")
      #스크린샷
      #page.screenshot(path="screenshot.png")
      #set timeout 3초
      time.sleep(3)
      #페이지 내 클릭 이벤트 실행(tag와 클래스 명으로 지정)
      page.click("button.Aside_searchButton__Xhqq3")
      #위의 클릭과 동일한 기능(locator가 seleter인듯 함)
      #page.locator("button.Aside_searchButton__Xhqq3").click()
      #set timeout 3초
      time.sleep(3)

      page.get_by_placeholder("검색어를 입력해 주세요.").fill(search_word)
      #set timeout 3초
      time.sleep(3)
      #엔터키를 누른다.
      page.keyboard.down("Enter")
      #set timeout 5초
      time.sleep(5)
      #a태그를 클릭한다.
      page.click("a#search_tab_position")
      for x in range(5):
          #set timeout 5초
          time.sleep(5)
          #엔드 키를 누른다.
          page.keyboard.down("End")
      #콘텐트 변수에 페이지 콘텐트를 넣는다.
      content = page.content()
      #메모리 누수 방지를 위해
      p.stop()
      #콘텐트 변수를 BeautifulSoup 에 넣어서 html parser를 하여 soup 변수에 넣는다.
      soup = BeautifulSoup(content,"html.parser")
      #soup 변수에서 job에 대한걸 찾아서 jobs리스트에 넣는다.
      jobs = soup.find_all("div",class_="JobCard_container__FqChn")
      #오브젝트를 담을 변수를 생성
      jobs_db = []
      #for 반복문을 통해 jobs에서 필요한 데이터를 가져온다.
      for job in jobs:
          #a태그에 href정보를 link 변수에 넣는다.
          link = f"https://www.wanted.co.kr{job.find('a')['href']}"
          #strong태그에 text정보를 title 변수에 넣는다.
          title = job.find("strong",class_="JobCard_title__ddkwM").text
          #span태그에 text정보를 company_name 변수에 넣는다.
          company_name = job.find("span",class_="JobCard_companyName__vZMqJ").text
          #span태그에 text정보를 reward 변수에 넣는다.
          reward = job.find("span",class_="JobCard_reward__sdyHn").text
          #오브젝트화 하여 데이터를 넣는다.
          job = {
              "title" : title,
              "company_name" : company_name,
              "reward" : reward,
              "link" : link
          }
          #jobs_db에 job을 추가한다.
          jobs_db.append(job)
      #확인을 위해 console에 보여준다.
      #print(jobs_db)
      #확인을 위해 jobs_db 개수를 console에 보여준다.
      #print(len(jobs_db))
      #csv 파일을 만든다, 인코딩 utf-8을 해야 vs code에서 한글이 보인다(다만 엑셀에선 한글깨짐), newline=""을 해야 줄 넘김이 없음.
      file = open(f"{search_word}_jobs.csv", "w", encoding="utf-8", newline = "")
      #csv파일에 데이터를 넣기 위해 writter 변수에 추가
      writter = csv.writer(file)
      #header 부분 작성
      writter.writerow(["Title","Company","Reward","Link"])
      #jobs 리스트를 반복문을 돌려 CSV에 한줄씩 추가
      for job in jobs_db:
          #딕셔너리에서 데이터만 가져다가 list로 만들어서(job.values()) csv에 한줄씩 추가
          writter.writerow(job.values())
      #메모리 누수 방지를 위해 파일 닫기
      file.close()

  #조회할 키워드
  keywards = [
      "flutter",
      "next js",
      "kotlin"
  ]

  #키워드 수만큼 반복
  for x in keywards:
      #함수 실행
      job_scrapper(x)