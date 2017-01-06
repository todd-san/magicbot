from bs4 import BeautifulSoup
import csv
import urllib2
import re

# I have the first 25 pages

card_names = []

for i in range(26, 50):
    soup = BeautifulSoup(urllib2.urlopen('https://deckbox.org/games/mtg/cards?p='+str(i)).read(), 'lxml')
    cardTable = soup.find('table', {'class': "main set_cards simple_table with_details"})

    for row in cardTable.findAll('tr')[1:]:
        col = row.findAll('td')

        # print col
        if 'card_name' in str(col):
            # print col
            name = re.findall(r">(.*?)</a>", str(col[0]))
            card_names.append(name)


card_names = [item for sublist in card_names for item in sublist]
# 'https://deckbox.org/mtg/A%20Display%20of%20My%20Dark%20Power?

card_pg_urls = []
card_urls = []
card_csv_list = []

for card in card_names:

    card_4_url = str('https://deckbox.org/mtg/')+str(card.replace(" ", "%20")) + str('?')
    card_pg_urls.append(card_4_url)

    # print card_4_url
    print card


    soup = BeautifulSoup(urllib2.urlopen(card_4_url).read(), 'lxml')
    card_on_card_page = soup.find('td', {'class': 'col left_card_col'})

    for row in card_on_card_page.findAll('img'):

        card_sparse_url = re.findall(r'src="(.*?)"/>', str(row))
        card_full_url = str('https://deckbox.org') + str(card_sparse_url[0])

        card_urls.append(card_full_url)
        print card_full_url
        print '-------------------'
        card_csv_list.append([card, card_full_url])
        break




with open("output.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(card_csv_list)


print card_names