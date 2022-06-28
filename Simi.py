import requests
from bs4 import BeautifulSoup

import Remedios

def Simi(principio_activo): # scraper doctor simi

    for i in principio_activo:

        url = f"https://www.drsimi.cl/catalogsearch/result/?q={i}"

        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")

        results = soup.find_all('div', class_='product details product-item-details')

        for job in results:
            try:
                descripcionElement = job.find("a", class_="product-item-link").get_text()  # nombre remedio
                precio = job.find("span", class_="price").get_text()  # precio remedio
                descripcionElement1 = descripcionElement[2:] #evita error de "\n" al principio del nombre
                Remedios.medicamentos.append(Remedios.Producto(i, "Drsimi", descripcionElement1.strip(), float(precio[1:].replace(".", "")))) #añade el producto a medicamentos[]

            except Exception as e:
                print("Exception: {}".format(e))
                pass


    return