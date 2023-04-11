from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware


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
cache = cachetools.TTLCache(maxsize=100, ttl=15)
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origin_regex='https?://localhost:8*',
    allow_credentials=True,
    allow_methods=['GET'],
    allow_headers=["*"],
)


@app.get("/", response_class=HTMLResponse)
async def root():
    now = time.ctime()
    return f'''{now}<br>the following API Endpoints are available:<br>
            <a href='/ignoredPatients'>ignoredPatients</a><br>
            <a href='/ersteRTsMockup'>ersteRTsMockup</a>'''


@app.get("/ignoredPatients")
async def get_ignored_patients():
    cursor = conn_local.execute('''SELECT * FROM IgnorePatient''')
    return await sqlite_tools.cursor_to_json(cursor)


@app.get("/ersteRTsMockup")
async def get_first_rts_mockup():
    patient_table = cache.get("mockup_patient_table")
    if patient_table is None:
        cursor = conn_local.execute('''SELECT * FROM MockupPatient''')
        patient_table = await sqlite_tools.cursor_to_json(cursor)
        cache["mockup_patient_table"] = patient_table
    return patient_table


@app.get("/oncologist_timetable/{oncologist_name}")
async def get_oncologist_timetable(oncologist_name: str):
    cursor = conn_local.execute('''SELECT TOP 1 * FROM ''')
    result = cursor.fetchone()
    if len(result) == 0:
        pass
    else:
        return result
