import csv
from BeautifulSoup import BeautifulSoup
import urllib

r = urllib.urlopen('http://m.nationals.mlb.com/roster/transactions/2017/03').read()
soup = BeautifulSoup(r)
table = soup.find('table')
print type(soup)

print soup.prettify()[0:1000]

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