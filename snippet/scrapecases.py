# importing modules
import requests
from bs4 import BeautifulSoup
import re

# URL for scrapping data
url = 'https://www.worldometers.info/coronavirus/country/us/'

# get URL html
page = requests.get('https://www.worldometers.info/coronavirus/')
soup = BeautifulSoup(page.text, 'html.parser')

data = []
#print(dir(soup))
#print(soup.text)
# soup.find_all('td') will scrape every
# element in the url's table
data_iterator = soup.find_all('odd')

# data_iterator is the iterator of the table
# This loop will keep repeating till there is
# data available in the iterator
#text = re.search("^<td*<>$", str(data_iterator[1]))
#txt = str(data_iterator[1])
print(data_iterator)
#Check if the string contains "a" followed by exactly two "l" characters:

'''#x = re.findall('^<td style="text-align:left;">', txt)
cases = {}
caseslist = []
count = 0
for i in data_iterator:
	txt = str(i)
	x = re.search('>', txt)
	count = count + 1
	caseslist.append(txt[x.start()+1:].split('</td>')[0])

print(caseslist)

cases['name'],cases['tcases'],cases['acases'],cases['tdeaths'] = caseslist[1],caseslist[2],caseslist[7],caseslist[4]
cases['rrate'] = (int(caseslist[6].replace(',',''))/int(caseslist[2].replace(',','')))* 100
print(caseslist[12])


#Expected elds in coronavirus cases summary: Country Name, Total Cases, Active Cases, Total
#Deaths, Recovery Rate(Total Recovered/Total Cases), Percentage of Population Infected (Total
#Cases/Population)'''

