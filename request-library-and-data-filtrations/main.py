from bs4 import BeautifulSoup
import requests
import re
html_text = requests.get('https://www.shine.com/job-search/web-developer-jobs-in-mumbai?q=web-developer&loc=Mumbai').text
# print(html_text)

soup = BeautifulSoup(html_text,'lxml')
# print(soup.prettify())

jobs = soup.find_all('div',class_="jobCard_jobCard__jjUmu")

# print(jobs)


for job in jobs :
   job_title = job.find('a')
   # print(job_title.text)

name = soup.find_all('div',class_="jobCard_jobCard_cName__mYnow")

for company_name in name :
   cname = company_name.find('span')
#    print(cname.text)

skills = soup.find_all('div', class_ = "jobCard_skillList__KKExE")

for skill in skills :
    skill_text = skill.text
    cleaned_skill_text = re.sub(r'^\+[\d]+', '', skill_text).strip()  # Removes the leading "+" and numbers
    # print(cleaned_skill_text)

# links = soup.find_all('div','https://www.shine.com/job-search/web-developer-jobs-in-mumbai?q=web-developer&loc=Mumbai')
# print(jobs)

for link in jobs :
   hyperlink = link.strong.p.a['href']
   print(hyperlink)
