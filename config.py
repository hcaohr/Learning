import os
from pathlib import Path


class CONST:
    try:
        PROJECT_PATH = Path(os.path.dirname(__file__))
        DATAPATH = str(PROJECT_PATH / Path('data.yml'))
        DatPATH = str(PROJECT_PATH / Path('test_in_theaters.yml'))

    except Exception as msg:
        print(msg)