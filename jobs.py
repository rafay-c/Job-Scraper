import requests
from bs4 import BeautifulSoup

URL = "https://jobs.github.com/positions?description=JavaScript" #change the description value for different searches

r = requests.get(URL)
s = BeautifulSoup(r.text,"html.parser")

for i in s.find_all("tr",class_="job"):
    print("Position: ", i.td.h4.a.text)
    print("Description Link: ", i.td.h4.a.attrs['href'])
    print("Company Name: ", i.find("a",class_="company").text)
    print("Company Url: ", i.find("a",class_="company").attrs['href'])
    print("Job Type: ", i.find("strong").text)
    print("Location: ", i.find("span",class_="location").text,"\n")

