import requests
from bs4 import BeautifulSoup
import re
import json

def scrape_words(url):
    # Send a GET request to the URL
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        text_content = soup.get_text()

        words = re.findall(r'\b\w+\b', text_content)

        return words
    else:
        print("Failed to retrieve the webpage. Status code:", response.status_code)
        return []

website_url = 'https://www.india.gov.in/'
word_list = scrape_words(website_url)

word_dict = {"words": word_list}

json_file_path = 'words.json'
# for word in word_list:
#         try:
#         # Encode the word as UTF-8 before printing
#             print(word.encode('utf-8').decode('utf-8'))
#         except UnicodeEncodeError:
#         # Handle characters that can't be encoded (you can customize this part)
#             print('*')
with open(json_file_path, 'w', encoding='utf-8') as json_file:
    json.dump(word_dict, json_file, ensure_ascii=False, indent=4)

print(f"Words have been saved to {json_file_path}")
