import json
from fastapi import FastAPI
import pandas as pd
from pathlib import Path

_DATA_DIR = Path(__file__).resolve().parent
_CSV_PATH = _DATA_DIR / "app" / "한국도로공사_교통사고통계_20241231.csv"

app = FastAPI(title="Monenon-doro_Data")

class DoroDirector:
    def __init__(self):
        pass
    
    def get_data(self):
        # 한글 깨짐 방지 인코딩 추가
        df = pd.read_csv(_CSV_PATH, encoding='cp949')
        # 인덱스 1번 행만 반환
        return df.iloc[[1]].astype(object).where(df.iloc[[1]].notna(), None)

@app.get("/")
def read_root():
    return {"message": "도로공사 데이터 서버 작동 중"}

@app.get("/doro/data")
def get_doro_statistics():
    director = DoroDirector()
    result_df = director.get_data()
    return result_df.to_dict(orient="records")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)