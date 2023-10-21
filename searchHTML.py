import csv
from bs4 import BeautifulSoup
import requests
from queue import Queue
from urllib.parse import urljoin, urlparse
import subprocess

""" # Text clearing function
def clean_text(text):
    try:
        return text.encode("utf-8", errors="ignore").decode("utf-8")
    except Exception:
        return text """

# Home URL
start_url = "https://www.siem-reap-car-service.com/"
parsed_start_url = urlparse(start_url)
base_url = f"{parsed_start_url.scheme}://{parsed_start_url.netloc}"

# We create a queue of URLs to crawl
url_queue = Queue()
url_queue.put(start_url)

# Store URLs already visited to avoid infinite loops
visited_urls = set()

# Create or open a CSV file to write the results with UTF-8 encoding
with open("Results.csv", "w", newline="", encoding="utf-8") as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(["URL FROM", "Link with .HTML", "Anchor"])

    while not url_queue.empty():
        url = url_queue.get()
        if url not in visited_urls:
            try:
                response = requests.get(url)
                soup = BeautifulSoup(response.text, "html.parser")
                for link in soup.find_all("a"):
                    href = link.get("href")
                    #text = clean_text(link.get_text())
                    text = link.get_text()
                    #if href and href.endswith(".html") and not href.startswith("#"):
                    if href and href.endswith(".html"):
                        # Remove anchors (#) from URL
                        href = urljoin(url, href).split('#')[0]
                        # Avoid identical links in URL FROM and Link that meets the .HTML condition
                        if url != href:
                            # Avoid URLs that end in .html in the URL FROM column
                            if not url.endswith(".html"):
                                csv_writer.writerow([url, href, text])
                    absolute_url = urljoin(base_url, href)  # Normalize the URL
                    #if urlparse(absolute_url).netloc == parsed_start_url.netloc and not href.startswith("#"):
                    if urlparse(absolute_url).netloc == parsed_start_url.netloc:
                        if absolute_url not in visited_urls:
                            url_queue.put(absolute_url)
                visited_urls.add(url)
            except Exception as e:
                print(f"Processing error {url}: {str(e)}")

print("Exported to Results.csv")


# Run script2.py from script1.py
subprocess.call(["python", "toExcel.py"])
