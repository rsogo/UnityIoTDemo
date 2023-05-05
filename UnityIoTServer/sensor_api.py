from fastapi import FastAPI
from typing import Optional

app = FastAPI()

# メモリ上に保存するデータを格納するための辞書
sensor_data = {}

@app.post("/sensor/{id}")
async def update_sensor_data(id: str, data: float):
    """
    M5Stackからのデータ送信API
    センサーIDとそのセンサーからのデータを受け取り、辞書に格納する
    """
    sensor_data[id] = data
    return {"message": f"Sensor data for ID {id} updated successfully."}

@app.get("/sensor/{id}")
async def read_sensor_data(id: str):
    """
    Unityアプリからのデータ取得API
    センサーIDを受け取り、そのセンサーのデータを返す
    """
    data = sensor_data.get(id, None)
    if data is not None:
        return {"sensor_id": id, "data": data}
    else:
        return {"message": f"Sensor data for ID {id} not found."}

@app.get("/sensor")
async def read_all_sensor_data():
    """
    全センサーデータ取得API
    現在保持している全てのセンサーデータを返す
    """
    return sensor_data
