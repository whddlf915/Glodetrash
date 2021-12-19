# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pandas as pd
import matplotlib.pyplot as plt
# 필요한 모듈 import 하기
import plotly
import plotly.graph_objects as go
import plotly.express as px

# 한국거래서의 상장법인목록 엑셀 다운
stock_code = pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download', header=0)[0]


stock_code.sort_values(['상장일'], ascending=True)

stock_code = stock_code[['회사명', '종목코드']]

stock_code = stock_code.rename(columns={'회사명': 'company', '종목코드': 'code'})

stock_code.code = stock_code.code.map('{:06d}'.format)

company = 'LG화학'
code = stock_code[stock_code.company==company].code.values[0].strip()
page = 1

url = 'http://finance.naver.com/item/sise_day.nhn?code={code}'.format(code=code)
url = '{url}&page={page}'.format(url=url, page=page)
print(url)
df = pd.read_html(url, header=0)[0]
df.head()




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
