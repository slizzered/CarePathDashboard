from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import cachetools
import sqlite3
import time
from mockup_data import mockup_db
from utils import sqlite_tools

# generate mockup data
mockup_db.create_ignorePatient('mydb.sqlite')
mockup_db.create_mockupPatient('mydb.sqlite', random_seed=5)


# connect to local database file
conn_local = sqlite3.connect('mydb.sqlite')
cache = cachetools.TTLCache(maxsize=100, ttl=3)
app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def root():
    now = cache.get("now")
    if now is None:
        now = time.ctime()
        cache["now"] = now
    return f'''the following API Endpoints are available:<br>
            <a href='/ignoredPatients'>ignoredPatients</a><br>
            <a href='/ersteRTsMockup'>ersteRTsMockup</a>'''


@app.get("/ignoredPatients")
async def get_ignored_patients():
    cursor = conn_local.execute('''SELECT * FROM IgnorePatient''')
    return await sqlite_tools.cursor_to_json(cursor)

@app.get("/ersteRTsMockup")
async def get_first_rts_mockup():
    cursor = conn_local.execute('''SELECT * FROM MockupPatient''')
    return await sqlite_tools.cursor_to_json(cursor)




