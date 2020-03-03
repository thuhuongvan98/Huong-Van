import requests
from bs4 import BeautifulSoup
import pyexcel

income = requests.get('http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn')
soup = BeautifulSoup(income.text,'html.parser')

div_content = soup.find('div',{'class': 'cf_ResearchDataHistoryInfo'})

table = div_content.find('table',{'id': 'tableContent'})
tr_content = table.find_all('tr')
all_account = []
for x in tr_content:
    td_content = x.find_all('td')
    account = []
    for y in td_content:
        if y.string == None:
            pass
        else:
            account.append(y.string.strip())
    if len(account) < 5:
        pass
    else:
        all_account.append(account) 
    income_statement = []
for i in all_account:
    data = {
        'Account': i[0],
        'Q4/2016': i[1],
        'Q1/2017': i[2],
        'Q2/2017': i[3],
        'Q3/2017': i[4]
    }
    income_statement.append(data)

pyexcel.save_as(records=income_statement, dest_file_name='lesson8_hw.xlsx')