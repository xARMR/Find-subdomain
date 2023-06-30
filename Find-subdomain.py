import requests
import pyfiglet
from bs4 import BeautifulSoup
from urllib.parse import urljoin
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

os.system('cls')
print('+'*67)
logo = pyfiglet.figlet_format("Find_Subdomain")
print(logo)
print('+'*67)

url = input("\n[?] Enter website: "+b)
if not url.startswith("https://"):
    url = "https://" + url

print(j+'-'*67)

# Set the headers to simulate a browser request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36",
}

# Send a GET request to the website and manually solve any security challenges if prompted
response = requests.get(url, headers=headers)

# Retrieve the HTML content after solving the security challenges
html_content = response.text

soup = BeautifulSoup(html_content, "html.parser")

links = soup.find_all("a")
for link in links:
    href = link.get("href")
    absolute_url = urljoin(url, href)
    print(c + absolute_url)

print(i+'-'*67)
print("By ARMR")

# Set the headers to simulate a browser request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36",
}

# Send a GET request to the website and manually solve any security challenges if prompted
response = requests.get(url, headers=headers)

# Retrieve the HTML content after solving the security challenges
html_content = response.text

soup = BeautifulSoup(html_content, "html.parser")

links = soup.find_all("a")
for link in links:
    href = link.get("href")
    absolute_url = urljoin(url, href)
    print(c + absolute_url)

print(i+'-'*67)
print("By ARMR")
