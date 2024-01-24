import pandas as pd
import os
from selenium.webdriver import Chrome, ChromeOptions
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
import pyodbc
import datetime

browser_options = ChromeOptions()
browser_options.headless = False
driver = Chrome(options=browser_options)

def solar():
    email = "solarweb@leeton.nsw.gov.au"
    password = "Leeton2705$"

    driver.get("https://www.solarweb.com/PvSystems/Widgets")
    driver.find_element("id", "usernameUserInput").send_keys(email)
    driver.find_element("id", "password").send_keys(password)
    driver.find_element("id", "login-button").click()
    WebDriverWait(driver, 100).until(EC.visibility_of_element_located((By.ID, "js-pvsystem-table-id_wrapper")))

    # main URL

    url_1 = "https://www.solarweb.com/PvSystems/PvSystem?pvSystemId=cccdb806-274c-4a21-b406-da78053ae78f"
    url_2 = "https://www.solarweb.com/PvSystems/PvSystem?pvSystemId=03f6c0ec-2edc-431d-a4a1-cea32d81dedb"
    url_3 = "https://www.solarweb.com/PvSystems/PvSystem?pvSystemId=e0267e7a-321b-4bf3-9b5f-eb3c7c25ec94"
    url_4 = "https://www.solarweb.com/PvSystems/PvSystem?pvSystemId=aad57497-4e06-4e7e-b484-5fbb296c9662"
    url_5 = "https://www.solarweb.com/PvSystems/PvSystem?pvSystemId=0527a82e-3629-42db-ac4c-293f16e9c741"
    url_6 = "https://www.solarweb.com/PvSystems/PvSystem?pvSystemId=635b8dbc-9e91-482a-a378-eb49a00c40ef"
    url_7 = "https://www.solarweb.com/PvSystems/PvSystem?pvSystemId=d33e50dd-8e6e-476b-8b4b-d3deb9369678"
    url_8 = "https://www.solarweb.com/PvSystems/PvSystem?pvSystemId=04f01791-9eea-4a59-b182-ee85c89a266e"
    url_9 = "https://www.solarweb.com/PvSystems/PvSystem?pvSystemId=25e266b5-6bbd-4994-a912-ddcab3b6c88b"
    url_10 = "https://www.solarweb.com/PvSystems/PvSystem?pvSystemId=8ac3ec93-b7c7-45c6-a585-22d00b044a5f"
    url_11 = "https://www.solarweb.com/PvSystems/PvSystem?pvSystemId=4a85d0ca-2104-496b-928f-968831cb0f6f"

    url = [url_1, url_2, url_3, url_4, url_5, url_6, url_7, url_8, url_9, url_10, url_11]

    result = {
        "url_1" : {
            "value_1" :  "",
            "value_2" :  "",
            "value_3" :  "",
            "value_4" :  "",
            "value_5" :  "",
            "value_6" :  "",
        },
        "url_2" : {
            "value_1" :  "",
            "value_2" :  "",
            "value_3" :  "",
            "value_4" :  "",
            "value_5" :  "",
            "value_6" :  "",
        },
        "url_3" : {
            "value_1" :  "",
            "value_2" :  "",
            "value_3" :  "",
            "value_4" :  "",
            "value_5" :  "",
            "value_6" :  "",
        },
        "url_4" : {
            "value_1" :  "",
            "value_2" :  "",
            "value_3" :  "",
            "value_4" :  "",
            "value_5" :  "",
            "value_6" :  "",
        },
        "url_5" : {
            "value_1" :  "",
            "value_2" :  "",
            "value_3" :  "",
            "value_4" :  "",
            "value_5" :  "",
            "value_6" :  "",
        },
        "url_6" : {
            "value_1" :  "",
            "value_2" :  "",
            "value_3" :  "",
            "value_4" :  "",
            "value_5" :  "",
            "value_6" :  "",
        },

        "url_7" : {
            "value_1" :  "",
            "value_2" :  "",
            "value_3" :  "",
            "value_4" :  "",
            "value_5" :  "",
            "value_6" :  "",
        },
        "url_8" : {
            "value_1" :  "",
            "value_2" :  "",
            "value_3" :  "",
            "value_4" :  "",
            "value_5" :  "",
            "value_6" :  "",
        },
        "url_9" : {
            "value_1" :  "",
            "value_2" :  "",
            "value_3" :  "",
            "value_4" :  "",
            "value_5" :  "",
            "value_6" :  "",
        },
        "url_10" : {
            "value_1" :  "",
            "value_2" :  "",
            "value_3" :  "",
            "value_4" :  "",
            "value_5" :  "",
            "value_6" :  "",
        },
        "url_11" : {
            "value_1" :  "",
            "value_2" :  "",
            "value_3" :  "",
            "value_4" :  "",
            "value_5" :  "",
            "value_6" :  "",
        }
    }

    for i in range(11):
        driver.get(url[i])

        if i==0:
            if driver.find_element("id", "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll").is_enabled():
                driver.find_element("id", "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll").click()

        result["url_"+str(i+1)]["value_1"] = driver.find_elements(By.CLASS_NAME, 'savings-swiper-value_row')[1].find_element(By.CLASS_NAME, 'savings-value').get_attribute('innerHTML')
        print("value_1", result["url_"+str(i+1)]["value_1"])
        result["url_"+str(i+1)]["value_2"] = driver.find_elements(By.CLASS_NAME, 'savings-swiper-value_row')[0].find_element(By.CLASS_NAME, 'savings-value').get_attribute('innerHTML')
        print("value_2", result["url_"+str(i+1)]["value_2"])
        result["url_"+str(i+1)]["value_3"] = driver.find_elements(By.CLASS_NAME, 'savings-swiper-value_row')[10].find_element(By.CLASS_NAME, 'savings-value').get_attribute('innerHTML')
        print("value_3", result["url_"+str(i+1)]["value_3"])
        result["url_"+str(i+1)]["value_4"] = driver.find_elements(By.CLASS_NAME, 'savings-swiper-value_row')[8].find_element(By.CLASS_NAME, 'savings-value').get_attribute('innerHTML')
        print("value_4", result["url_"+str(i+1)]["value_4"])

        sub_1 = driver.find_elements(By.CLASS_NAME, 'mod-second-level')[2].find_elements(By.CLASS_NAME, 'second-level-nav-element')[3]
        sub_1.click()
        time.sleep(10)

        result["url_"+str(i+1)]["value_5"] = driver.find_elements(By.CLASS_NAME, 'mod-second-level')[2].find_elements(By.TAG_NAME, 'li')[8].find_element(By.CLASS_NAME, 'second-level-nav-element-text').get_attribute('innerHTML')
        print("value_5", result["url_"+str(i+1)]["value_5"])

        sub_2 = driver.find_elements(By.CLASS_NAME,'mod-second-level')[2].find_elements(By.CLASS_NAME, 'second-level-nav-element')[2]
        sub_2.click()
        time.sleep(5)

        result["url_"+str(i+1)]["value_6"] = driver.find_elements(By.CLASS_NAME, 'mod-second-level')[2].find_elements(By.TAG_NAME, 'li')[8].find_element(By.CLASS_NAME, 'second-level-nav-element-text').get_attribute('innerHTML')
        print("value_6", result["url_"+str(i+1)]["value_6"])

        current_time = datetime.datetime.now()
        current_year = str(current_time.year)
        current_month = str(current_time.month)
        current_day = str(current_time.day).zfill(2)

        date = current_year + '/' + current_month + '/' + current_day
        #db_connect

        conn = pyodbc.connect('Driver={SQL Server};' 
                            'Server=DESKTOP-E5FORGP\VE_SERVER;'
                            'Database=scrap;'
                            'Trusted_Connection=yes;')

        cursor = conn.cursor()

        # conn = pyodbc.connect('Driver={SQL Server};' 
        #                 'Server=INTRANET\SQLEXPRESS;'
        #                 'Database=solarweb;'
        #                 'UID=sa;'
        #                 'PWD=2A291b5369;')

        # if cursor.connection is not None:
        #     print("Connection established successfully.")
        # else:
        #     print("Connection failed.")

        sql_1 = "INSERT INTO site_01 ([Date], [Earning(Today)], [Earning(Total)], [Co2 Saving Total(t)], [Co2 Saving Total(tree)], [Production(kWh)], [Consumption(kWh)]) VALUES (?, ?, ?, ?, ?, ?, ?)"
        conn.execute(sql_1, (date, result["url_1"]["value_1"], result["url_1"]["value_2"], result["url_1"]["value_3"], result["url_1"]["value_4"], result["url_1"]["value_5"], result["url_1"]["value_6"] ))
        
        sql_2 = "INSERT INTO site_02 ([Date], [Earning(Today)], [Earning(Total)], [Co2 Saving Total(t)], [Co2 Saving Total(tree)], [Production(kWh)], [Consumption(kWh)]) VALUES (?, ?, ?, ?, ?, ?, ?)"
        conn.execute(sql_2, (date, result["url_2"]["value_1"], result["url_2"]["value_2"], result["url_2"]["value_3"], result["url_2"]["value_4"], result["url_2"]["value_5"], result["url_2"]["value_6"] ))

        sql_3 = "INSERT INTO site_03 ([Date], [Earning(Today)], [Earning(Total)], [Co2 Saving Total(t)], [Co2 Saving Total(tree)], [Production(kWh)], [Consumption(kWh)]) VALUES (?, ?, ?, ?, ?, ?, ?)"
        conn.execute(sql_3, (date, result["url_3"]["value_1"], result["url_3"]["value_2"], result["url_3"]["value_3"], result["url_3"]["value_4"], result["url_3"]["value_5"], result["url_3"]["value_6"] ))
        
        sql_4 = "INSERT INTO site_04 ([Date], [Earning(Today)], [Earning(Total)], [Co2 Saving Total(t)], [Co2 Saving Total(tree)], [Production(kWh)], [Consumption(kWh)]) VALUES (?, ?, ?, ?, ?, ?, ?)"
        conn.execute(sql_4, (date, result["url_4"]["value_1"], result["url_4"]["value_2"], result["url_4"]["value_3"], result["url_4"]["value_4"], result["url_4"]["value_5"], result["url_4"]["value_6"] ))

        sql_5 = "INSERT INTO site_05 ([Date], [Earning(Today)], [Earning(Total)], [Co2 Saving Total(t)], [Co2 Saving Total(tree)], [Production(kWh)], [Consumption(kWh)]) VALUES (?, ?, ?, ?, ?, ?, ?)"
        conn.execute(sql_5, (date, result["url_5"]["value_1"], result["url_5"]["value_2"], result["url_5"]["value_3"], result["url_5"]["value_4"], result["url_5"]["value_5"], result["url_5"]["value_6"] ))

        sql_6 = "INSERT INTO site_06 ([Date], [Earning(Today)], [Earning(Total)], [Co2 Saving Total(t)], [Co2 Saving Total(tree)], [Production(kWh)], [Consumption(kWh)]) VALUES (?, ?, ?, ?, ?, ?, ?)"
        conn.execute(sql_6, (date, result["url_6"]["value_1"], result["url_6"]["value_2"], result["url_6"]["value_3"], result["url_6"]["value_4"], result["url_6"]["value_5"], result["url_6"]["value_6"] ))

        sql_7 = "INSERT INTO site_07 ([Date], [Earning(Today)], [Earning(Total)], [Co2 Saving Total(t)], [Co2 Saving Total(tree)], [Production(kWh)], [Consumption(kWh)]) VALUES (?, ?, ?, ?, ?, ?, ?)"
        conn.execute(sql_7, (date, result["url_7"]["value_1"], result["url_7"]["value_2"], result["url_7"]["value_3"], result["url_7"]["value_4"], result["url_7"]["value_5"], result["url_7"]["value_6"] ))

        sql_8 = "INSERT INTO site_08 ([Date], [Earning(Today)], [Earning(Total)], [Co2 Saving Total(t)], [Co2 Saving Total(tree)], [Production(kWh)], [Consumption(kWh)]) VALUES (?, ?, ?, ?, ?, ?, ?)"
        conn.execute(sql_8, (date, result["url_8"]["value_1"], result["url_8"]["value_2"], result["url_8"]["value_3"], result["url_8"]["value_4"], result["url_8"]["value_5"], result["url_8"]["value_6"] ))

        sql_9 = "INSERT INTO site_09 ([Date], [Earning(Today)], [Earning(Total)], [Co2 Saving Total(t)], [Co2 Saving Total(tree)], [Production(kWh)], [Consumption(kWh)]) VALUES (?, ?, ?, ?, ?, ?, ?)"
        conn.execute(sql_9, (date, result["url_9"]["value_1"], result["url_9"]["value_2"], result["url_9"]["value_3"], result["url_9"]["value_4"], result["url_9"]["value_5"], result["url_9"]["value_6"] ))

        sql_10 = "INSERT INTO site_10 ([Date], [Earning(Today)], [Earning(Total)], [Co2 Saving Total(t)], [Co2 Saving Total(tree)], [Production(kWh)], [Consumption(kWh)]) VALUES (?, ?, ?, ?, ?, ?, ?)"
        conn.execute(sql_10, (date, result["url_10"]["value_1"], result["url_10"]["value_2"], result["url_10"]["value_3"], result["url_10"]["value_4"], result["url_10"]["value_5"], result["url_10"]["value_6"] ))

        sql_11 = "INSERT INTO site_11 ([Date], [Earning(Today)], [Earning(Total)], [Co2 Saving Total(t)], [Co2 Saving Total(tree)], [Production(kWh)], [Consumption(kWh)]) VALUES (?, ?, ?, ?, ?, ?, ?)"
        conn.execute(sql_11, (date, result["url_11"]["value_1"], result["url_11"]["value_2"], result["url_11"]["value_3"], result["url_11"]["value_4"], result["url_11"]["value_5"], result["url_11"]["value_6"] ))

        print("Site_"+str(i+1)+ " done!")
    conn.commit()
solar()
