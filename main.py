import requests


def get_country_data(country):
    response = requests.get(f"https://restcountries.com/v3.1/name/{country}")
    data = response.json()
    capital = data[0]['capital'][0]
    region = data[0]['region']
    population = data[0]['population']
    languages = data[0]['languages']['ita']

    return capital, region, population, languages


def run():
    country = input("Enter country: ")
    country_data = get_country_data(country)
    capital, region, population, languages = country_data


    print(f"""Capital: {capital}
Region: {region}
Population: {population}
Languages: {languages}
""")


if __name__ == '__main__':
    run()
