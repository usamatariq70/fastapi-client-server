from fastapi import FastAPI, Request
from pydantic import BaseModel
import base64
import json
import cv2
import numpy as np

app = FastAPI()

class Img(BaseModel):
    frame:str
    
@app.post("/process_frames")
async def process_frames(request:Request, img:Img):
    
    img_org = base64.b64decode(img.frame)
    img_np = np.frombuffer(img_org, dtype=np.uint8)
    img = cv2.imdecode(img_np, cv2.IMREAD_COLOR)
    
    response = {'message': 'image received. size={}x{}'.format(img.shape[1], img.shape[0])}
    
    return response