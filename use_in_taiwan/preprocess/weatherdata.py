from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Chrome() 
for i in range(2010,2019):
    for j in range(1,13):
        year = str(i)
        if j < 10:
            month = '0'+str(j)
        else:
            month = str(j)
        driver.get('https://e-service.cwb.gov.tw/HistoryDataQuery/MonthDataController.do?command=viewMain&station=467060&stname=%25E8%2598%2587%25E6%25BE%25B3&datepicker='+year+'-'+month+'#')
        try:
            driver.find_element_by_xpath("//a[@id='downloadCSV']").click()
        except:
            print('hurry up!'+year+month)
            time.sleep(3)
        