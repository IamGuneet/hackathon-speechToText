import requests
from bs4 import BeautifulSoup
from googletrans import Translator
from bs4.element import Tag


from translate import Translator

# Function to translate text using the Translate library
def translate_text(text, target_language='hi'):
    translator = Translator(to_lang=target_language)
    translation = translator.translate(text)
    return translation

# ... rest of the code remains the same ...


# Function to recursively process and translate HTML elements
def translate_html_element(element):
    if isinstance(element, Tag):
        # If the element is a tag, recursively process its children
        for child in element.contents:
            translate_html_element(child)
    else:
        # If the element is a string, translate it and replace the content
        translated_text = translate_text(element)
        element.replace_with(translated_text)

# URL of the website to scrape
url = 'https://www.india.gov.in/'  # Replace with the URL of the website you want to scrape

# Send a GET request to the website
response = requests.get(url)

if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Translate the entire HTML content
    translate_html_element(soup)

    # Create a new HTML file with the translated content
    with open('translated_page.html', 'w', encoding='utf-8') as output_file:
        output_file.write(str(soup))
else:
    print("Failed to retrieve the web page. Status code:", response.status_code)
