import requests
import bs4

# deck = noStarchSoup.select('.Stable')
# deck = noStarchSoup.select('.Stable span')
# deck = noStarchSoup.select('.L14')

res = requests.get('http://mtgtop8.com/event?e=18649&d=316268&f=PAU')
# res = requests.get('http://mtgtop8.com/event?e=18649&d=316253&f=PAU')
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text)
deckname = noStarchSoup.select('.S16')
decklist = noStarchSoup.select('.G14')

print('Decklist: ' + deckname[0].get_text())
for span in decklist:
    print(span.get_text())


