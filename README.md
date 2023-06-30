#Find-Subdomain
Find-Subdomain is a Python script that allows you to discover subdomains of a given website. It utilizes the requests library to make HTTP requests and the BeautifulSoup library for HTML parsing.

#Features
Automatically adds "https://" to the input URL if missing.
Retrieves and displays all the subdomain links found on the website.
Provides a user-friendly command-line interface.
#Usage
Clone the repository or download the find_subdomain.py file.
Install the required dependencies: pip install requests beautifulsoup4 pyfiglet.
Run the script: python find_subdomain.py.
Enter the website you want to check (e.g., youtube.com or https://example.com).
The script will retrieve the HTML content of the website and display the subdomain links found.
Requirements
#Python 3.x
requests library
beautifulsoup4 library
pyfiglet library
