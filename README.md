BCA Registered Contractors Scraper

This Python script scrapes data from the BCA Registered Contractors directory on the Singapore Building and Construction Authority (BCA) website. It specifically focuses on Construction Workhead (CW02) contractors.

Requirements:

Python 3
Libraries:
requests
beautifulsoup4
pandas
Installation:

Make sure you have Python 3 installed.
Open a terminal or command prompt.
Install the required libraries using pip:
pip install requests beautifulsoup4 pandas
Usage:

Clone or download this repository.
Open a terminal or command prompt and navigate to the directory containing the script (scraping.py).   
Run the script with the following command:
python scraping.py
Output:

The script will:

Print the title of the scraped webpage.
Scrape data for registered contractors with Construction Workhead (CW02) from the provided URL. This data includes:
No. (sequential number)
Company Name
UEN (Unique Entity Number)
Address
Tel (Telephone Number)
Print the scraped data as a list of dictionaries.
Save the scraped data to an Excel file named output_data.xlsx.
Notes:

This script uses a basic example URL. You can modify the url_to_scrape variable in the script to target different search criteria on the BCA website.
Be aware of website scraping limitations and terms of use. It's recommended to check the BCA website's policies before scraping data extensively.
Additional Information:

This script demonstrates basic web scraping techniques using the requests and BeautifulSoup libraries.
The script uses pandas to organize the scraped data into an Excel file.

