# -*- coding: utf-8 -*-
"""PythonLegecy.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tEDQo_Mx7Vp_ng4--i-WlGg7F1Mv-Oda

#***GPU information***
"""

gpu_info = !nvidia-smi
gpu_info = '\n'.join(gpu_info)
if gpu_info.find('failed') >= 0:
  print('Not connected to a GPU')
else:
  print(gpu_info)

"""#***Connect Google Drive***"""

from google.colab import drive
drive.mount('/content/gdrive/', force_remount=True)

"""#***Access Pickle Files***"""

import pickle
objects = []
with (open("keywords.pickle", "rb")) as openfile:
    while True:
        try:
            objects.append(pickle.load(openfile))
        except EOFError:
            break

print(len(objects))
print(objects)

# create a dummy directory of files and folders
import os

os.mkdir("/content/TestDir")
os.mkdir("/content/TestDir/New Dir1")
os.mkdir("/content/TestDir/New Dir2")
os.mkdir("/content/TestDir/New Dir3")
os.mkdir("/content/TestDir/New Dir1/New Dir Dir1")
os.mkdir("/content/TestDir/New Dir1/New Dir Dir2")
os.mkdir("/content/TestDir/New Dir2/New Dir Dir3")
os.mkdir("/content/TestDir/New Dir3/New Dir Dir4")
os.mkdir("/content/TestDir/New Dir3/New Dir Dir5")
os.mkdir("/content/TestDir/New Dir3/New Dir Dir6")

"""#***Download google colab files to local directory automatically***"""

from google.colab import files
files.download('ingredients.json')

"""#***Creating Zip Files***"""

from zipfile import ZipFile
from pathlib import Path
import os

path_to_files = "/content/data/"
path_to_store_img = "/content/img.zip"
path_to_store_txt = "/content/txt.zip"


print(os.path.exists(path_to_files))


with ZipFile(path_to_store_img, "w") as zip:
  for path in Path(path_to_files).rglob("[7-9][0-9][0-9]_*.png"):
    #zip.write(path)
    print(path)

print()
print()
with ZipFile(path_to_store_txt, "w") as zip:
  for path in Path(path_to_files).rglob("[6-7].txt"):
    #zip.write(path)
    print(path)

path_to_files = "/content/nilearn_data/"
output_filename = "nilearn_data"

import shutil
shutil.make_archive(output_filename, 'zip', path_to_files)

"""#***Creating Zips from COCO Data Format***

"""

from zipfile import ZipFile
from pathlib import Path
import os

path2ann = "Data-Generated-50k-latest/annotations"
path2cap = "Data-Generated-50k-latest/captions"
path2img = "Data-Generated-50k-latest/images"
path2store = "ZipStore/"

print("Annotations: ", os.path.exists(path2ann))
print("Captions: ", os.path.exists(path2cap))
print("Images: ", os.path.exists(path2img))

# File name looks like this "object_detect-1.json"
with ZipFile(path2store+"annotations.zip", "w") as zip:
  for path in Path(path_to_files).rglob("object_detect-[0-9][0-9].json"):
    zip.write(path)

# File name looks like this "object_caption-1.json"
with ZipFile(path2store+"captions.zip", "w") as zip:
  for path in Path(path_to_files).rglob("object_captions-[0-9][0-9].json"):
    zip.write(path)



with ZipFile(path2store+"images.zip", "w") as zip:
  for path in Path(path_to_files).rglob("[0-2][0-9][0-9]_*.png"):
    zip.write(path)

"""#***Working with CSV files***"""

import csv # https://docs.python.org/3/library/csv.html

with open("data.csv", "w") as file:
  writer = csv.writer(file)
  writer.writerow(["transaction_id", "product_id", "price"])
  writer.writerow([1111, 1, 5])
  writer.writerow([2000, 77, 500])
  writer.writerow([500, 1000, 567])


with open("data.csv", "r") as file:
  reader = csv.reader(file)
  reader2 = reader
  print(list(reader2))

"""#***Working with JSON files***"""

import json
from pathlib import Path


movies = [
    {"id": 1, "title": "Pirates of the Caribbean: The Curse of the Black Pearl", "Year": 2003},
    {"id": 2, "title": "Pirates of the Caribbean: Dead Man's Chest", "Year": 2006},
    {"id": 3, "title": "Pirates of the Caribbean: At World's End", "Year": 2007},
    {"id": 4, "title": "Lord of the Rings: The Fellowship of the Ring", "Year": 2001},
    {"id": 5, "title": "Lord of the Rings: The Two Towers", "Year": 2002},
    {"id": 6, "title": "Lord of the Rings: The Return of the king", "Year": 2003}
]

data = json.dumps(movies)
print(data)

# Writing in JSON
Path("movies.json").write_text(data)


# Reading from JSON
data = Path("movies.json").read_text()
movies = json.loads(data)
print(movies[0]["title"])

"""#***SQLite Database***"""

import sqlite3

# https://docs.python.org/3/library/sqlite3.html


conn = sqlite3.connect('db.sqlite3')

conn.execute('''
CREATE TABLE Movies (
   Id INTEGER PRIMARY KEY,
   Title TEXT NOT NULL ,
   Year INTEGER NOT NULL
 );''')

conn.commit()

print("Movies table created");

# an example how you create databases using sqlite3


# conn = sqlite3.connect('test.db')

# conn.execute('''
# CREATE TABLE Departments (
#    Code INTEGER PRIMARY KEY NOT NULL,
#    Name NVARCHAR NOT NULL ,
#    Budget REAL NOT NULL
#  );''')

# conn.commit()

# print("Departments table created");

# conn.execute('''
# CREATE TABLE Employees (
#    SSN INTEGER PRIMARY KEY NOT NULL,
#    Name TEXT NOT NULL ,
#    LastName VARCHAR NOT NULL ,
#    Department INTEGER NOT NULL ,
#    Salary INTEGER NOT NULL,
#    CONSTRAINT fk_Departments_Code FOREIGN KEY(Department)
#    REFERENCES Departments(Code)
#  );''')

# conn.commit()

# print("Employees table created");

import sqlite3
import json
from pathlib import Path

# google > "db browser for SQLite"


movies_data = json.loads(Path("movies.json").read_text())
print(movies_data)

# writing to a database
with sqlite3.connect("db.sqlite3") as connection:
  command = "INSERT INTO Movies VALUES(?, ?, ?)"
  for movie in movies_data:
    connection.execute(command, tuple(movie.values()))
  connection.commit()

# reading from the database
with sqlite3.connect("db.sqlite3") as connection:
  command = "SELECT * FROM movies"
  cursor = connection.execute(command) # iterable object
  for row in cursor:
    print(row)


# reading from the database method 2
with sqlite3.connect("db.sqlite3") as connection:
  command = "SELECT * FROM movies"
  cursor = connection.execute(command) # iterable object
  movies = cursor.fetchall()
  print(movies)

"""#***Working with Timestamps/Date Time Objects***"""

import datetime
import time
from datetime import datetime
from datetime import timedelta

print(time.time()) # from the begining of time unix Jan 1st, 1970

def send_emails():
  for i in range (10000):
    pass

start = time.time()
send_emails()
end = time.time()
duration = end - start
print(duration)


dt = datetime(2018, 1, 1)
print(dt)
dt = datetime.now()
print(dt)
dt = datetime.strptime("2023/04/09", "%Y/%m/%d")
print(dt)

dt = datetime.fromtimestamp(time.time())
print(dt)

print(f"{dt.year}/{dt.month}")

dt1 = datetime(2018, 1, 1)
dt2 = datetime.now()
duration = dt2 - dt1

print(duration)
print("Days: ", duration.days)
print("Seconds: ", duration.seconds)

"""#***Playing with Random Values***"""

import random
import string


print("Random Value between [0,1) :", random.random())
print("Random Value between a & b :", random.randint(a=33, b=333))

print("Choosing randomly from an array :", random.choice([1,2,3,4,5,66,77,88,99,100,111,222,333,444,555]))
print("Choosing multiple numbers (k) randomly from an array :", random.choices([1,2,3,4,5,66,77,88,99,100,111,222,333,444,555], k=3))

# using string class you can get all the capital and small leters and intergers

print("Captial and small letters :", string.ascii_letters)
print("All numbers :", string.digits)


# Now creating passwords

password = "".join(random.choices(string.ascii_letters + string.digits, k=8))
print("Generated 8 character password :", password)


numbers = [1,3,5,6,8,33,21,64,732,6234]

print("Random Shuffling :", random.shuffle(numbers))

"""#***Sending Emails*** it doesn't work"""

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

message = MIMEMultipart()
message["from"] = "nayeemmohammad.nm@gmail.com"
message["to"] = "nayeemmohammad.nm@gmail.com"
message["subject"] = "Trying sending email tutorial from Colab"
message.attach(MIMEText("let's see if this shit works or not"))


with smtplib.SMTP(host="smtp.gmail.com", port= 587) as smtp:
  smtp.ehlo()
  smtp.starttls()
  smtp.login("nayeemmohammad.nm@gmail.com", "losnotches")
  smtp.send_message(message)
  print("sent...")