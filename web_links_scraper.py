import sys
import csv
from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin
import subprocess

# Verificar si se proporcionó un argumento (URL del sitio web)
if len(sys.argv) != 2:
    print("Uso: python web_links_scraper.py <URL_del_sitio_web>")
    sys.exit(1)

# Obtener la URL del sitio web desde los argumentos de la línea de comandos
site_url = sys.argv[1]

# Realizar la solicitud HTTP y procesar el HTML
try:
    response = requests.get(site_url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
except Exception as e:
    print(f"Error al acceder al sitio web: {str(e)}")
    sys.exit(1)

# Crear o abrir un archivo CSV para escribir los resultados
with open("resultados.csv", "w", newline="", encoding="utf-8") as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(["URL FROM", "Enlace que cumple con la condición .HTML", "Texto del enlace"])

    for link in soup.find_all("a"):
        href = link.get("href")
        text = link.get_text()
        #if href and href.endswith(".html"):
        if href:
            csv_writer.writerow([site_url, href, text])

print("Resultados exportados a resultados.csv")

# Run script2.py from script1.py
subprocess.call(["python", "toExcel.py"])
