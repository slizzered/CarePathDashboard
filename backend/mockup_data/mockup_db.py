import sqlite3
import random
from datetime import datetime, timedelta


def create_ignorePatient(dbfile):
    # create a new database file
    conn = sqlite3.connect(dbfile)
    # create a new table to store the values
    conn.execute('''CREATE TABLE IF NOT EXISTS IgnorePatient
                    (id STRING PRIMARY KEY, EntryCreationDateTime DATETIME, EntryExpirationDateTime DATETIME)''')
    # insert some values into the table
    values = [('z123', datetime.now(), datetime.now()+timedelta(days=1)),
              ('z456', datetime.now(), datetime.now()+timedelta(days=1)),
              ('z789', datetime.now(), datetime.now()+timedelta(days=1))]

    conn.executemany('INSERT OR IGNORE INTO IgnorePatient (id, EntryCreationDateTime, EntryExpirationDateTime) VALUES (?, ?, ?)', values)
    # commit the changes to the database
    conn.commit()
    conn.close()


def create_mockupPatient(dbfile, random_seed=None):
    random.seed(random_seed, version=2)
    conn = sqlite3.connect(dbfile)
    conn.execute('''CREATE TABLE IF NOT EXISTS MockupPatient
                        ( PatientId STRING PRIMARY KEY
                        , PatientFullName STRING
                        , PatientBirthDate DATETIME
                        , PatientPrimaryOncologist STRING
                        , PatientDepartment STRING
                        , TreatmentStartName STRING
                        , TreatmentStartDate DATETIME
                        , BlockingTaskName STRING
                        , BlockingTaskDueDate DATETIME
                        , BlockingTaskSuggestedDuration INT
                        , BlockingTaskStatus STRING
                        , BlockingTaskOwner STRING
                        )'''
                 )

    # Define the possible values for each column
    patient_names = [
        'SpongeBob SquarePants',
        'Patrick Star',
        'Squidward Tentacles',
        'Sandy Cheeks',
        'Mr. Krabs',
        'Plankton',
        'Karen Plankton',
        'Gary the Snail',
        'Mrs. Puff',
        'Pearl Krabs',
        'Larry the Lobster',
        'Mermaid Man',
        'Barnacle Boy',
        'Flying Dutchman',
        'Patchy the Pirate',
        'Potty the Parrot',
        'King Neptune',
        'Bubble Bass',
        'Man Ray',
        'Dirty Bubble']
    patient_ids = ['z_64042196', 'z_79852651', 'z_54179436', 'z_91106890', 'z_56177642', 'z_63937026', 'z_74561971',
                   'z_81285467', 'z_65970339', 'z_75928470', 'z_60056431', 'z_61814035', 'z_47237856', 'z_46988348',
                   'z_74208731', 'z_13123810', 'z_26576932', 'z_82975358', 'z_96601667', 'z_83212000']
    departments = ['MÖR', 'Q21']
    oncologists = ['Meredith Grey', 'Derek Shepherd', 'Miranda Bailey', 'Richard Webber']
    physicists = ['Marie Curie', 'Henri Becquerel', 'Ernest Rutherford', 'Irene Joliot-Curie']
    nurses = ['Florence Nightingale', 'Clara Barton', 'Mary Eliza Mahoney', 'Dorothea Dix']
    medical_procedures = ['Blood test', 'Physical exam', 'X-ray', 'CT scan']
    blocking_tasks = ["Filing paperwork", "Data entry", "Organizing files", "Proofreading documents", "Taking inventory"]
    blocking_task_statuses = ['Open', 'In Progress']
    blocking_durations = [10, 15, 30, 60]

    # Define the date range for treatment start dates

    # Generate the mockup data
    rows = []
    for i in range(len(patient_names)):
        # Generate random values for each column
        patient_id = patient_ids[i % len(patient_ids)]
        patient_name = patient_names[i % len(patient_names)]
        patient_birthdate = datetime.now() - timedelta(days=random.randint(365*20, 365*80))
        oncologist = random.choice(oncologists)
        department = random.choice(departments)
        treatment_start_name = random.choice(medical_procedures)
        treatment_start_date = datetime.now() + timedelta(minutes=random.randint(60, 60*24*7))
        blocking_task_name = random.choice(blocking_tasks)
        blocking_task_due_date = treatment_start_date - timedelta(hours=random.randint(5, 168))
        blocking_task_suggested_duration = random.choice(blocking_durations)
        blocking_task_status = random.choice(blocking_task_statuses)
        blocking_task_owner = random.choice(oncologists+physicists+nurses)

        # Insert the row into the database
        row = (patient_id, patient_name, patient_birthdate, oncologist, department, treatment_start_name,
               treatment_start_date, blocking_task_name, blocking_task_due_date, blocking_task_suggested_duration,
               blocking_task_status, blocking_task_owner)
        rows.append(row)

    conn.executemany('''INSERT OR IGNORE INTO MockupPatient (PatientId, PatientFullName, PatientBirthDate, PatientPrimaryOncologist,
                     PatientDepartment, TreatmentStartName, TreatmentStartDate, BlockingTaskName, BlockingTaskDueDate,
                     BlockingTaskSuggestedDuration, BlockingTaskStatus, BlockingTaskOwner)
                     VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', rows)

    conn.commit()
    conn.close()
    random.seed(None, version=2)
