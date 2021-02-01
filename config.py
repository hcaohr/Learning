import os
from pathlib import Path


class CONST:
    try:
        PROJECT_PATH = Path(os.path.dirname(__file__))

        CSV_PATH = str(PROJECT_PATH / Path('data/csv/example.csv'))

        REPORT_PATH = str(PROJECT_PATH / Path('reports'))

    except Exception as msg:
        print(msg)
