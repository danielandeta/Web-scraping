from selenium import webdriver
from selenium.webdriver.common.by import By
import time


PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get('https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc')

peliculas = driver.find_elements(By.CLASS_NAME, 'lister-item.mode-advanced')
# Recorro cada uno de los anuncios que he encontrado
cont=1
for pelicula in peliculas:
    # Por cada anuncio hallo el preico
    rank = pelicula.find_element(By.CLASS_NAME, 'lister-item-index.unbold.text-primary').text
    print (rank)
    titulo = pelicula.find_element(By.XPATH, '//*[@id="main"]/div/div[3]/div/div['+str(cont)+']/div[3]/h3/a').text
    print (titulo)
    year = pelicula.find_element(By.CLASS_NAME, 'lister-item-year.text-muted.unbold').text
    print(year)
    cont += 1
driver.quit()
