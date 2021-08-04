import requests
from bs4 import BeautifulSoup
import time
import pandas as pd


datas = []
for x in range(1,5):
    url = 'https://www.carsome.id/beli-mobil-bekas?pageNo='
    headers = {
        'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
    }
    r = requests.get(url+str(x), headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    content = soup.find_all('div', attrs={'class': 'card-box rewrite__card-list'})

    for item in content:
        name = item.find('div', attrs={'class': 'v-card__title pa-0 font-weight-bold card-title'})\
            .text.replace('\n','').replace('           ','').strip()
        price = item.find('div', attrs={'class': 'total-price'})\
            .text.replace('\n','').replace('Rp            ','').strip()
        location = item.find('span', attrs={'class': 'scale-inner'})\
            .text.replace('\n','').strip()

        cars_info = {
            'name': name,
            'price': price,
            'location': location
        }
        datas.append(cars_info)
    print('used car found: ',len(datas))
    time.sleep(3)

print(datas)

df = pd.DataFrame(datas)
print(df.head())

df.to_csv('datas.csv')
df.to_json('datas.json')
