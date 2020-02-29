import pymongo
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['c4e']

dantri_collection = db['dantri']

import requests
from bs4 import BeautifulSoup
dantri_content = requests.get('https://dantri.com.vn/')

# print(dantri_content.text)

soup = BeautifulSoup(dantri_content.text, 'html.parser')
# print(soup.prettify()) #khiến đoạn code dễ đọc hơn

div_content = soup.find('div',{'class': 'xnano'}) #('tên thẻ',{'class': 'tên class'})

ul_content = div_content.find('ul',{'class': 'ul1 ulnew'})

#tìm tất cả những cái cái có chung đặc điểm
li_content = ul_content.find_all('li') #li_content là 1 list chứa các thẻ li => k find tiếp đc
dantri_collection.delete_many({})
for li in li_content:
    news_link = li.h4.a['href'] #.string sẽ cho ra chỉ có chữ, ['href'] (do web đặt thế) cho ra link
    news_title = li.h4.a.string.strip()
    print(type(news_title))
    dantri_collection.insert_one({
        'news_title': news_title,
        'news_link': news_link
    })





