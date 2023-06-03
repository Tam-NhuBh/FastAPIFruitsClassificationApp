from fastapi import APIRouter, Response, Depends
from fastapi.responses import JSONResponse
import cv2

from api.home.request.home import ImageResuest
from app.home.services.home import HomeService

home_router = APIRouter()

import base64
import numpy as np
@home_router.get("/health")
async def home():
    return Response(status_code=200)
homeServive = HomeService()
@home_router.post("/images")
async def home(image: ImageResuest):
    print()
    if not image:
        return JSONResponse(content={"error": "Not data"}, status_code=200)
    try:
        decoded_data = base64.b64decode(image.stringImage)
        np_data = np.fromstring(decoded_data, np.uint8)
        image = cv2.imdecode(np_data, cv2.IMREAD_UNCHANGED)
        image = cv2.cvtColor(image, cv2.COLOR_RGBA2RGB)
        cv2.imwrite("D:\\Nam 3\\HK2\\Mobile\\Final\\web\\image.jpg", image) 
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        lable = await  homeServive.detect(image)
        print(lable)
        return JSONResponse(content={"result": str(lable)}, status_code=200)
    except Exception as ex:
        print(str(ex))
        return JSONResponse(content={"error": str(ex)}, status_code=400)