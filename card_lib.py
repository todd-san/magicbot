import csv


f = open('raw_cards_and_urls.csv')

reader = csv.reader(f)


# chars_to_remove = ['.', '!', '?']
# subj = 'A.B!C?'
# subj.translate(None, ''.join(chars_to_remove))

chars_to_remove = [',', "'", '"', '.', ' ']
cleaned_card_list = []

for row in reader:
    clean_card = str(row[0].lower())
    clean_card = clean_card.translate(None, ''.join(chars_to_remove))
    print clean_card

    cleaned_card_list.append([clean_card, row[1]])


card_dict = {el[0]: el[1] for el in cleaned_card_list}
print card_dict