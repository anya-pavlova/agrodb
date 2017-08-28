# -*- coding: utf-8 -*-

ReservedFields = 3
FieldCounter = ReservedFields

def get_index():
    global FieldCounter
    res = FieldCounter
    FieldCounter += 1
    return res

DataSchema = (
    ('meancrop',    get_index(), 'REAL', 'урожай: среднее значение'),
    ('cormeancrop', get_index(), 'REAL', 'урожай: исправленное среднее значение'),
    ('devfb',       get_index(), 'REAL', 'отклоенение от лучшего стандарта'),
    ('rank',        get_index(), 'REAL', 'ранг'),
    ('wet',         get_index(), 'REAL', 'влажность'),
    ('stofrep1',    get_index(), 'REAL', 'дней от посева до цветения: 1 повтор'),
    ('stofrep2',    get_index(), 'REAL', 'дней от посева до цветения: 2 повтор'),
    ('hrep1',       get_index(), 'REAL', 'высота растений: 1 повт.'),
    ('hrep2',       get_index(), 'REAL', 'высота растений: 2 повт.'),
    ('disbasrot',   get_index(), 'REAL', 'Болезни% прикорневая гниль'),
    ('diswhrot',    get_index(), 'REAL', 'болезни % белая гниль'),
    ('discrrot',    get_index(), 'REAL', 'болезни % серая гниль'),
    ('evrustrep1',  get_index(), 'REAL', 'оценка ржавчина: 1 повт.'),
    ('evrustrep2',  get_index(), 'REAL', 'оценка ржавчина: 2 повт.'),
    ('rstgrrep1',   get_index(), 'REAL', 'остался зел: 1 повт.'),
    ('rstgrrep2',   get_index(), 'REAL', 'остался зел: 2 повт.'),
    ('oilcropperc', get_index(), 'REAL', 'урожай масла в %'),
    ('oilcropcwt',  get_index(), 'REAL', 'Урожай масла в ц/га'),
    ('oleicacid',   get_index(), 'REAL', 'олеиновая кислота в %'),
    ('comment',     get_index(), 'TEXT', 'комментарии')
)

# Keeps infomation about search options.
class QueryInfo:
    def __init__(self, experiment, hybrid):
        self.experiment = experiment
        self.hybrid = hybrid
        self.data = [] # List of other fileds

    def mark(self, field):
        if self.data.count(field) > 0:
            return
        for item in DataSchema:
            if (item[0] == field):
                self.data.append(field)
                return

# Info about hybride.
class Item:
    def __init__(self, hybrid):
        self.values = [hybrid]

# Search result.
class Result:
    def __init__(self, experiment):
        self.experiment = experiment
        self.records = []
        self.query = None

    def set_query(self, query):
        self.query = query

