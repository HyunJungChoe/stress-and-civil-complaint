
# from get_url import get_request_url
import urllib.request
import json
import math
from config import *

def get_keyword(yyyymmdd):
    end_point="http://apis.data.go.kr/1140100/minAnalsInfoView2/minRisingKeyword2"
    parameters="?serviceKey="+service_key
    parameters+="&scoreMode=rising"  # 검색 방식 
    parameters+="&analysisTime="+yyyymmdd
    parameters+="&maxResult=5" # 검색 결과 
    parameters+="&dataType=json"
    parameters+="&target=pttn,dfpt,saeol"
    # parameters+="&age"

    url = end_point+parameters
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req)
    req = response.read().decode('utf-8')
    if(req==None):
        return None
    else:
        return json.loads(req)
        
# print(response.read().decode('utf-8'))
# req = get_request_url(url) # get_url.py
# jsonData = getNatVisitor(yyyymm, natinal_code,ed_cd)
jsonResult=[]
    # if( jsonData['response']['header']['resultCode'] =='200'):
        # for item in jsonData['response']['body']['items']['item'] :

for year in range(2020,2021):
    for month in range(1,12):
        for day in range(1,29,7):
            yyyymmdd = "{0}{1:0>2}{2:0>2}".format(str(year),str(month),str(day))   
            jsonData = get_keyword(yyyymmdd)
            print(json.dumps(jsonData, indent=4, sort_keys=True, ensure_ascii=False))
            for item in jsonData['returnObject']:
                # for item in jsonData['response']['body']['items']['item']:
                nw_date = item['date']
                nw_keyword = item['keyword']
                nw_df = item['df']
                # print(nw_date, " ", nw_keyword," ",nw_df)
                # jsonResult.append(nw_date)
                # jsonResult.append(nw_keyword)
                # jsonResult.append(nw_df)
                jsonResult.append({'date': nw_date, 'keyword': nw_keyword, 'df':nw_df})
print(jsonResult)

with open('keyword_2020.json','w', encoding='utf-8') as file:
    jsonOut=json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
    file.write(jsonOut)

# if __name__ == '__main__':
#     get_keyword()


