import cv2
import requests
import json
import base64


base_url = 'http://127.0.0.1:8000/'

url = base_url + 'process_frames'

content_type = 'application/json'
headers = {'content-type':content_type}

path = 'image.jpg'

img = cv2.imread(path)

_, img_encoded = cv2.imencode('.jpg', img)
str_img = base64.b64encode(img_encoded).decode()

payload = {"frame": str_img}

response = requests.post(url, data=json.dumps(payload), headers=headers)

print(json.loads(response.text))


