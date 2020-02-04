import bs4
import urllib.request as url

job = input("Enter job title/company : ")
path = f"https://www.indeed.co.in/{job}-jobs"

res = url.urlopen(path)
page = bs4.BeautifulSoup(res,'lxml')

jobs = page.find_all('div',class_='jobsearch-SerpJobCard')
for i in range(len(jobs)):
    job_title = jobs[i].find('div',class_='title')
    job_company = jobs[i].find('span',class_='company')
    job_location = jobs[i].find('span',class_='location')
    salary = jobs[i].find('div',class_='salarySnippet')
    print(job_title.text.strip())
    print(job_company.text.strip())
    if not job_location:
        print("Location Not Provided")
    else:
        print(job_location.text.strip())
    if not salary:
        print("Salary not disclosed...")
    else:
        print(salary.text.strip())
    print("="*20)

