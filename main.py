import sqlite3
import urllib.request
import requests as requests
import re
from bs4 import BeautifulSoup


connection = sqlite3.connect("MYBD.sl3", 5)
cur = connection.cursor()
# cur.execute("CREATE TABLE search (links TEXT);")
# cur.execute("INSERT INTO search (links) VALUES ('');")
# cur.execute("CREATE TABLE search (links TEXT)")
# cur.execute("DELETE FROM search WHERE rowid=2;


search_term = input("Введіть інформацію для пошуку: ")
cur.execute('''SELECT * FROM search;''')


rows = cur.fetchall()




for link in rows:
   print(link[0])
   page = requests.get(link[0])
   print("Отримано", len(page.content), " bytes")
   print(page.text)
   soup = BeautifulSoup(page.content, 'html.parser')
   print("Шукаємо про ", search_term, sep="")
   results = soup.find_all(string=search_term)
if len(results) > 0:
   print("Знайдено на сторінці ", link[0], " = ", len(results) )
else:
   print("Нічого не знайдено")




connection.commit()


connection.close()
