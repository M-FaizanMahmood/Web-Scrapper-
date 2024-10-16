# -*- coding: utf-8 -*-
"""Website Data Scraper.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1BBSXyUzknoKp6a4l3woGPDhW_5X6M01u
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Define the URL of the target web page (Replace with your actual URL)
url = 'https://stephanieyounger.com/about'

# Step 2: Send a GET request to the URL
response = requests.get(url)

# Step 3: Check if the request was successful
if response.status_code == 200:
    # Step 4: Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Step 5: Initialize lists to store the leads
    leads = []

    # Find the featured team list for names
    featured_team_list = soup.find('ul', class_='featured-team-list')  # Find the correct UL by class

    if featured_team_list:
        for item in featured_team_list.find_all('li'):  # Iterate through each LI
            # Extract name (if available)
            name_elem = item.find('h5')  # Name is in <h5>
            name = name_elem.text.strip() if name_elem else 'N/A'  # Extract name

            # Extract phone number (if available)
            phone_elem = item.find('a', href=lambda x: x and x.startswith('tel:'))
            number = phone_elem['href'].replace('tel:', '') if phone_elem else 'N/A'

            # Append the extracted data to the leads list
            leads.append({'Name': name, 'Number': number})

    # Step 6: Create a DataFrame to store the leads
    leads_df = pd.DataFrame(leads)

    # Print the DataFrame or save it to a CSV file
    print(leads_df)
    # leads_df.to_csv('leads.csv', index=False)  # Uncomment to save to a CSV file
else:
    print(f"Failed to retrieve data: {response.status_code}")

# prompt: save to csv

leads_df.to_csv('leads.csv', index=False)

