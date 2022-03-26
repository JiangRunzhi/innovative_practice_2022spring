import ssl
ssl._create_default_https_context = ssl._create_unverified_context

from urllib.request import urlopen 
from bs4 import BeautifulSoup 
url = "https://weibo.com/5044281310?refer_flag=1001030103_" 
html = urlopen(url) 
soup = BeautifulSoup(html, 'html.parser') 
type(soup) 
# Print out the text 
text = soup.get_text() 
print(soup.text)