import requests
from bs4 import BeautifulSoup
import pyfiglet
import os

a = "\033[0m"
b = "\033[31m"
c = "\033[32m"
d = "\033[33m"
e = "\033[34m"
f = "\033[35m"
g = "\033[36m"
h = "\033[37m"
i = "\033[91m"
j = "\033[92m"
k = "\033[90m"
l = "\033[94m"

os.system('clear')
print('+'*67)
logo = pyfiglet.figlet_format("Find-Subdomain")
print(logo)
print('+'*67)

url = input("\n[?] Enter website: "+b)
if not url.startswith("https://"):
    url = "https://" + url

print(j+'-'*67)
response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(html_content, "html.parser")

links = soup.find_all("a")
for link in links:
    href = link.get("href")
    print(c+href)
print(i+'-'*67)
print(d+"By ARMR")
