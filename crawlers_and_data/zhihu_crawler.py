import ssl
ssl._create_default_https_context = ssl._create_unverified_context

from urllib.request import urlopen 
from bs4 import BeautifulSoup 

url = "https://www.zhihu.com/question/518627949" 
html = urlopen(url) 

soup = BeautifulSoup(html, 'html.parser') 
type(soup) 

# Print out the text 

items = soup.find_all('p') 
for item in items:       
    print(item.text)
    print("\n")
