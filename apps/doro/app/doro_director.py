from fastapi import FastAPI
from doro.app.doro_reader import doro_reader

app = FastAPI(title="doro (director)")

class doro_director:
    def __init__(self):
        pass
    
    def get_data(self):
        df = pd.read.csv(_CSV_PATH)

        return df = pd.read_csv(_CSV_PATH)