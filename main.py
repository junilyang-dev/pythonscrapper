from flask import Flask
from extractors.indeed import extract_indeed_jobs
from extractors.wwr import extract_wwr_jobs
from file import save_to_file
#Flask 객체 생성
app = Flask("JobScrapper")
#루트 라우팅
@app.route("/")
#루트 함수
def home():
  #루트 함수 반환
  return 'hey there!'
#루트 함수 실행
app.run("0.0.0.0")

# keyword = input("What do you want to search for?")

# #indeed = extract_indeed_jobs(keyword)
# wwr = extract_wwr_jobs(keyword)
# #jobs = indeed + wwr
# jobs = wwr
# save_to_file(keyword, jobs)