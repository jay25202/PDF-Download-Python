# Import libraries
import requests
from bs4 import BeautifulSoup

# URL from which pdfs to be downloaded
url = "https://www.osc.ca/en/securities-law/osc-bulletin?keyword=61-101&date%5Bmin%5D=&date%5Bmax%5D=&sort_bef_combine=field_start_date_DESC"

# Requests URL and get response object
response = requests.get(url)

# Parse text obtained
soup = BeautifulSoup(response.text, 'html.parser')
print(soup)

# Find all hyperlinks present on webpage
links = soup.find_all('a')
print(links)

i = 0

for link in links:

    if ('.pdf' in link.get('href', [])):
        i += 1
        print("Downloading file: ", i)

        # Get response object for link
        response = requests.get(link.get('href'))

        # Write content in pdf file
        pdf = open("pdf"+str(i)+".pdf", 'wb')
        pdf.write(response.content)
        pdf.close()
        print("File ", i, " downloaded")

print("All PDF files downloaded")
