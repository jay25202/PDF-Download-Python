import requests
import json


with open("codee.json", encoding="utf-8") as l:
    data = json.load(l)

i = 0
for link in data:

    i += 1
    print("Downloading file: ", i)

    # Get response object for link
    response = requests.get(link)

    # Write content in pdf file
    pdf = open("pdf"+str(i)+".pdf", 'wb')
    pdf.write(response.content)
    pdf.close()
    print("File ", i, " downloaded")

print("All PDF files downloaded")

# for pdf in response:

#     # Write content in pdf file
# pdf = open("pdf"+str(i)+".pdf", 'wb')
# pdf.write(response.content)
# pdf.close()
