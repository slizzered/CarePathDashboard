from fastapi import FastAPI
import cachetools
import sqlite3

import time


# create a new database file
conn = sqlite3.connect('mydb.sqlite')
# create a new table to store the values
conn.execute('''CREATE TABLE IF NOT EXISTS IgnorePatient
                (id STRING PRIMARY KEY, EntryCreationDateTime DATETIME)''')
# insert some values into the table
values = [('z123', sqlite3.datetime.datetime.now()),
          ('z456', sqlite3.datetime.datetime.now()),
          ('z789', sqlite3.datetime.datetime.now())]
conn.executemany('INSERT OR IGNORE INTO IgnorePatient (id, EntryCreationDateTime) VALUES (?, ?)', values)
# commit the changes to the database
conn.commit()


cache = cachetools.TTLCache(maxsize=100, ttl=3)
app = FastAPI()


@app.get("/")
async def root():
    now = cache.get("now")
    if now is None:
        now = time.ctime()
        cache["now"] = now
    return {"message": f"Hello World. The current time is {now}"}


@app.get("/ignoredPatients")
async def get_ignored_patients():
    result = conn.execute('''SELECT * FROM IgnorePatient''')
    return result


@app.post("/ignoredPatients/{patient_id}")
async def post_ignored_patient(patient_id: str):
    conn.execute(f'INSERT OR IGNORE INTO IgnorePatient (id, EntryCreationDateTime) VALUES (?, ?)',
                 (patient_id, sqlite3.datetime.datetime.now()))
    conn.commit()
