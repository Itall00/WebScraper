import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=chrome_options)


def extraer(url):
    driver.get(url)
    page = driver.page_source
    soup = BeautifulSoup(page, 'lxml')
    return soup


def Ahumada(remedios,lista2):


    for i in remedios:

        url = f"https://www.farmaciasahumada.cl/catalogsearch/result/?q={i}"

        soup = extraer(url)
        lista = soup.find_all('ol', class_='products list items product-items')

        for job in lista:
            try:
                print(f"Principio activo:{i}")

                descripcionElement = job.find("a", class_="product-item-link").get_text()
                precio = job.find("span", class_="price").get_text()

                lista2.append(descripcionElement.strip())
                lista2.append("Ahumada")
                lista2.append(precio[1:])
                lista2.append("\n")



            except Exception as e:
                print("Exception: {}".format(e))
                pass

    return lista2