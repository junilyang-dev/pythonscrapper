import requests 
from bs4 import BeautifulSoup

url = "https://weworkremotely.com/categories/remote-full-stack-programming-jobs#job-listings"

response = requests.get(url)

#print(response.content)

soup = BeautifulSoup(response.content, "html.parser",)
jobs = soup.find("section", class_="jobs").find_all("li")

print(jobs)