# from get_url import get_request_url
import urllib.request
import json, xmltodict
import math
from config import *

# def get_keyword():
end_point="http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson"
parameters="?serviceKey="+service_key
parameters+="&pageNo=1"  
parameters+="&numOfRows=10"
parameters+="&startCreateDt=20200310" 
parameters+="&endCreateDt=20200315"

url = end_point+parameters
req = urllib.request.Request(url)
response = urllib.request.urlopen(req)
req = response.read().decode('utf-8')
# print(req)
dict = xmltodict.parse(req)
jsonString = json.dumps(dict['response']['body'], ensure_ascii=False)
jsonData = json.loads(jsonString)


jsonResult=[]

for item in jsonData['items']['item']:
    date = item['stateDt'] # 기준일 
    decide = item['decideCnt']  # 확진자 수 
    acc = item['accExamCnt']  # 누적 검사 수 
    print(date, " ", decide," ",acc)
    jsonResult.append({'stateDt': date, 'decideCnt': decide, 'accExamCnt':acc})
print(jsonResult)


with open('covid19.json','w', encoding='utf-8') as file:
    jsonOut=json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
    file.write(jsonOut)

