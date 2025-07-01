import requests
from bs4 import BeautifulSoup

url = "http://quotes.toscrape.com/"


try:
    response = requests.get(url)
except requests.exceptions.RequestException as e:
    print(f"Oops. Something went wrong. Maybe check your internet connection? More details: {e}")
else:
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        print(soup.prettify())
        no_of_quotes = soup.find_all("div div.quotes span.text")

        if not no_of_quotes:
            print("No quotes available")
        
        all_quotes = len(no_of_quotes)
        print(all_quotes)
