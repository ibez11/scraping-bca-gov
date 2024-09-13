BCA Registered Contractors Scraper

This Python script scrapes data from the BCA Registered Contractors directory on the Singapore Building and Construction Authority (BCA) website. It specifically focuses on Construction Workhead (CW02) contractors.

**Requirements:**

**Python 3**
Libraries:
1. requests
2. beautifulsoup4
3. pandas

**Installation:**

1. Make sure you have Python 3 installed.
2. Open a terminal or command prompt.
3. Install the required libraries using pip:

```
pip install requests beautifulsoup4 pandas
```

**Usage:**

1. Clone or download this repository.
2. Open a terminal or command prompt and navigate to the directory containing the script (scraping.py).   
3. Run the script with the following command:

```
python scraping.py
```

**Output:**

The script will:

1. Print the title of the scraped webpage.
2. Scrape data for registered contractors with Construction Workhead (CW02) from the provided URL.This data includes:

    1. No. (sequential number)
    2. Company Name
    3. UEN (Unique Entity Number)
    4. Address
    5. Tel (Telephone Number)

3. Print the scraped data as a list of dictionaries.
4. Save the scraped data to an Excel file named output_data.xlsx.
