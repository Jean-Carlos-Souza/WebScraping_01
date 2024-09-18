from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep
import pandas as pd


servico = Service(ChromeDriverManager().install()) #Para baixar o Driver correspondente automáticamente

driver = webdriver.Chrome(service = servico)
url = 'https://books.toscrape.com/'

driver.get(url)

#Para pegar os Títulos dos livros:
titulosDosElementos = driver.find_elements(By.TAG_NAME, 'a')[54:94:2]

titleList = [title.get_attribute('title') for title in titulosDosElementos]
estoqueList = []
sleep(1)

for title in titulosDosElementos:

    title.click()

    quantidade_estoque = int(driver.find_element(By.CLASS_NAME, 'instock').text.replace('In stock (','').replace(' available)', ''))

    estoqueList.append(quantidade_estoque)

    driver.back()

sleep(5)

dicDoc = {
    'title':titleList,
    'estoque':estoqueList
}


print(pd.DataFrame(dicDoc))