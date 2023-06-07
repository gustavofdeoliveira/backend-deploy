from sanic import Sanic, Request, Websocket
from sanic.response import json
import cv2 as cv
from ultralytics import YOLO
import asyncio

app = Sanic(__name__)
model = YOLO('./best.pt')
cap = cv.VideoCapture(0)
clients = []

@app.websocket("/video_feed")
async def video_feed(request: Request, ws: Websocket):
    clients.append(ws)
    try:
        while True:
            success, frame = cap.read()
            if not success:
                cap.release()
                break
            else:
                result = model.predict(frame, conf=0.6)
                _, buffer = cv.imencode('.jpg', cv.flip(result[0].plot(), 1))
                frame = buffer.tobytes()
    
                tasks = []
                for client in clients:
                    tasks.append(asyncio.create_task(client.send(frame)))
    
                await asyncio.gather(*tasks)
    except Exception as err:
        print(err)
    finally:
        clients.remove(ws)

@app.route('/')
async def index(request):
    return json('Video feed is running on /video_feed')

if __name__ == "__main__":
    app.run(debug=True, host="10.128.73.158", port=8080)