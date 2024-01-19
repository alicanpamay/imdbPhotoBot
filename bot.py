import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib.request

titleList = ['tt0482571', 'tt0093779', 'tt1305806', 'tt0050976', 'tt0111161', 'tt0081505', 'tt0102926', 'tt0167404', 'tt0070735', 'tt0088247', 'tt0084787', 'tt0041959', 'tt0040897', 'tt0120382', 'tt0114814', 'tt0046268', 'tt0032138', 'tt0993846', 'tt0469494', 'tt5027774', 'tt0056592', 'tt0046438', 'tt0052311', 'tt0114709', 'tt0435761', 'tt0117951', 'tt0105695', 'tt1049413', 'tt0434409', 'tt0052357', 'tt0910970', 'tt1291584', 'tt2582802', 'tt0050986', 'tt3011894', 'tt0051201', 'tt0055630', 'tt5311514']

driver=webdriver.Edge()

title = 213

for i in titleList:
    driver.get('https://www.google.com.tr')
    time.sleep(2)

    searchBar = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea')
    searchBar.send_keys(i)

    searchButton = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]')    
    searchButton.click()
    time.sleep(2)

    gorselButton = driver.find_element(By.XPATH,'/html/body/div[5]/div/div[3]/div/div[1]/div/div[1]/div/div[2]/a')
    gorselButton.click()
    time.sleep(2)

    ilkGorsel = driver.find_element(By.XPATH,'//*[@id="islrg"]/div[1]/div[1]/a[1]/div[1]/img')
    ilkGorsel.click()
    time.sleep(3)

    #img = driver.find_element(By.XPATH,'//*[@id="Sva75c"]/div[2]/div[2]/div[2]/div[2]/c-wiz/div/div/div/div/div[3]/div[1]/a/img[1]')
    src = ilkGorsel.get_attribute('src')
    url = src

    driver.get(url)
    time.sleep(1)
    #driver.save_screenshot(str(title)+".jpeg")
    urllib.request.urlretrieve(url , str(title)+".jpeg")
    time.sleep(1)

    title = title +1