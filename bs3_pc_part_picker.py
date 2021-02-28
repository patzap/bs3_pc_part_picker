
import requests, bs4
import csv

#outfile = open('pc_partpicker.csv', 'w')
#writer = csv.writer(outfile)

#writer.writerow(['Item', 'Previous'])

res = requests.get('https://ca.pcpartpicker.com/products/pricedrop/')
src = res.content
soup = bs4.BeautifulSoup(src, 'lxml')
main_content = soup.find('div', {'class': 'main-content col xs-col-12 md-col-9 lg-col-9'})

for rows in main_content.find_all('tr'):
    '''
    if (rows.a is not None) and (rows is not main_content.find('div', {'id': 'dg_laptop'})): 
        items = rows.find_all('td')
        items = [ele.text.strip() for ele in items if ele is not ele.find('td', {'class': 'td__add'}) and ele != '\n']
        

        print(items)
    '''
    data_set = []

    #title_header = rows.find_all('h2')
    if (rows.a is not None) and (rows is not main_content.find('div', {'id': 'dg_laptop'})):

        header = []
        item = rows.find('td', {'class': 'td__item'}).text.strip()
        prev = rows.find('td', {'class': 'td__previous'}).text.strip()
        curr = rows.find('td', {'class': 'td__current'}).text.strip()
        data_set.append([header, item, prev, curr])

     
div = main_content.find_all('div')
print(div)
    
#outfile.close()

        





    


