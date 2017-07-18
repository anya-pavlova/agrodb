import csv
import sqlite3
from webquery.result import DataSchema


def fix_float(x):
    if isinstance(x, str):
        if x.count(',') == 1:
            return x.replace(',', '.')
    return x

def get_as_string(x):
    if x == None:
        return "NULL"
    if isinstance(x, float):
        return "%f" % x
    if x == "":
        return "NULL"
    return str(x)


with open("SFVoronezh16.csv") as csvfile:
    agroreader = csv.reader(csvfile, delimiter=";", quotechar='"')

    # TODO: get from file name
    exp_name = 'SFVoronezh16'
    
    db = sqlite3.connect('db.sqlite3')
    cursor = db.cursor()

    # Check if necessarary tables exist, if not, create them.

    res = cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='hybrid';")
    row = res.fetchone()
    if not row or len(row) == 0:
        res = cursor.execute(
            'CREATE TABLE hybrid '
            ' (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,'
            '  name TEXT NOT NULL'
            ');')
        db.commit()
        print("Cannot find table 'hybrid' in database")
    
    res = cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='experiment';")
    row = res.fetchone()
    if not row or len(row) == 0:
        res = cursor.execute(
            'CREATE TABLE experiment'
            ' (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,'
            '  name TEXT NOT NULL'
            ');')
        db.commit()
        print("Cannot find table 'experiment' in database")

    res = cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='data';")
    row = res.fetchone()
    if not row or len(row) == 0:
        stmt = 'CREATE TABLE data' \
               ' (id INTEGER PRIMARY KEY AUTOINCREMENT,' \
               '  hybrid INTEGER NOT NULL,' \
               '  experiment INTEGER NOT NULL'
        for schema_item in DataSchema:
            stmt += (', ' + schema_item[0] + ' ' + schema_item[2])
        stmt += ' );'
        res = cursor.execute(stmt)
        db.commit()
        print("Cannot find table 'experiment' in database")
            # Read csv file and put its records to the database.

    rowcnt = 0  # Counts records read fron csv file.
    for rec in agroreader:
        if rowcnt == 0:
            # The first line contains column names
            assert len(rec) > 1
        else:
            data = {}
            for item in DataSchema:
                data[item[0]] = None

            # Get hybrid id.
            hybrid_name = rec[1]
        
            res = cursor.execute("SELECT id FROM hybrid WHERE name = \"" + hybrid_name + "\";")
            row = res.fetchone()
            if not row or len(row) == 0:
                cursor.execute("INSERT INTO hybrid(name) VALUES(\"" + hybrid_name + "\");")
                db.commit()
            
            res = cursor.execute("SELECT id FROM hybrid WHERE name = \"" + hybrid_name + "\";")
            row = res.fetchone()
            assert row and len(row) != 0
            hybrid_id = row[0]
        
            # Get experiment id.
            res = cursor.execute("SELECT id FROM experiment WHERE name = \"" + exp_name + "\";")
            row = res.fetchone()
            if not row or len(row) == 0:
                cursor.execute("INSERT INTO experiment(name) VALUES(\"" + exp_name + "\");")
                db.commit()

            res = cursor.execute("SELECT id FROM experiment WHERE name = \"" + exp_name + "\";")
            row = res.fetchone()
            assert row and len(row) != 0
            exp_id = row[0]

            for item in DataSchema:
                item_pos = item[1] - 1
                if item_pos < len(rec):
                    if item[2] == 'REAL':
                        data[item[0]] = fix_float(rec[item_pos])
                    else:
                        data[item[0]] = rec[item_pos]

            # Prepare data about this experiment.
            res = cursor.execute("SELECT id FROM data WHERE hybrid = " + str(hybrid_id) +
                                 " AND experiment = " + str(exp_id) + ";")
            row = res.fetchone()
            if row and len(row) > 0:
                # such record already exists, update it
                pass
            else:
                # insert new record
                stmt = "INSERT INTO data(experiment, hybrid"
                for item in DataSchema:
                    stmt += ", "
                    stmt += item[0]
                stmt += ")  VALUES(" + \
                    get_as_string(exp_id) + ", " + \
                    get_as_string(hybrid_id)
                for item in DataSchema:
                    stmt += ", "
                    stmt += get_as_string(data[item[0]])
                stmt += ");"
                cursor.execute(stmt)
                db.commit()

        rowcnt += 1
