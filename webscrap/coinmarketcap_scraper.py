# UD12.b

from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd
url = 'https://coinmarketcap.com/new/'
service = Service(executable_path=r'./chromedriver')
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920,1200")

browser = webdriver.Chrome(service=service, options=chrome_options)

browser.get(url)

accept_cookies_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID,"onetrust-accept-btn-handler")))

accept_cookies_button.click()

language_button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH,"//div[@class='cmc-popover__trigger']/button")))

language_button.click()

topbar = browser.find_element(By.CLASS_NAME, 'topbar')

language_input = WebDriverWait(topbar, 5).until(EC.presence_of_element_located((By.XPATH,".//input")))

language_input.send_keys("Español")

spanish_option = WebDriverWait(browser,5).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, 'Español')))

spanish_option.click()


url_gainers_losers = 'https://coinmarketcap.com/gainers-losers/'

browser.get(url_gainers_losers)

table_wrap = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CLASS_NAME,"table-wrap")))

tables = table_wrap.find_elements(By.XPATH, ".//table")

table_gainers = tables[0]

rows = table_gainers.find_elements(By.XPATH, ".//tbody/tr")

for row in rows:
    cells = row.find_elements(By.XPATH, ".//td")
    row_text = (cells[0].text + ' - ' + cells[1].text + ' - ' + cells[3].text).replace("\n", "")
    print(row_text)

table_gainers_bs = BeautifulSoup(table_gainers.get_attribute('outerHTML'), 'html.parser')

dataframe = pd.read_html(str(table_gainers_bs))[0]

dataframe = dataframe.sort_values(by=["24h"], ascending=False)

column_24h = dataframe["24h"].str.rstrip("%").astype('float')

dataframe.insert(loc = 2, column = "24h(%)", value = column_24h)

dataframe = dataframe.drop(columns=["24h"])

print(dataframe)

sleep(10)