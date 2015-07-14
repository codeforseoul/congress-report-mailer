
# coding: utf-8

# In[2]:

# http://data.popong.com/#api 에서 데이터 가져오기

import requests
import json
import pandas as pd

servicekey='test'
pagenum = 1
endpoint='http://api.popong.com/v0.1/bill/?api_key=test&page='
cont_dict = {}

while pagenum < 10 : # 원하는 페이지 만큼 가져오기
    response = requests.get(endpoint + str(pagenum))
    result = response.json()
    for item in result['items']:
        tmpDict = {}
        for key in item:
            tmpDict[key]=item[key]
        cont_dict[item['id']]=tmpDict
    pagenum += 1

df = pd.DataFrame(dict_key)
df = df.transpose()
df.to_csv('popong.csv', encoding='utf-8')


# 이하는 질문드리고 싶은 부분입니다..

# from sqlalchemy import create_engine
# engine = create_engine('mysql://root:비밀번호@localhost/congressReport', encoding='utf-8')

# import MySQLdb
# conn = MySQLdb.connect(host="localhost", user="root", passwd="비밀번호", db="congressReport")

# conn 또는 engine
# df.to_sql('popong_data2', conn, flavor='mysql', schema=None, if_exists='replace', index=False, index_label=None, chunksize=None, encoding='utf-8')

# 에러 메시지 (sqlalchemy, MySQLdb 에서 둘다 발생)
# UnicodeEncodeError: 'latin-1' codec can't encode characters in position 0-8: ordinal not in range(256)

