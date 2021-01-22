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
wait2 = WebDriverWait(driver,2)
wait5 = WebDriverWait(driver,5)
wait20 = WebDriverWait(driver,20)
wait60 = WebDriverWait(driver,60)
# 
def google_map_search(url,skeep_page,file_name):
    # url = 'https://www.google.com/maps/search/Health+Food+Stores+near+Regional+Municipality+of+Peel,+ON/@43.6517235,-79.8971072,10z/data=!3m1!4b1'

    driver.get(url)    
    time.sleep(5)
    for i in range(skeep_page):
        try:
            next_page = wait20.until(EC.presence_of_element_located((By.XPATH,'//*[@id="n7lv7yjyC35__section-pagination-button-next"]/img')))
            next_page.click()
            time.sleep(5)
        except:
            time.sleep(2)
            next_page = wait20.until(EC.presence_of_element_located((By.XPATH,'//*[@id="n7lv7yjyC35__section-pagination-button-next"]/img')))
            next_page.click()

    k = True
    while k == True:
        index_i = wait20.until(EC.presence_of_element_located((By.XPATH,'//span[@class="n7lv7yjyC35__left"]/span[1]'))).text
        print(index_i)
        index_i = int(index_i)%20
        print(index_i)
        index_j = wait20.until(EC.presence_of_element_located((By.XPATH,'//span[@class="n7lv7yjyC35__left"]/span[2]'))).text
        print(index_j)
        index_j =int(index_j)%20
        if index_j == 0:
            index_j = 20
        if index_j < 20:
            k = False
            print('stoping execution, k less 20')
        print(index_j)

        for i in range(index_i,index_j+1):
            detail_list = []    
            xpath_details = '//*/div[@class="section-result"][' + str(i) + ']'
            print(xpath_details)      
            try:
                detail = wait60.until(EC.element_to_be_clickable((By.XPATH,xpath_details)))
                detail.click()
            except ElementClickInterceptedException:
                time.sleep(2)
                detail = wait20.until(EC.element_to_be_clickable((By.XPATH,xpath_details)))
                detail.click()
            time.sleep(2)
            # title
            try:
                title = wait20.until(EC.presence_of_element_located((By.XPATH,'//h1[@class="section-hero-header-title-title GLOBAL__gm2-headline-5"]/span[1]'))).text
                print(title)
            except:
                continue
            # 
            try:
                address = wait2.until(EC.presence_of_element_located((By.XPATH,'//img[@src="//www.gstatic.com/images/icons/material/system_gm/1x/place_gm_blue_24dp.png"]/ancestor::node()[@class="ugiz4pqJLAG__content"]/div[2]/div[1]'))).text
            except:
                address = 'adress not available'
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
            # website
            try:
                website = wait2.until(EC.presence_of_element_located((By.XPATH,'//img[@src="//www.gstatic.com/images/icons/material/system_gm/1x/public_gm_blue_24dp.png"]/ancestor::node()[@class="ugiz4pqJLAG__content"]/div[2]/div[1]'))).text
            except:
                website = 'website not available'
            print(website)
            # Phone No.
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
            # review
            try:
                review =  wait2.until(EC.presence_of_element_located((By.XPATH,'//div[@class="section-hero-header-title-description-container"]//span[@class="section-star-display"]'))).text
            except:
                review = 'review not available'
            print(review)
            #review phone number
            try:
                review_number = wait2.until(EC.presence_of_element_located((By.XPATH,'//span[@class="section-rating-term-list"]//button[@class="widget-pane-link"]'))).text
            except:
                review_number = 'not available'
            print(review_number)
            # processing deatails
            detail_list = [title,address,opening_hrs,website,phone,plus_code,review,review_number]
            save_data(detail_list,file_name)
            back_to_results = driver.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/button/span')
            back_to_results.click()
            print('back to results')

        try:
            next_page = wait20.until(EC.presence_of_element_located((By.XPATH,'//*[@id="n7lv7yjyC35__section-pagination-button-next"]/img')))
            next_page.click()
        except:
            k = False

