from fastapi import FastAPI
from pydantic import BaseModel
import logging

app = FastAPI()

# メモリ上に保存するデータを格納するための辞書
sensor_data_store = {}

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class SensorData(BaseModel):
    sensor_data: float

@app.post("/sensor/{id}")
async def update_sensor_data(id: int, sensor_data: SensorData):

    """
    M5Stackからのデータ送信API
    センサーIDとそのセンサーからのデータを受け取り、辞書に格納する
    """
    global sensor_data_store
    sensor_data_store[id] = sensor_data

    logging.info(sensor_data_store);
    return {"message": f"Sensor data updated successfully."}

@app.get("/sensor/{id}")
async def read_sensor_data(id: int) -> SensorData:
    """
    Unityアプリからのデータ取得API
    センサーIDを受け取り、そのセンサーのデータを返す
    """
    logging.info(sensor_data_store);
    data = sensor_data_store.get(id, None)
    logging.info(data);
    if data is not None:
        return {"sensor_id": id, "data": data}
    else:
        return {"message": f"Sensor data for ID {id} not found."}

@app.get("/sensor")
async def read_all_sensor_data() -> dict:
    """
    全センサーデータ取得API
    現在保持している全てのセンサーデータを返す
    """
    return sensor_data_store
