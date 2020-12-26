
# from get_url import get_request_url
import urllib.request
import json
import math
import pandas as pd
from config import *

def get_keyword():
    end_point="http://apis.data.go.kr/1140100/minAnalsInfoView2/minStaticsInfo2"
    parameters="?serviceKey="+service_key
    parameters+="&topN=10000" # 검색 결과 
    parameters+="&dateFrom=20201101" # 시작날짜 
    parameters+="&dateTo=20201213"  
    parameters+="&period=DAILY"  # 일별 
    parameters+="&sortBy=NAME&sortOrder=false" 
    parameters+="&sex=m"  # 남
    # parameters+="&sex=w"  # 여
    parameters+="&age=20"  
    # parameters+="&dataType=json"
    parameters+="&target=pttn,dfpt,saeol"

    url = end_point+parameters
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req)
    req = response.read().decode('utf-8')

    if(req==None):
        return None
    else:
        return json.loads(req)
        
jsonData = get_keyword()
print(jsonData)

# json
with open('stat_2020_m_20.json','w', encoding='utf-8') as file:
    jsonOut=json.dumps(jsonData, indent=4, sort_keys=True, ensure_ascii=False)
    file.write(jsonOut)

# csv
# with open('stat_2020_m_20.json','w', encoding='utf-8') as file:
#     df = pd.read_json(input)
# df.to_csv("stat_2020_m_20.csv", encoding="cp949", index=False)