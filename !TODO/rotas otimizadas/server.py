from sanic import Sanic, response
import json
import os
import aiofiles
import base64

app = Sanic(__name__)
app.config.LOG_LEVEL = "DEBUG"

# Static files
app.static('/static', './static')

# Routes
@app.route("/")
async def index(request):
    return await response.file("templates/interface_rota.html")

# API
@app.route("/save", methods=["POST"])
async def save(request):
    data = request.json
    file_path = os.path.join("static/trajetoria", "points.json")  

    with open(file_path, "w") as file:
        json.dump(data, file)

    return response.json({"message": "File saved successfully."}, status=200)

@app.route("/upload_image", methods=["POST"])
async def upload_image(request):
    data = request.json
    image_data = data['image'].split(",")[1]
    image_bytes = base64.b64decode(image_data)

    file_path = os.path.join("static/images", "user_image.png")
    async with aiofiles.open(file_path, 'wb') as outfile:
        await outfile.write(image_bytes)

    return response.json({"message": "Image saved successfully."}, status=200)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
