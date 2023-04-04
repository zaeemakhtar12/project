import cs50
import csv

open("favorites8.db", "w").close()
db = cs50.SQL("sqlite:///favorites8.db")

db.execute("CREATE TABLE show (id INTEGER, title TEXT NOT NULL, PRIMARY KEY(id))")
db.execute("CREATE TABLE genres (show_id INTEGER, genre TEXT NOT NULL, FOREIGN KEY (show_id) REFERENCES shows(id)")

with open("favorites.cvs", "r") as file:    
    reader = cvs.DictReader(file)
    for row in reader:

        print(row)

        title = row["title"].strip().upper()
        show_id = db.execute("INSERT INTO SHOWS (title) VALUES(?)", title)
        for genre in row["genres"].split(", "):
            db.execute("INSERT INTO genres (show_id, genre) VALUES(?, ?)", show_id, genre)