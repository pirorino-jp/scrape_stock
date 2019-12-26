# そのまま実行しても動きません

■seleniumテスト

import time
import chromedriver_binary
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.google.com/')
time.sleep(5)
search_box = driver.find_element_by_name("q")
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5)
driver.quit()
-----------------------------------------------

■selenium株価ダウンロード

#import chromedriver_binary
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
driver = webdriver.Chrome()

def download_stock_csv(code_range,year_range):
    for code in code_range:
        try:
            for year in year_range:
                url = 'https://kabuoji3.com/stock/{0}/{1}/'.format(code,year)
                driver.get(url)
 
                try:
                    driver.find_element_by_name("csv").click()
                    time.sleep(3)
                    driver.find_element_by_name("csv").click()
                except NoSuchElementException:
                    print("no data:"+str(code)+" year:"+str(year))
                    pass
                time.sleep(1)
 	
        except NoSuchElementException:
            print("no data:"+str(code)+" year:"+str(year))
        pass
    time.sleep(3)

#1332,1333,1605,1721,1801,1802,1803,1808,1812,1925,1928,1963,2002,2269,2282,2432,2501,2502,2503,2531,2768,2801,2802,2871,2914,3086,3099,3101,3103,3105,3289,3382,3401,3402,3405,3407,3436,3861,3863,4004,4005,4021,4042,4043,4061,4063,4151,4183,4188,4208,4272,4324,4452,4502,4503,4506,4507,4519,4523,4543,4568,4578,4631,4689,4704,4751,4755,4901,4902,4911,5019,5020,5101,5108,5201,5202,5214,5232,5233,5301,5332,5333,5401,5406,5411,5541,5631,5703,5706,5707,5711,5713,5714,5801,5802,5803,5901,6098,6103,6113,6178,6301,6302,6305,6326,6361,6366,6367,6471,6472,6473,6479,6501,6503,6504,6506,6645,6674,6701,6702,6703,6724,6752,6758,6762,6770,6841,6857,6902,6952,6954,6971,6976,6988,7003,7004,7011,7012,7013,7186,7201,7202,7203,7205,7211,7261,7267,7269,7270,7272,7731,7733,7735,7751,7752,7762,7911,7912,7951,8001,
jp_225 = [8002,8015,8028,8031,8035,8053,8058,8233,8252,8253,8267,8303,8304,8306,8308,8309,8316,8331,8354,8355,8411,8601,8604,8628,8630,8725,8729,8750,8766,8795,8801,8802,8804,8830,9001,9005,9007,9008,9009,9020,9021,9022,9062,9064,9101,9104,9107,9202,9301,9412,9432,9433,9437,9501,9502,9503,9531,9532,9602,9613,9681,9735,9766,9983,9984]

download_stock_csv(jp_225,range(2019,2020))
-------------
quandle
xxx@gmail.com
xxx

import quandl
>>> quandl.ApiConfig.api_key = '123456789ABCDEFG'
>>> data = quandl.get('TSE/6758')
>>> data [:5]
xxx


import datetime
import quandl
import pandas as pd

# 各種設定
## 取得したい日付レンジの指定
start = datetime.datetime(2018, 1, 1)
end = datetime.datetime(2019, 8, 1)

# 取得したい会社のティックシンボルを記載します。
## 例えばの武田薬品工業の場合　TSE/4502 となります。
## https://www.quandl.com/data/TSE/4502-Takeda-Pharmaceutical-Co-Ltd-4502
company_id = 'TSE/4502'

# APIキーの設定
quandl.ApiConfig.api_key = 'xxx'

# データ取得
df = quandl.get(company_id) # 無料版では2017年終わりまでしか取れません

-----------------------------------
■matplotlibで使えるフォントの確認
import matplotlib.font_manager as fm
fm.findSystemFonts()

import matplotlib as mpl
mpl.matplotlib_fname()
'D:\\projects\\pyeprog\\env\\Lib\\site-packages\\matplotlib\\mpl-data\\matplotlibrc'


matplotlib.font_manager._rebuild()


pip install --upgrade matplotlib


■pandas株価分析

import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams

#os.chdir("C:\\Users\\piror\\Downloads") #ファイルの場所を指定，先にデータを入れておく
path = "C:\\Users\\piror\\Downloads\\"

plt.rcParams['figure.figsize'] = [10, 5]
plt.rcParams['xtick.direction'] = 'in'#x軸の目盛線が内向き('in')か外向き('out')か双方向か('inout')
plt.rcParams['ytick.direction'] = 'in'#y軸の目盛線が内向き('in')か外向き('out')か双方向か('inout')
plt.rcParams['xtick.major.width'] = 1.0 #x軸主目盛り線の線幅
plt.rcParams['ytick.major.width'] = 1.0 #y軸主目盛り線の線幅
plt.rcParams['font.size'] = 12 #フォントの大きさ
plt.rcParams['axes.linewidth'] = 1.0 # 軸の線幅edge linewidth。囲みの太さ
plt.rcParams['font.family'] = 'sans-serif' #使用するフォント名
plt.rcParams['font.sans-serif'] = ['Hiragino Maru Gothic Pro', 'Yu Gothic', 'Meirio', 'Takao', 'IPAexGothic', 'IPAPGothic', 'Noto Sans CJK JP']

code = 8729
start = 2019
end = 2020

x = []
y = []

for n in range (start, end):
    file_name = str(code)+'_%d.csv' %n #ファイル名を指定
    try:
        firstline = list(pd.read_csv(path + file_name, nrows=1,encoding='cp932'))
        stockname = firstline[0]
        data = pd.read_csv(path + file_name, header=1,encoding='cp932')
    except FileNotFoundError:
        print("File not found:"+file_name)
        sys.exit
    a =list(pd.to_datetime(data.iloc[:,0], format='%Y-%m-%d'))
    x += a[::] 
    b = list(data.iloc[:,4])
    y += b[::]

# 為替
ex_file_name = 'full_webstats_eer_d_dataflow_csv_row.zip' #ファイル名を指定
try:
    ex_data = pd.read_csv(path + ex_file_name, header=3, encoding='cp932')
except FileNotFoundError:
    print("File not found:"+file_name)
    sys.exit


z = pd.DataFrame(y)#DataFrameに変換
sma75 = pd.DataFrame.rolling(z, window=75,center=False).mean()
sma25 = pd.DataFrame.rolling(z, window=25,center=False).mean()

# MACDの計算を行う
ema12 = pd.DataFrame.rolling(z, window=12,center=False).mean()
ema26 = pd.DataFrame.rolling(z, window=26,center=False).mean()
macd = pd.DataFrame()
macd = ema12 - ema26
macd_signal = macd.ewm(span=9).mean()
# macd.head()

# 為替の計算

ex_data = ex_data.drop(0, axis=0) #余計な先頭行を削除 ちゃんと結果を入れてあげないと更新できないので注意
ex_data = ex_data.dropna(how='any', axis=0) #nanを含む行を削除 ちゃんと結果を入れてあげないと更新できないので注意

ex_x = pd.DataFrame(x)#DataFrameに変換
ex_x2 = ex_x.set_index([0]) #1銘柄目の日付をインデックスに設定する
ex_x2 = ex_x2.assign(yen=None) # 円の列追加
ex_x2 = ex_x2.assign(doller=None) # ドルの列追加

for n in range(len(ex_data)): # 株価配列を元に、日付をマッチさせてその日付の為替を取得、リスト化する
    # print(n)
    try:
        match_no = ex_x2.index.get_loc(pd.to_datetime(ex_data.iloc[n,0], format='%Y-%m-%d'))
        if match_no is not None: # インデックス日付にマッチするならリストに格納
            ex_x2.iat[match_no,0]=ex_data.iloc[n,33]
            ex_x2.iat[match_no,1]=ex_data.iloc[n,58]
    except KeyError: # 為替リストと、株価中心リストのindexが合わなければスキップ
        # print("skip:"+str(ex_data.iloc[n,0]))
        continue

# matplotlibで描画
#fig, (ax1, ax2) = plt.subplots(2,1, gridspec_kw = {'height_ratios':[3, 1]}) # 2種類
fig, (ax1, ax2, ax3) = plt.subplots(3,1, sharex='col', gridspec_kw = {'height_ratios':[3, 1,1]}) # 3種類

ax1.plot(x, y, color="blue", linewidth=1, linestyle="-")
ax1.plot(x, sma25, color="g", linewidth=1, linestyle="-", label="SMA25")
ax1.plot(x, sma75, color="r", linewidth=1, linestyle="-", label="SMA75")

ax2.plot(x, macd, color="b", linewidth=1, linestyle="-", label="MACD")
ax2.plot(x, macd_signal, color="g", linewidth=1, linestyle="-", label="SIGNAL")

# 為替も表示
ax3.plot(x, ex_x2.iloc[:,0], color="b", linewidth=1, linestyle="-", label="YEN")
ax3.plot(x, ex_x2.iloc[:,1], color="g", linewidth=1, linestyle="-", label="DOLLER")


#plt.xlabel("Year-Month", fontsize=14, fontname='Times New Roman') # x軸のタイトル
#plt.ylabel("Stock price", fontsize=14, fontname='Times New Roman') # y軸のタイトル
#plt.legend(loc="best")

fig.suptitle(str(stockname)+"("+str(code)+")", fontsize=16) # グラフタイトル
fig.tight_layout()
plt.subplots_adjust(top=0.9)
plt.show()



■seleniumドル円ダウンロード
https://www.bis.org/statistics/eer.htm

#import chromedriver_binary
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
driver = webdriver.Chrome()

def download_exchange_csv():
    try:
        url = 'https://www.bis.org/statistics/eer.htm'
        driver.get(url)
        element = driver.find_elements_by_link_text('CSV vertical')
        element[0].click()
        time.sleep(3)
    except NoSuchElementException:
        print("no data")
    pass

time.sleep(3)

download_exchange_csv()


■為替処理
import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams

os.chdir("C:\\Users\\piror\\Downloads") #ファイルの場所を指定，先にデータを入れておく
#4行：国 6行目：1983/10/3からの日付 L:CN 11 AH:JP 33 AI:KR 34 BG:US 58

ex_file_name = 'full_webstats_eer_d_dataflow_csv_row.zip' #ファイル名を指定
ex_data = pd.read_csv(path + ex_file_name, header=3, encoding='cp932')

ex_data = ex_data.drop(0, axis=0) #余計な先頭行を削除 ちゃんと結果を入れてあげないと更新できないので注意
ex_data = ex_data.dropna(how='any', axis=0) #nanを含む行を削除 ちゃんと結果を入れてあげないと更新できないので注意

ex_x = []
ex2_x = []
ex_yen = []
ex2_yen = []
ex_doller = []
ex2_doller = []

ex_x = list(pd.to_datetime(ex_data.iloc[:,0], format='%Y-%m-%d'))

ex_temp = list(ex_data.iloc[:,33])
ex_yen += ex_temp[::]

ex_temp = list(ex_data.iloc[:,58])
ex_doller += ex_temp[::]

for n in range(len(x)): # 株価配列を元に、日付をマッチさせてその日付の為替を取得、リスト化する
    match_no = ex_x.index(x[n])
    ex2_x.append(ex_x[match_no])
    ex2_yen.append(ex_yen[match_no])
    ex2_doller.append(ex_doller[match_no])

■株価の相関

import os
import pandas as pd
import ntpath
from glob import glob

# os.chdir("C:\\Users\\piror\\Downloads") #ファイルの場所を指定，先にデータを入れておく
path = "C:\\Users\\piror\\Downloads\\"
codes = []
files = glob(path+"[0-9][0-9][0-9][0-9]*_2019.csv")
print(files) # ['mydir/aa.txt', 'mydir/cc.txt']

for file in range(len(files)):
    codes.append(ntpath.split(files[file])[1].split("_")[0])


start_code = codes[0]
start = 2019
# end = 2019

x = []
y = []

# 名称の作成、配列の準備
file_name = str(start_code)+'_%d.csv' %start #ファイル名を指定
firstline = list(pd.read_csv(path + file_name, nrows=1,encoding='cp932'))
stockname = firstline[0]
data = pd.read_csv(path + file_name, header=1,encoding='cp932')
a =list(pd.to_datetime(data.iloc[:,0], format='%Y-%m-%d'))
x += a[::] 
b = list(data.iloc[:,4])
y += b[::]

# 株価個別ファイルを読み込んで配列に格納
corr_list = pd.DataFrame(x)#DataFrameに変換
corr_list2 = corr_list.set_index([0]) #1銘柄目の日付をインデックスに設定する

for code in codes:
    corr_list2 = corr_list2.assign(code=0)
    dic = {'code':code}
    corr_list2 = corr_list2.rename(columns=dic)
    if code != codes[0]: #2銘柄目からはファイルを読み込む
        file_name = str(code)+'_%d.csv' %start #ファイル名を指定
        data = pd.read_csv(path + file_name, header=1,encoding='cp932')
    for n in range(len(data)): # 株価配列を元に、日付をマッチさせてその日付の為替をセットする
        match_no = corr_list2.index.get_loc(pd.to_datetime(data.iloc[n,0], format='%Y-%m-%d'))
        if match_no is not None: # インデックス日付にマッチするならリストに格納
            # print("code:"+code+" n:"+str(n)+" match_no:"+str(match_no))
            corr_list2.iat[match_no,corr_list2.columns.get_loc(code)]=data.iloc[n,1] # debugged

# 銘柄間の相関係数を計算
result = corr_list2.corr()

# 条件を超えるものを表示
result_corr_high = result[(result>0.98)&(result!=1.0)]

# 条件を下回るものを表示
result_corr_low = result[(result<-0.9)&(result!=1.0)]

---------------------------一つ前のソースです
# ソース汚いけど、ペアをリストできた
# corr_pair_high = []
# for rows in range(len(result_corr_high.index)): #行毎ループ
#     for cols in range(len(result_corr_high.columns)): #列ごとループ
#         if result_corr_high.isnull().iat[rows,cols] != True: #nullでない場合
#             temp_pair_high = [result_corr_high.index[rows],result_corr_high.columns[cols]]
#             temp_pair_high.sort()
#             print(temp_pair_high)
#             if temp_pair_high not in corr_pair_high: #重複がないか確認してからinsert
#                 corr_pair_high.append(temp_pair_high)
#                 print("insert"+str(temp_pair_high))
#                 # print(result_corr_high.index[rows],result_corr_high.columns[cols])
---------------------------test

def calc_unique_pair(result_corr): #配列渡しに特別な表記は不要だった
    corr_pair = []
    for rows in range(len(result_corr.index)): #行毎ループ
        for cols in range(len(result_corr.columns)): #列ごとループ
            if result_corr.isnull().iat[rows,cols] != True: #nullでない場合
                temp_pair = [result_corr.index[rows],result_corr.columns[cols]]
                temp_pair.sort()
                print(temp_pair)
                if temp_pair not in corr_pair: #重複がないか確認してからinsert
                    corr_pair.append(temp_pair)
                    print("insert"+str(temp_pair))
                    # print(result_corr.index[rows],result_corr.columns[cols])
    return corr_pair

#相関があるもの
corr_pair_high = []

corr_pair_high = calc_unique_pair(result_corr_high)

#逆相関があるもの 実際はファーストリテイリングだらけになったので、地合いの方が影響が大きい様子
corr_pair_low = []

corr_pair_low = calc_unique_pair(result_corr_low)

■ボリンジャーバンド
# ボリンジャーバンドの計算
bband = pd.DataFrame()
bband['close'] = buy_1min_s['close']
bband['mean'] = buy_1min_s['close'].rolling(window=20).mean()
bband['std'] = buy_1min_s['close'].rolling(window=20).std()
bband['upper'] = bband['mean'] + (bband['std'] * 2) # 1,3もこの数値変更で修正可能
bband['lower'] = bband['mean'] - (bband['std'] * 2) # 1,3もこの数値変更で修正可能

■ＲＳＩ
# RSI = 期間中の値上がり幅 ÷ （期間中の値上がり幅 + 値下がり幅）x 100% 

# データセットから終値のみ切り出して差分を計算
close = buy_1min_l['close']
diff = close.diff()

Python
# 終値の最初の10行
close[0:10]

# 差分の最初の10行
diff[0:10]

# 最初のレコードが欠損してしまうので落としてあげる
diff = diff[1:]

# 値上がり幅、値下がり幅をシリーズへ切り分け
up, down = diff.copy(), diff.copy()
up[up < 0] = 0
down[down > 0] = 0

# 値上がり幅/値下がり幅の単純移動平均（14)を処理
up_sma_14 = up.rolling(window=14, center=False).mean()
down_sma_14 = down.abs().rolling(window=14, center=False).mean()

# RSIの計算
RS = up_sma_14 / down_sma_14
RSI = 100.0 - (100.0 / (1.0 + RS))

■スローストキャスティクス
def STOK(close, low, high, n): 
    STOK = ((close - low.rolling(window=n, center=False).min()) / ( high.rolling(window=n,center=False).max() - low.rolling(window=n,center=False).min())) * 100
    return STOK
 
# ストキャスの%Dを計算（%Kの3日SMA）
def STOD(close, low, high, n):
    STOK = ((close - low.rolling(window=n, center=False).min()) / (high.rolling(window=n, center=False).max() - low.rolling(window=n, center=False).min())) * 100
    STOD = STOK.rolling(window=3,center=False).mean()
    return STOD
 
# ストキャスの%SDを計算（%Dの3日SMA）
def STOSD(close, low, high, n):
    STOK = ((close - low.rolling(window=n, center=False).min()) / (high.rolling(window=n, center=False).max() - low.rolling(window=n, center=False).min())) * 100
    STOD = STOK.rolling(window=3,center=False).mean()
    STOSD = STOD.rolling(window=3, center=False).mean()    
    return STOSD

■マルチスレッド株価ダウンロード（３並列）

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import threading

driver1 = webdriver.Chrome()
driver2 = webdriver.Chrome()
driver3 = webdriver.Chrome()

def download_stock_csv(code_range,year_range,driver):
    for code in code_range:
        try:
            for year in year_range:
                url = 'https://kabuoji3.com/stock/{0}/{1}/'.format(code,year)
                driver.get(url)
 
                try:
                    driver.find_element_by_name("csv").click()
                    time.sleep(3)
                    driver.find_element_by_name("csv").click()
                except NoSuchElementException:
                    print("no data:"+str(code)+" year:"+str(year))
                    pass
                time.sleep(1)
 	
        except NoSuchElementException:
            print("no data:"+str(code)+" year:"+str(year))
        pass
    time.sleep(3)

# jp_225 = [1332,1333,1605,1721,1801,1802,1803,1808,1812,1925,1928,1963,2002,2269,2282,2432,2501,2502,2503,2531,2768,2801,2802,2871,2914,3086,3099,3101,3103,3105,3289,3382,3401,3402,3405,3407,3436,3861,3863,4004,4005,4021,4042,4043,4061,4063,4151,4183,4188,4208,4272,4324,4452,4502,4503,4506,4507,4519,4523,4543,4568,4578,4631,4689,4704,4751,4755,4901,4902,4911,5019,5020,5101,5108,5201,5202,5214,5232,5233,5301,5332,5333,5401,5406,5411,5541,5631,5703,5706,5707,5711,5713,5714,5801,5802,5803,5901,6098,6103,6113,6178,6301,6302,6305,6326,6361,6366,6367,6471,6472,6473,6479,6501,6503,6504,6506,6645,6674,6701,6702,6703,6724,6752,6758,6762,6770,6841,6857,6902,6952,6954,6971,6976,6988,7003,7004,7011,7012,7013,7186,7201,7202,7203,7205,7211,7261,7267,7269,7270,7272,7731,7733,7735,7751,7752,7762,7911,7912,7951,8001,8002,8015,8028,8031,8035,8053,8058,8233,8252,8253,8267,8303,8304,8306,8308,8309,8316,8331,8354,8355,8411,8601,8604,8628,8630,8725,8729,8750,8766,8795,8801,8802,8804,8830,9001,9005,9007,9008,9009,9020,9021,9022,9062,9064,9101,9104,9107,9202,9301,9412,9432,9433,9437,9501,9502,9503,9531,9532,9602,9613,9681,9735,9766,9983,9984]

jp_225_1 = [1332,1333,1605,1721,1801,1802,1803,1808,1812,1925,1928,1963,2002,2269,2282,2432,2501,2502,2503,2531,2768,2801,2802,2871,2914,3086,3099,3101,3103,3105,3289,3382,3401,3402,3405,3407,3436,3861,3863,4004,4005,4021,4042,4043,4061,4063,4151,4183,4188,4208,4272,4324,4452,4502,4503,4506,4507,4519,4523,4543,4568,4578,4631,4689,4704,4751,4755,4901,4902,4911,5019,5020,5101,5108,5201,5202,5214,5232,5233,5301,5332,5333,5401,5406,5411,5541,5631,5703,5706]
jp_225_2 = [5707,5711,5713,5714,5801,5802,5803,5901,6098,6103,6113,6178,6301,6302,6305,6326,6361,6366,6367,6471,6472,6473,6479,6501,6503,6504,6506,6645,6674,6701,6702,6703,6724,6752,6758,6762,6770,6841,6857,6902,6952,6954,6971,6976,6988,7003,7004,7011,7012,7013,7186,7201,7202,7203,7205,7211,7261,7267,7269,7270,7272,7731,7733,7735,7751,7752,7762,7911,7912]
jp_225_3 = [7951,8001,8002,8015,8028,8031,8035,8053,8058,8233,8252,8253,8267,8303,8304,8306,8308,8309,8316,8331,8354,8355,8411,8601,8604,8628,8630,8725,8729,8750,8766,8795,8801,8802,8804,8830,9001,9005,9007,9008,9009,9020,9021,9022,9062,9064,9101,9104,9107,9202,9301,9412,9432,9433,9437,9501,9502,9503,9531,9532,9602,9613,9681,9735,9766,9983,9984]

def download1(self,*stock_code):
    download_stock_csv(stock_code,range(2019,2020),driver1)
    print("download1 end")

def download2(self,*stock_code):
    download_stock_csv(stock_code,range(2019,2020),driver2)
    print("download2 end")

def download3(self,*stock_code):
    download_stock_csv(stock_code,range(2019,2020),driver3)
    print("download2 end")

th_me1 = threading.Thread(target=download1, name="download1", args=jp_225_1)
th_me1.start()
th_me2 = threading.Thread(target=download2, name="download2", args=jp_225_2)
th_me2.start()
th_me3 = threading.Thread(target=download3, name="download3", args=jp_225_3)
th_me3.start()

print("process kick end")

# test start 13:52 to 15:00 約70分