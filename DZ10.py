import sqlite3
import requests

from bs4 import BeautifulSoup

connection = sqlite3.connect("DZ10.sl3", 5)
cur = connection.cursor()

response = requests.get("https://sinoptik.ua/")
if response.status_code == 200:
     soup = BeautifulSoup(response.text, features="html.parser")
     soup_list = soup.find_all("p", {"class" : "today-temp"})
for elem in soup_list:
    time = elem.text

response = requests.get("https://sinoptik.ua/")
if response.status_code == 200:
     soup = BeautifulSoup(response.text, features="html.parser")
     soup_list = soup.find_all("p", {"class" : "today-temp"})
for elem in soup_list:
    time = elem.text

cur.execute(f"INSERT INTO datatime (Time) VALUES ('{time}')")
connection.commit()

cur.execute("SELECT rowid, Time  FROM datatime;")
connection.commit()
res = cur.fetchall()
print(res)
cur.execute(f"INSERT INTO datatime (Time) VALUES ('{time}')")
connection.commit()
cur.execute("SELECT rowid, Temperatura  FROM weather;")
connection.commit()
res = cur.fetchall()
print(res)
