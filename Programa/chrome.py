from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep

servico = Service(ChromeDriverManager().install()) #Para baixar o Driver correspondente automáticamente

driver = webdriver.Chrome(service = servico)
url = 'https://books.toscrape.com/'
sleep(2)
driver.get(url)
sleep(20)
