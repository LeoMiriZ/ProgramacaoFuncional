import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options 
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary 
from selenium.webdriver.common.by import By
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# conexão com base de dados MySQL
SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost:3306/nba'

engine = create_engine(SQLALCHEMY_DATABASE_URI)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

session = SessionLocal()

Base = declarative_base()

Base.metadata.create_all(bind=engine)

# scrap nba 
url = 'https://stats.nba.com/players/traditional/?PerMode=Totals&Season=2019-20&SeasonType=Regular%20Season&sort=PLAYER_NAME&dir=-1'
binary = FirefoxBinary('C:\\Program Files\\Mozilla Firefox\\firefox.exe')

option = Options()
option.headless = True
driver = webdriver.Firefox(firefox_binary=binary, executable_path='C:\\geckodriver.exe')

driver.get(url)
#time.sleep(10)

#element = driver.find_element_by_xpath("//div[@class='nba-stat-table']//table")
element = driver.find_element(By.XPATH, "//*[@class='Crom_table__p1iZz']")
html_content = element.get_attribute('outerHTML')
print(html_content)
time.sleep(5)

# Parsear conteúdo HTML - BeautifulSoup
soup = BeautifulSoup(html_content, 'lxml')
table = soup.find(name='table')
print(table)

# Estruturar conteúdo em um Data Frame - Pandas
df_full = pd.read_html(str(table))
df_sql = pd.DataFrame(df_full[0])
df_sql.drop(columns=['Unnamed: 0'], inplace=True)

# Criação e inserção de dados na tabela MySQL

df_sql.to_sql(name='nba-stats', con=engine, index=False, if_exists='append')

driver.find_element(By.XPATH, "//*[@title='Next Page Button']").click()
time.sleep(5)

element = driver.find_element(By.XPATH, "//*[@class='Crom_table__p1iZz']")
html_content = element.get_attribute('outerHTML')
print(html_content)
time.sleep(5)

# Parsear conteúdo HTML - BeautifulSoup
soup = BeautifulSoup(html_content, 'lxml')
table = soup.find(name='table')
print(table)

# Estruturar conteúdo em um Data Frame - Pandas
df_full = pd.read_html(str(table))
df_sql = pd.DataFrame(df_full[0])
df_sql.drop(columns=['Unnamed: 0'], inplace=True)

# Criação e inserção de dados na tabela MySQL

df_sql.to_sql(name='nba-stats', con=engine, index=False, if_exists='append')

driver.quit()