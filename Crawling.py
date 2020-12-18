
import bs4
import requests
import pandas as pd 
import numpy as np
# import urllib.request
# from selenium import webdriver
# driver = webdriver.Chrome('chromedriver.exe')


url = 'https://www.i-sh.co.kr/main/lay2/S1T243C1045/contents.do'
result = requests.get(url)
aptData = bs4.BeautifulSoup(result.content, "html.parser")

apt_list=[]
def get_pre_apt():
    
    apt_table = aptData.find('table')
    apt_tbody = apt_table.find('tbody')
    apt_tr = apt_tbody.findAll('tr')
    # apt_td = apt_tbody.findAll('td')
    # firstLine = apt_tr.findAll('td', {'class':'firstLine'})

    for item in apt_tr:
        #------------------------
        tr_tag = list(item.strings)  # 리스트로 변환 
        # print(tr_tag)

        try:
            apt_name = tr_tag[1]
            apt_sum = tr_tag[3].strip()
            apt_addr = tr_tag[-2]

            if tr_tag[1] == '신규':
                apt_name = tr_tag[3]
                apt_sum = tr_tag[5].strip()
                apt_addr = tr_tag[-7] #1,2번재줄 짤라야함.

            # print(apt_name,"\n계: "+apt_sum,"\n주소: "+apt_addr)
            apt_list.append(apt_name+'/'+apt_sum+'/'+apt_addr)
            # print(apt_list)
        except:
            pass
    print(apt_list[:-1]) # 마지막 제외 
        #------------------------

if __name__ == '__main__':
    get_pre_apt()
    

