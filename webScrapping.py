import requests
import bs4
res=requests.get('paste here link of any websites')
res.test

# If you what to take indivisual parts of html then we code like this
#here we make soup an object

soup=bs4.BeautifulSoup(res.text,'lxml')
hi=soup.select('title')
print(hi)
