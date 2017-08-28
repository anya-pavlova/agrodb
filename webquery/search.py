# -*- coding: utf-8 -*-
import sqlite3
from .result import Result, Item, DataSchema

def get_average_expression(result, species, gene_name, local_name):
    # loc_codition filters results by location name
    if local_name:
        loc_condition = "AND webquery_location.name LIKE \"%" + local_name + "%\""
    else:
        loc_condition = ""

    if species:
        spec_condition = "AND webquery_location.name LIKE \"%" + species + "%\""
    else:
        spec_condition = ""

    db = sqlite3.connect('db.sqlite3')
    cursor = db.cursor()

    if local_name:
        stmt = "SELECT webquery_gene.name, AVG(webquery_expression.express) \
                    FROM webquery_expression \
                        INNER JOIN webquery_location ON webquery_expression.location_id = webquery_location.id \
                        INNER JOIN webquery_gene ON webquery_expression.gene_id = webquery_gene.id \
                    WHERE webquery_gene.name = \"" + gene_name + "\" " + \
                          loc_condition + spec_condition + "\
                    GROUP BY webquery_gene.id;"
        res = cursor.execute(stmt)
        for row in res:
            result.species.append(Item(species, row[1]))



def find_gene(experiment, hybrid):
    result = Result(experiment, hybrid)

    get_average_expression(result, "HUMAN", gene_name, local_name)
    get_average_expression(result, "GIBBON", gene_name, local_name)
    get_average_expression(result, "Chimpanzee", gene_name, local_name)
    get_average_expression(result, "Gorilla", gene_name, local_name)

    db = sqlite3.connect('db.sqlite3')
    cursor = db.cursor()

    if not local_name:
        res = cursor.execute("SELECT webquery_location.name AS Location, webquery_expression.express AS Expression\
                              FROM webquery_expression \
                                   INNER JOIN webquery_location ON webquery_expression.location_id = webquery_location.id \
                                   INNER JOIN webquery_gene ON webquery_expression.gene_id = webquery_gene.id \
                              WHERE webquery_gene.name = \"" + gene_name + "\";")
    else:
        res = cursor.execute("SELECT webquery_location.name AS Location, webquery_expression.express AS Expression\
                            FROM webquery_expression \
                                 INNER JOIN webquery_location ON webquery_expression.location_id = webquery_location.id \
                                 INNER JOIN webquery_gene ON webquery_expression.gene_id = webquery_gene.id \
                            WHERE webquery_gene.name = \"" + gene_name + "\" AND \
                                  webquery_location.name LIKE \"" + "%" + local_name + "%" + "\";")
    for row in res:
        result.expressions.append(Item(row[0], row[1]))


    return result

def find_records(experiment, hybrid, options):
    db = sqlite3.connect('db.sqlite3')
    cursor = db.cursor()

    stmt = "SELECT hybrid.name"
    for item in DataSchema:
        if options.count(item[0]):
            stmt += ", data."
            stmt +=  item[0]
    stmt += " FROM data INNER JOIN experiment ON data.experiment = experiment.id \
                       INNER JOIN hybrid ON data.hybrid = hybrid.id \
             WHERE experiment.name = \"" + experiment + "\""
    if hybrid:
        stmt += " AND hybrid.name = \"" + hybrid + "\""
    stmt += ";"

    result = Result(experiment)
    res = cursor.execute(stmt)
    for row in res:
        row_item = Item(row[0])
        cnt = 1
        for item in DataSchema:
            if options.count(item[0]) > 0:
                row_item.values.append(row[cnt])
                cnt += 1
        result.records.append(row_item)

    return result

def get_all_experiments():
    db = sqlite3.connect('db.sqlite3')
    cursor = db.cursor()
    res = cursor.execute("SELECT name FROM experiment;")
    result = []
    for row in res:
        result.append((str(row[0]), str(row[0])))
    return result

def get_all_hybrids():
    db = sqlite3.connect('db.sqlite3')
    cursor = db.cursor()
    res = cursor.execute("SELECT name FROM hybrid;")
    result = []
    for row in res:
        result.append((row[0], row[0]))
    return result
