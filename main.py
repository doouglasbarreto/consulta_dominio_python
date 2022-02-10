from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

print("Iniciando nosso robô...\n")

driver = webdriver.Chrome('C:/Users/JMTech/Desktop/Projetos Python/consultar_dominio_python/chromedriver.exe')
driver.get("https://br.godaddy.com/domainsearch/find?")
pesquisa = driver.find_element_by_id("domain-search-box")
pesquisa.clear() # Limpando a barra de pesquisa
time.sleep(2)
pesquisa.send_keys("douglasbarreto.me")
pesquisa.send_keys(Keys.RETURN)

time.sleep(8)


driver.close()
