import csv
import locale
import sqlite3

with open("DTGeneExpression.csv") as csvfile:
    expreader = csv.reader(csvfile, delimiter=";", quotechar='"')
    locations = []
    num_of_locations = 0
    genes = []
    db = sqlite3.connect('db.sqlite3')
    cursor = db.cursor()
    res = cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='webquery_gene';")
    if len(res.fetchone()) == 0:
        print("Cannot file table 'gene' in database")
    res = cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='webquery_location';")
    if len(res.fetchone()) == 0:
        print("Cannot file table 'location' in database")
    res = cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='webquery_expression';")
    if len(res.fetchone()) == 0:
        print("Cannot file table 'expression' in database")
    for row in expreader:
        if len(locations) == 0:
            # The first line contains location names
            assert len(row) > 1
            assert not bool(row[0])
            num_of_locations = len(row) - 1
            del row[0]
            for name in row:
                locations.append(name)
                cursor.execute("INSERT INTO webquery_location(name) VALUES(\"" + name + "\");")
            db.commit()
        else:
            assert len(row) == num_of_locations + 1
            gene_name = row.pop(0)
            genes.append(gene_name)
            cursor.execute("INSERT INTO webquery_gene(name) VALUES(\"" + gene_name + "\");")
            db.commit()
            exps = []
            for cell in row:
                cell = cell.replace(',', '.')
                expvalue = locale.atof(cell)
                exps.append(expvalue)
            for i in range(0, num_of_locations):
                location = locations[i]
                expression = exps[i]
                stmt = "INSERT INTO webquery_expression(gene_id, location_id, express) VALUES(" + \
                       "(SELECT id FROM webquery_gene WHERE name == \"" + gene_name + "\"), " + \
                       "(SELECT id FROM webquery_location WHERE name = \"" + location + "\"), " + \
                       str(expression) + ");"
                cursor.execute(stmt)
            db.commit()
            ngenes = len(genes)
            if ngenes % 10 == 0:
                print("Processed gene #" + str(ngenes) + " :" + gene_name)
    cursor.close()
