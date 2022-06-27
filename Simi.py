import requests
from bs4 import BeautifulSoup

import Remedios

def Simi(principio_activo):

    for i in principio_activo:

        url = f"https://www.drsimi.cl/catalogsearch/result/?q={i}"

        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")

        results = soup.find_all('div', class_='product details product-item-details')

        for job in results:
            try:
                descripcionElement = job.find("a", class_="product-item-link").get_text()
                precio = job.find("span", class_="price").get_text()
                Remedios.medicamentos.append(Remedios.Producto(i, "Drsimi", descripcionElement.strip(), float(precio[1:].replace(".", ""))))

            except Exception as e:
                print("Exception: {}".format(e))
                pass


    return