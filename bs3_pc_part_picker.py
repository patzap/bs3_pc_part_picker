
import requests, bs4
import csv

res = requests.get('https://ca.pcpartpicker.com/products/pricedrop/')
src = res.content
soup = bs4.BeautifulSoup(src, 'lxml')
main_content = soup.find('div', {'class': 'main-content col xs-col-12 md-col-9 lg-col-9'})

for rows in main_content.find_all('tr'):
   
    data_set = []

    if (rows.a is not None) and (rows is not main_content.find('div', {'id': 'dg_laptop'})):

        item = rows.find('td', {'class': 'td__item'}).text.strip()
        prev = rows.find('td', {'class': 'td__previous'}).text.strip()
        curr = rows.find('td', {'class': 'td__current'}).text.strip()
        data_set.append([item, prev, curr])

    print(data_set)
        




        





    


