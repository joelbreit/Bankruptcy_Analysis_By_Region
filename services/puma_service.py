import csv
from enum import Enum

from models.PUMA import *

def get_puma_data(filepath, year):

    dictionary_of_pumas = dict()

    with open(filepath, encoding='utf-8', errors='ignore') as csvfile:
        file_reader = csv.reader(csvfile)
        line = next(file_reader)

        class Column(Enum):
            PUMA = line.index('puma12')
            STATE_CODE = line.index('state')
            STATE = line.index('stab')
            NAME = line.index('PUMAname')

        next(file_reader) # skip extra header line

        try:
            while True:
                row = next(file_reader)
                id = row[Column.STATE_CODE.value] + row[Column.PUMA.value] + year
                puma = PUMA(id)
                puma.name = row[Column.NAME.value]
                puma.state = row[Column.STATE.value]
                puma.year = year
                dictionary_of_pumas[id] = puma
        except StopIteration:
            pass

    return dictionary_of_pumas