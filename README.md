# Find-Subdomain

Find-Subdomain is a Python script that allows you to retrieve all the paths within a given website. It leverages the `requests` library to send HTTP requests and the `BeautifulSoup` library to parse the HTML content.

## Requirements
- Python 3.x
- `requests` library: Install with `pip install requests`
- `beautifulsoup4` library: Install with `pip install beautifulsoup4`
-  `pyfiglet` library: Install with `pip install pyfiglet`

## Features
- Clean design Made by me <3
- Provides a user-friendly command-line interface.
- Manually solves Cloudflare security challenges to access protected websites
- Retrieves all the paths (URLs) within the website by parsing anchor tags (`<a>`) in the HTML content

## Usage
1. Clone the repository or download the script.
2. Install the required Python libraries: `pip install -r requirements.txt`.
3. Run the script: `python find_subdomain.py`.
4. Enter the website URL when prompted.
5. If the website is protected by Cloudflare, manually solve any security challenges presented in your web browser.
6. The script will then retrieve and display all the paths (URLs) within the website.

## Notes that no one cares about
- Please ensure that you have the necessary permissions to access and scrape the target website.
- Use this script responsibly and in accordance with the target website's terms of service.
- Be aware of any legal or ethical implications when scraping or accessing website content without explicit authorization.

## License

This project is licensed under the [MIT License](LICENSE).
