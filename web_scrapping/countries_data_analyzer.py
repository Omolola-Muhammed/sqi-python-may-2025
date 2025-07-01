import requests
from bs4 import BeautifulSoup

def scrape_and_analyze_countries(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        rows = soup.find_all('tr')[1:]  

        countries = []
        for row in rows:
            cols = row.find_all('td')
            country = {
                'name': cols[0].text.strip(),
                'capital': cols[1].text.strip(),
                'population': int(cols[2].text.strip().replace(',', '')),
                'area': float(cols[3].text.strip().replace(',', ''))
            }
            countries.append(country)

        # Count countries
        country_count = len(countries)
        print(f"Number of countries: {country_count}")

        # Country with the largest population
        largest_population_country = max(countries, key=lambda x: x['population'])
        print(f"Country with the largest population: {largest_population_country['name']} ({largest_population_country['population']})")

        # Country with the smallest population
        smallest_population_country = min(countries, key=lambda x: x['population'])
        print(f"Country with the smallest population: {smallest_population_country['name']} ({smallest_population_country['population']})")

        # Average population
        average_population = sum(country['population'] for country in countries) / country_count
        print(f"Average population: {average_population:.2f}")

        # Population density
        for country in countries:
            country['density'] = country['population'] / country['area']

        # Top 3 countries with the highest density
        top_3_dense_countries = sorted(countries, key=lambda x: x['density'], reverse=True)[:3]
        print("Top 3 countries with the highest density:")
        for country in top_3_dense_countries:
            print(f"{country['name']}: {country['density']:.2f} people/km²")

        # Countries whose capital city starts with the letter "A"
        countries_with_capital_a = [(country['name'], country['capital']) for country in countries if country['capital'].startswith('A')]
        print("Countries whose capital city starts with the letter 'A':")
        for country, capital in countries_with_capital_a:
            print(f"{country}: {capital}")

        # Countries with an area greater than 1,000,000 km²
        large_area_countries = [country['name'] for country in countries if country['area'] > 1000000]
        print("Countries with an area greater than 1,000,000 km²:")
        print(large_area_countries)

        # Countries with an area less than 500 km²
        small_area_countries = [country['name'] for country in countries if country['area'] < 500]
        print("Countries with an area less than 500 km²:")
        print(small_area_countries)

        # Country with 0 population
        zero_population_country = [country['name'] for country in countries if country['population'] == 0]
        print("Country with 0 population:")
        print(zero_population_country)

    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    url = 'https://www.scrapethissite.com/pages/simple/'
    scrape_and_analyze_countries(url)

main()