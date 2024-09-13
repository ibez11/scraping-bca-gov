import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_website(url):
    try:
        # Fetching web page content using requests
        response = requests.get(url)
        response.raise_for_status()  # Checking if the response is successful or not

        # Parsing HTML web page using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Example: Getting the page title
        page_title = soup.title.string
        print(f"Title: {page_title}")

        # Example: Getting all links on the page
        companies = soup.find_all('div', class_='company-list-item')
        data_list = []
        count = 1
        for company in companies:
            title_div = company.find('a', class_='title')
            en_div = company.find('div', class_='uen')
            address_div = company.find('div', class_='address')
            tel_div = company.find('div', class_='tel')
            data_list.append({'No.': count, 'Company Name': title_div.text.strip(), 'UEN': en_div.text.strip(), 'Address': address_div.text.strip(), 'Tel': tel_div.text.strip()})
            count += 1
            # Uncomment the following lines to print individual data
            # print(count)
            # print(title_div.text.strip())
            # print(en_div.text.strip())
            # print(address_div.text.strip())
            # print(tel_div.text.strip())
            # print(f"Link: {link.get('href')}")

        print(data_list)
        df = pd.DataFrame(data_list)
        excel_filename = 'output_data.xlsx'
        df.to_excel(excel_filename, index=False)
        print(f"Data has been saved to Excel file: {excel_filename}")

    except requests.exceptions.RequestException as e:
        print(f"Error during request: {e}")
    except Exception as e:
        print(f"Error: {e}")

# Replace the URL with the website URL you want to scrape
url_to_scrape = "https://www1.bca.gov.sg/bca-directory/registered-contractors/construction?workhead=CW02&grading=All&filter=All&itemsperpage=882&page=1"
scrape_website(url_to_scrape)
