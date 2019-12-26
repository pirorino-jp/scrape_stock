# ���̂܂܎��s���Ă������܂���

��selenium�e�X�g

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

��selenium�����_�E�����[�h

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

# �e��ݒ�
## �擾���������t�����W�̎w��
start = datetime.datetime(2018, 1, 1)
end = datetime.datetime(2019, 8, 1)

# �擾��������Ђ̃e�B�b�N�V���{�����L�ڂ��܂��B
## �Ⴆ�΂̕��c��i�H�Ƃ̏ꍇ�@TSE/4502 �ƂȂ�܂��B
## https://www.quandl.com/data/TSE/4502-Takeda-Pharmaceutical-Co-Ltd-4502
company_id = 'TSE/4502'

# API�L�[�̐ݒ�
quandl.ApiConfig.api_key = 'xxx'

# �f�[�^�擾
df = quandl.get(company_id) # �����łł�2017�N�I���܂ł������܂���

-----------------------------------
��matplotlib�Ŏg����t�H���g�̊m�F
import matplotlib.font_manager as fm
fm.findSystemFonts()

import matplotlib as mpl
mpl.matplotlib_fname()
'D:\\projects\\pyeprog\\env\\Lib\\site-packages\\matplotlib\\mpl-data\\matplotlibrc'


matplotlib.font_manager._rebuild()


pip install --upgrade matplotlib


��pandas��������

import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams

#os.chdir("C:\\Users\\piror\\Downloads") #�t�@�C���̏ꏊ���w��C��Ƀf�[�^�����Ă���
path = "C:\\Users\\piror\\Downloads\\"

plt.rcParams['figure.figsize'] = [10, 5]
plt.rcParams['xtick.direction'] = 'in'#x���̖ڐ�����������('in')���O����('out')���o������('inout')
plt.rcParams['ytick.direction'] = 'in'#y���̖ڐ�����������('in')���O����('out')���o������('inout')
plt.rcParams['xtick.major.width'] = 1.0 #x����ڐ�����̐���
plt.rcParams['ytick.major.width'] = 1.0 #y����ڐ�����̐���
plt.rcParams['font.size'] = 12 #�t�H���g�̑傫��
plt.rcParams['axes.linewidth'] = 1.0 # ���̐���edge linewidth�B�݂͂̑���
plt.rcParams['font.family'] = 'sans-serif' #�g�p����t�H���g��
plt.rcParams['font.sans-serif'] = ['Hiragino Maru Gothic Pro', 'Yu Gothic', 'Meirio', 'Takao', 'IPAexGothic', 'IPAPGothic', 'Noto Sans CJK JP']

code = 8729
start = 2019
end = 2020

x = []
y = []

for n in range (start, end):
    file_name = str(code)+'_%d.csv' %n #�t�@�C�������w��
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

# �ב�
ex_file_name = 'full_webstats_eer_d_dataflow_csv_row.zip' #�t�@�C�������w��
try:
    ex_data = pd.read_csv(path + ex_file_name, header=3, encoding='cp932')
except FileNotFoundError:
    print("File not found:"+file_name)
    sys.exit


z = pd.DataFrame(y)#DataFrame�ɕϊ�
sma75 = pd.DataFrame.rolling(z, window=75,center=False).mean()
sma25 = pd.DataFrame.rolling(z, window=25,center=False).mean()

# MACD�̌v�Z���s��
ema12 = pd.DataFrame.rolling(z, window=12,center=False).mean()
ema26 = pd.DataFrame.rolling(z, window=26,center=False).mean()
macd = pd.DataFrame()
macd = ema12 - ema26
macd_signal = macd.ewm(span=9).mean()
# macd.head()

# �בւ̌v�Z

ex_data = ex_data.drop(0, axis=0) #�]�v�Ȑ擪�s���폜 �����ƌ��ʂ����Ă����Ȃ��ƍX�V�ł��Ȃ��̂Œ���
ex_data = ex_data.dropna(how='any', axis=0) #nan���܂ލs���폜 �����ƌ��ʂ����Ă����Ȃ��ƍX�V�ł��Ȃ��̂Œ���

ex_x = pd.DataFrame(x)#DataFrame�ɕϊ�
ex_x2 = ex_x.set_index([0]) #1�����ڂ̓��t���C���f�b�N�X�ɐݒ肷��
ex_x2 = ex_x2.assign(yen=None) # �~�̗�ǉ�
ex_x2 = ex_x2.assign(doller=None) # �h���̗�ǉ�

for n in range(len(ex_data)): # �����z������ɁA���t���}�b�`�����Ă��̓��t�̈בւ��擾�A���X�g������
    # print(n)
    try:
        match_no = ex_x2.index.get_loc(pd.to_datetime(ex_data.iloc[n,0], format='%Y-%m-%d'))
        if match_no is not None: # �C���f�b�N�X���t�Ƀ}�b�`����Ȃ烊�X�g�Ɋi�[
            ex_x2.iat[match_no,0]=ex_data.iloc[n,33]
            ex_x2.iat[match_no,1]=ex_data.iloc[n,58]
    except KeyError: # �בփ��X�g�ƁA�������S���X�g��index������Ȃ���΃X�L�b�v
        # print("skip:"+str(ex_data.iloc[n,0]))
        continue

# matplotlib�ŕ`��
#fig, (ax1, ax2) = plt.subplots(2,1, gridspec_kw = {'height_ratios':[3, 1]}) # 2���
fig, (ax1, ax2, ax3) = plt.subplots(3,1, sharex='col', gridspec_kw = {'height_ratios':[3, 1,1]}) # 3���

ax1.plot(x, y, color="blue", linewidth=1, linestyle="-")
ax1.plot(x, sma25, color="g", linewidth=1, linestyle="-", label="SMA25")
ax1.plot(x, sma75, color="r", linewidth=1, linestyle="-", label="SMA75")

ax2.plot(x, macd, color="b", linewidth=1, linestyle="-", label="MACD")
ax2.plot(x, macd_signal, color="g", linewidth=1, linestyle="-", label="SIGNAL")

# �בւ��\��
ax3.plot(x, ex_x2.iloc[:,0], color="b", linewidth=1, linestyle="-", label="YEN")
ax3.plot(x, ex_x2.iloc[:,1], color="g", linewidth=1, linestyle="-", label="DOLLER")


#plt.xlabel("Year-Month", fontsize=14, fontname='Times New Roman') # x���̃^�C�g��
#plt.ylabel("Stock price", fontsize=14, fontname='Times New Roman') # y���̃^�C�g��
#plt.legend(loc="best")

fig.suptitle(str(stockname)+"("+str(code)+")", fontsize=16) # �O���t�^�C�g��
fig.tight_layout()
plt.subplots_adjust(top=0.9)
plt.show()



��selenium�h���~�_�E�����[�h
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


���ב֏���
import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams

os.chdir("C:\\Users\\piror\\Downloads") #�t�@�C���̏ꏊ���w��C��Ƀf�[�^�����Ă���
#4�s�F�� 6�s�ځF1983/10/3����̓��t L:CN 11 AH:JP 33 AI:KR 34 BG:US 58

ex_file_name = 'full_webstats_eer_d_dataflow_csv_row.zip' #�t�@�C�������w��
ex_data = pd.read_csv(path + ex_file_name, header=3, encoding='cp932')

ex_data = ex_data.drop(0, axis=0) #�]�v�Ȑ擪�s���폜 �����ƌ��ʂ����Ă����Ȃ��ƍX�V�ł��Ȃ��̂Œ���
ex_data = ex_data.dropna(how='any', axis=0) #nan���܂ލs���폜 �����ƌ��ʂ����Ă����Ȃ��ƍX�V�ł��Ȃ��̂Œ���

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

for n in range(len(x)): # �����z������ɁA���t���}�b�`�����Ă��̓��t�̈בւ��擾�A���X�g������
    match_no = ex_x.index(x[n])
    ex2_x.append(ex_x[match_no])
    ex2_yen.append(ex_yen[match_no])
    ex2_doller.append(ex_doller[match_no])

�������̑���

import os
import pandas as pd
import ntpath
from glob import glob

# os.chdir("C:\\Users\\piror\\Downloads") #�t�@�C���̏ꏊ���w��C��Ƀf�[�^�����Ă���
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

# ���̂̍쐬�A�z��̏���
file_name = str(start_code)+'_%d.csv' %start #�t�@�C�������w��
firstline = list(pd.read_csv(path + file_name, nrows=1,encoding='cp932'))
stockname = firstline[0]
data = pd.read_csv(path + file_name, header=1,encoding='cp932')
a =list(pd.to_datetime(data.iloc[:,0], format='%Y-%m-%d'))
x += a[::] 
b = list(data.iloc[:,4])
y += b[::]

# �����ʃt�@�C����ǂݍ���Ŕz��Ɋi�[
corr_list = pd.DataFrame(x)#DataFrame�ɕϊ�
corr_list2 = corr_list.set_index([0]) #1�����ڂ̓��t���C���f�b�N�X�ɐݒ肷��

for code in codes:
    corr_list2 = corr_list2.assign(code=0)
    dic = {'code':code}
    corr_list2 = corr_list2.rename(columns=dic)
    if code != codes[0]: #2�����ڂ���̓t�@�C����ǂݍ���
        file_name = str(code)+'_%d.csv' %start #�t�@�C�������w��
        data = pd.read_csv(path + file_name, header=1,encoding='cp932')
    for n in range(len(data)): # �����z������ɁA���t���}�b�`�����Ă��̓��t�̈בւ��Z�b�g����
        match_no = corr_list2.index.get_loc(pd.to_datetime(data.iloc[n,0], format='%Y-%m-%d'))
        if match_no is not None: # �C���f�b�N�X���t�Ƀ}�b�`����Ȃ烊�X�g�Ɋi�[
            # print("code:"+code+" n:"+str(n)+" match_no:"+str(match_no))
            corr_list2.iat[match_no,corr_list2.columns.get_loc(code)]=data.iloc[n,1] # debugged

# �����Ԃ̑��֌W�����v�Z
result = corr_list2.corr()

# �����𒴂�����̂�\��
result_corr_high = result[(result>0.98)&(result!=1.0)]

# �������������̂�\��
result_corr_low = result[(result<-0.9)&(result!=1.0)]

---------------------------��O�̃\�[�X�ł�
# �\�[�X�������ǁA�y�A�����X�g�ł���
# corr_pair_high = []
# for rows in range(len(result_corr_high.index)): #�s�����[�v
#     for cols in range(len(result_corr_high.columns)): #�񂲂ƃ��[�v
#         if result_corr_high.isnull().iat[rows,cols] != True: #null�łȂ��ꍇ
#             temp_pair_high = [result_corr_high.index[rows],result_corr_high.columns[cols]]
#             temp_pair_high.sort()
#             print(temp_pair_high)
#             if temp_pair_high not in corr_pair_high: #�d�����Ȃ����m�F���Ă���insert
#                 corr_pair_high.append(temp_pair_high)
#                 print("insert"+str(temp_pair_high))
#                 # print(result_corr_high.index[rows],result_corr_high.columns[cols])
---------------------------test

def calc_unique_pair(result_corr): #�z��n���ɓ��ʂȕ\�L�͕s�v������
    corr_pair = []
    for rows in range(len(result_corr.index)): #�s�����[�v
        for cols in range(len(result_corr.columns)): #�񂲂ƃ��[�v
            if result_corr.isnull().iat[rows,cols] != True: #null�łȂ��ꍇ
                temp_pair = [result_corr.index[rows],result_corr.columns[cols]]
                temp_pair.sort()
                print(temp_pair)
                if temp_pair not in corr_pair: #�d�����Ȃ����m�F���Ă���insert
                    corr_pair.append(temp_pair)
                    print("insert"+str(temp_pair))
                    # print(result_corr.index[rows],result_corr.columns[cols])
    return corr_pair

#���ւ��������
corr_pair_high = []

corr_pair_high = calc_unique_pair(result_corr_high)

#�t���ւ�������� ���ۂ̓t�@�[�X�g���e�C�����O���炯�ɂȂ����̂ŁA�n�����̕����e�����傫���l�q
corr_pair_low = []

corr_pair_low = calc_unique_pair(result_corr_low)

���{�����W���[�o���h
# �{�����W���[�o���h�̌v�Z
bband = pd.DataFrame()
bband['close'] = buy_1min_s['close']
bband['mean'] = buy_1min_s['close'].rolling(window=20).mean()
bband['std'] = buy_1min_s['close'].rolling(window=20).std()
bband['upper'] = bband['mean'] + (bband['std'] * 2) # 1,3�����̐��l�ύX�ŏC���\
bband['lower'] = bband['mean'] - (bband['std'] * 2) # 1,3�����̐��l�ύX�ŏC���\

���q�r�h
# RSI = ���Ԓ��̒l�オ�蕝 �� �i���Ԓ��̒l�オ�蕝 + �l�����蕝�jx 100% 

# �f�[�^�Z�b�g����I�l�̂ݐ؂�o���č������v�Z
close = buy_1min_l['close']
diff = close.diff()

Python
# �I�l�̍ŏ���10�s
close[0:10]

# �����̍ŏ���10�s
diff[0:10]

# �ŏ��̃��R�[�h���������Ă��܂��̂ŗ��Ƃ��Ă�����
diff = diff[1:]

# �l�オ�蕝�A�l�����蕝���V���[�Y�֐؂蕪��
up, down = diff.copy(), diff.copy()
up[up < 0] = 0
down[down > 0] = 0

# �l�オ�蕝/�l�����蕝�̒P���ړ����ρi14)������
up_sma_14 = up.rolling(window=14, center=False).mean()
down_sma_14 = down.abs().rolling(window=14, center=False).mean()

# RSI�̌v�Z
RS = up_sma_14 / down_sma_14
RSI = 100.0 - (100.0 / (1.0 + RS))

���X���[�X�g�L���X�e�B�N�X
def STOK(close, low, high, n): 
    STOK = ((close - low.rolling(window=n, center=False).min()) / ( high.rolling(window=n,center=False).max() - low.rolling(window=n,center=False).min())) * 100
    return STOK
 
# �X�g�L���X��%D���v�Z�i%K��3��SMA�j
def STOD(close, low, high, n):
    STOK = ((close - low.rolling(window=n, center=False).min()) / (high.rolling(window=n, center=False).max() - low.rolling(window=n, center=False).min())) * 100
    STOD = STOK.rolling(window=3,center=False).mean()
    return STOD
 
# �X�g�L���X��%SD���v�Z�i%D��3��SMA�j
def STOSD(close, low, high, n):
    STOK = ((close - low.rolling(window=n, center=False).min()) / (high.rolling(window=n, center=False).max() - low.rolling(window=n, center=False).min())) * 100
    STOD = STOK.rolling(window=3,center=False).mean()
    STOSD = STOD.rolling(window=3, center=False).mean()    
    return STOSD

���}���`�X���b�h�����_�E�����[�h�i�R����j

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

# test start 13:52 to 15:00 ��70��