import pandas as pd
import os
inputdir=r'C:\Users\廖勗宏\Desktop\test\空氣品質監測資料'#要合的資料夾路徑(要改)
location = 'pm25_all2'#哪裡(要改)
#df_empty=pd.DataFrame(columns=["ObsTime","StnPres","SeaPres","StnPresMax","StnPresMaxTime","StnPresMin","StnPresMinTime","Temperature","T Max","T Max Time","T Min","T Min Time","Td dew point","RH","RHMin","RHMinTime","WS","WD","WSGust","WDGust","WGustTime","Precp","PrecpHour","PrecpMax10","PrecpMax10Time","PrecpHrMax","PrecpHrMaxTime","SunShine","SunShineRate","GloblRad","VisbMean","EvapA","UVI Max","UVI Max Time","Cloud Amount"])
c = ['year','month','day','hour','AMB_TEMP','CH4','CO','NMHC','NO','NO2','NOx','O3','PH_RAIN','PM10','PM2.5','RAINFALL','RAIN_COND','RH','SO2','THC','UVB','WD_HR','WIND_DIREC','WIND_SPEED','WS_HR']
'''
['ObsTimeMonth1_tsub10',
 'ObsTimeDay2_tsub10',
 'StnPres3_tsub10',
 'Temperature4_tsub10',
 'T Max5_tsub10',
 'T Min6_tsub10',
 'RH7_tsub10',
 'WS8_tsub10',
 'WD9_tsub10',
 'Precp10_tsub10',
 'SunShine11_tsub10',
 'latitude12_tsub10',
 'altitude13_tsub10',
 'ObsTimeMonth1_tsub9',
 'ObsTimeDay2_tsub9',
 'StnPres3_tsub9',
 'Temperature4_tsub9',
 'T Max5_tsub9',
 'T Min6_tsub9',
 'RH7_tsub9',
 'WS8_tsub9',
 'WD9_tsub9',
 'Precp10_tsub9',
 'SunShine11_tsub9',
 'latitude12_tsub9',
 'altitude13_tsub9',
 'ObsTimeMonth1_tsub8',
 'ObsTimeDay2_tsub8',
 'StnPres3_tsub8',
 'Temperature4_tsub8',
 'T Max5_tsub8',
 'T Min6_tsub8',
 'RH7_tsub8',
 'WS8_tsub8',
 'WD9_tsub8',
 'Precp10_tsub8',
 'SunShine11_tsub8',
 'latitude12_tsub8',
 'altitude13_tsub8',
 'ObsTimeMonth1_tsub7',
 'ObsTimeDay2_tsub7',
 'StnPres3_tsub7',
 'Temperature4_tsub7',
 'T Max5_tsub7',
 'T Min6_tsub7',
 'RH7_tsub7',
 'WS8_tsub7',
 'WD9_tsub7',
 'Precp10_tsub7',
 'SunShine11_tsub7',
 'latitude12_tsub7',
 'altitude13_tsub7',
 'ObsTimeMonth1_tsub6',
 'ObsTimeDay2_tsub6',
 'StnPres3_tsub6',
 'Temperature4_tsub6',
 'T Max5_tsub6',
 'T Min6_tsub6',
 'RH7_tsub6',
 'WS8_tsub6',
 'WD9_tsub6',
 'Precp10_tsub6',
 'SunShine11_tsub6',
 'latitude12_tsub6',
 'altitude13_tsub6',
 'ObsTimeMonth1_tsub5',
 'ObsTimeDay2_tsub5',
 'StnPres3_tsub5',
 'Temperature4_tsub5',
 'T Max5_tsub5',
 'T Min6_tsub5',
 'RH7_tsub5',
 'WS8_tsub5',
 'WD9_tsub5',
 'Precp10_tsub5',
 'SunShine11_tsub5',
 'latitude12_tsub5',
 'altitude13_tsub5',
 'ObsTimeMonth1_tsub4',
 'ObsTimeDay2_tsub4',
 'StnPres3_tsub4',
 'Temperature4_tsub4',
 'T Max5_tsub4',
 'T Min6_tsub4',
 'RH7_tsub4',
 'WS8_tsub4',
 'WD9_tsub4',
 'Precp10_tsub4',
 'SunShine11_tsub4',
 'latitude12_tsub4',
 'altitude13_tsub4',
 'ObsTimeMonth1_tsub3',
 'ObsTimeDay2_tsub3',
 'StnPres3_tsub3',
 'Temperature4_tsub3',
 'T Max5_tsub3',
 'T Min6_tsub3',
 'RH7_tsub3',
 'WS8_tsub3',
 'WD9_tsub3',
 'Precp10_tsub3',
 'SunShine11_tsub3',
 'latitude12_tsub3',
 'altitude13_tsub3',
 'ObsTimeMonth1_tsub2',
 'ObsTimeDay2_tsub2',
 'StnPres3_tsub2',
 'Temperature4_tsub2',
 'T Max5_tsub2',
 'T Min6_tsub2',
 'RH7_tsub2',
 'WS8_tsub2',
 'WD9_tsub2',
 'Precp10_tsub2',
 'SunShine11_tsub2',
 'latitude12_tsub2',
 'altitude13_tsub2',
 'ObsTimeMonth1_tsub1',
 'ObsTimeDay2_tsub1',
 'StnPres3_tsub1',
 'Temperature4_tsub1',
 'T Max5_tsub1',
 'T Min6_tsub1',
 'RH7_tsub1',
 'WS8_tsub1',
 'WD9_tsub1',
 'Precp10_tsub1',
 'SunShine11_tsub1',
 'latitude12_tsub1',
 'altitude13_tsub1',
 'ObsTimeMonth1(t)',
 'ObsTimeDay2(t)',
 'StnPres3(t)',
 'Temperature4(t)',
 'T Max5(t)',
 'T Min6(t)',
 'RH7(t)',
 'WS8(t)',
 'WD9(t)',
 'Precp10(t)',
 'SunShine11(t)',
 'latitude12(t)',
 'altitude13(t)']
'''
df_empty=pd.DataFrame(columns= c)
for parents, dirnames, filenames in os.walk(inputdir):
    for filename in filenames:
        df=pd.read_csv(os.path.join(parents,filename),engine = 'python',index_col=0)
        df_empty=df_empty.append(df,ignore_index=True,sort=False)
df_empty.to_csv(location + '.csv',encoding="utf_8_sig", index=False)