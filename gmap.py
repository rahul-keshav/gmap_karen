from selenium import webdriver
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from shutil import which
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import random
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException

from basic import save_data

chrome_path = which('chromedriver.exe')
chrome_options = Options()
# chrome_options.add_argument('--headless')
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--disable-geo")
chrome_options.add_argument("start-maximized")
chrome_options.ensure_clean_session = True
# added to disable geo location,
# 0 - Default, 1 - Allow, 2 - Block
prefs = {"profile.default_content_setting_values.geolocation" :2}
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(executable_path = chrome_path,options=chrome_options)
# 
url = 'https://www.google.ca/maps/search/atm+near+me/@46.5844081,-95.1908992,5.08z'
driver.get(url)

wait2 = WebDriverWait(driver,2)
wait5 = WebDriverWait(driver,5)
wait20 = WebDriverWait(driver,20)
time.sleep(5)
for i in range(5):
    for i in range(1,21):
        detail_list = []    
        xpath_details = '//*/div[@class="section-result"][' + str(i) + ']'        
        try:
            detail = wait20.until(EC.element_to_be_clickable((By.XPATH,xpath_details)))
            detail.click()
        except ElementClickInterceptedException:
            time.sleep(2)
            detail = wait20.until(EC.element_to_be_clickable((By.XPATH,xpath_details)))
            detail.click()
        # except:
        #     driver.refresh()
        #     time.sleep(20)
        #     detail = wait20.until(EC.element_to_be_clickable((By.XPATH,xpath_details)))
        #     detail.click()


        time.sleep(2)
        # title
        title = wait20.until(EC.presence_of_element_located((By.XPATH,'//h1[@class="section-hero-header-title-title GLOBAL__gm2-headline-5"]/span[1]'))).text
        print(title)
        address = wait2.until(EC.presence_of_element_located((By.XPATH,'//div[@class="ugiz4pqJLAG__primary-text gm2-body-2"][1]'))).text
        # address
        print(address)
        # opening Hours
        try:
            opening_hrs_ = wait2.until(EC.presence_of_element_located((By.XPATH,'//img[@src="//www.gstatic.com/images/icons/material/system_gm/1x/schedule_gm_blue_24dp.png"]/parent::node()/div/div[@class="cX2WmPgCkHi__primary-text"]/span[@class="cX2WmPgCkHi__section-info-hour-text"]')))
            texts = driver.find_elements_by_xpath('//img[@src="//www.gstatic.com/images/icons/material/system_gm/1x/schedule_gm_blue_24dp.png"]/parent::node()/div/div[@class="cX2WmPgCkHi__primary-text"]/span[@class="cX2WmPgCkHi__section-info-hour-text"]//span')
            opening_hrs = texts[0].text+texts[1].text
            opening_hrs = opening_hrs.encode("windows-1252").decode("utf-8")
        except:
            opening_hrs = 'opening hr not provided'

        print(opening_hrs)
        
        try:
            website = wait2.until(EC.presence_of_element_located((By.XPATH,'//img[@src="//www.gstatic.com/images/icons/material/system_gm/1x/public_gm_blue_24dp.png"]/ancestor::node()[@class="ugiz4pqJLAG__content"]/div[2]/div[1]'))).text
        except:
            website = 'website not available'
        print(website)
        try:
            phone = wait2.until(EC.presence_of_element_located((By.XPATH,'//img[@src="//www.gstatic.com/images/icons/material/system_gm/1x/phone_gm_blue_24dp.png"]/ancestor::node()[@class="ugiz4pqJLAG__content"]/div[2]/div[1]'))).text
        except:
            phone ='Phone not available'
        print(phone)
        try:
            plus_code = wait2.until(EC.presence_of_element_located((By.XPATH,'//img[@src="//maps.gstatic.com/mapfiles/maps_lite/images/2x/ic_plus_code.png"]/ancestor::node()[@class="ugiz4pqJLAG__content"]/div[2]/div[1]'))).text
        except:
            plus_code = 'plus code available'
        print(plus_code)
        
        detail_list = [title,address,opening_hrs,website,phone,plus_code]
        save_data(detail_list)

        back_to_results = driver.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/button/span')
        back_to_results.click()
        print('back to results')

    next_page = wait20.until(EC.presence_of_element_located((By.XPATH,'//*[@id="n7lv7yjyC35__section-pagination-button-next"]/img')))
    next_page.click()

