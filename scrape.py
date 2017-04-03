import csv
import requests
from BeautifulSoup import BeautifulSoup

url = 'http://m.nationals.mlb.com/roster/transactions/2017/03'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)
table = soup.find('table')

list_of_rows = []
counter = 1
for row in table.findAll('tr')[1:-1]:
    list_of_cells = []
    for cell in row.findAll('td'):
        list_of_cells.append(cell.text.encode('utf-8'))
    list_of_rows.append(list_of_cells)

outfile = open("transactions.csv", "wb")
writer = csv.writer(outfile)
writer.writerow(["date", "url", "text"])
writer.writerows(list_of_rows)