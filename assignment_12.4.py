# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/known_by_Kriss.html"
# # url = input('Enter - ')
# html = urlopen(url, context=ctx).read()
# soup = BeautifulSoup(html, "html.parser")

# # Retrieve all of the anchor tags
# tags = soup('a')
# for tag in tags:
#     print(tag.text)

postition = 18
times = 7


def get_third(link):
    html = urlopen(link, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")

    # Retrieve all of the anchor tags
    tags = soup('a')

    return tags[postition - 1].get_attribute_list('href')[0]


count = 0
while count != times:
    count += 1
    url = get_third(url)

print(url.replace(".html", "").replace("http://py4e-data.dr-chuck.net/known_by_", ""))

