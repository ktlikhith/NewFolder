import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/List_of_cities_in_India_by_population'

page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

city_table = soup.find('table')

table_header = [ colname.text.rstrip('\n') for colname in city_table.find_all('th')]

table_rows = city_table.find_all('tr')

for row in table_rows:
	row_data = [ data.text for data in row.find_all('td')]
	print(row_data)
