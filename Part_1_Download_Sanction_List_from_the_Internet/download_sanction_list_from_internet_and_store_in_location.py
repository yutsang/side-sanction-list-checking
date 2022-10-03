import urllib.request
from datetime import date

def download_file(url, filename):
    response = urllib.request.urlopen(URL)
    file = open(filename+".pdf", "wb")
    file.write(response.read())
    file.close()

URL = "https://scsanctions.un.org/consolidated/"
Location = "/Users/ytsang/Desktop/Github/side-sanction-list-checking/Sanction_List"

download_file(URL, "HKICPA_UN Consolidated list_"+str(date.today()))