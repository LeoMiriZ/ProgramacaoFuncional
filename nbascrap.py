import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.by import By


# set url scraping

url = 'https://www.nba.com/stats/players/traditional'

binary = FirefoxBinary('C:\\Program Files\\Mozilla Firefox\\firefox.exe')

option = Options()

option.headless = False

driver = webdriver.Firefox(firefox_binary=binary, executable_path=r'C:\\geckodriver.exe', options=option)

driver.get(url)

time.sleep(10)

element = driver.find_element(By.XPATH, "//*[@class='Crom_table__p1iZz']")

print(element.text)

html_content = element.get_attribute('outerHTML')

print(html_content)

soup = BeautifulSoup(html_content, 'lxml')

table = soup.find(name='table')

print(table)

df_full = pd.read_html(str(table))

df_full[0].to_csv('nba_scraping.csv', index=False)

print(type(df_full))

print('Done')
