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

driver.find_element(By.XPATH, "//div[@class='Crom_container_C45Ti crom-container']//table//thead/tr//th[@field='PTS']")


