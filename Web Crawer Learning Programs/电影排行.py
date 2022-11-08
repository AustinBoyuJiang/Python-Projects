from urllib.request import urlopen
import re   
from bs4 import BeautifulSoup  
from distutils.filelist import findall  

page =urlopen('http://movie.douban.com/top250?format=text')   
contents = page.read()   
 #print(contents)  
soup = BeautifulSoup(contents,"html.parser")

print("豆瓣电影TOP250" + "\n")
n=0
for tag in soup.find_all('div', class_='info'):
    n=n+1
    m_name = tag.find('span', class_='title').get_text()        
    m_rating_score = float(tag.find('span',class_='rating_num').get_text())          
    m_people = tag.find('div',class_="star")  
    m_span = m_people.findAll('span')  
    m_peoplecount = m_span[3].contents[0]  
    m_url=tag.find('a').get('href')  
    print("TOP",n,":\n电影名:",m_name+"\n评分:",str(m_rating_score)+"\n"+m_peoplecount+"\n网址:",m_url+"\n" )

