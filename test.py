import requests 

BASE = "http://127.0.0.1:5000"


response = requests.post(BASE+"/train",{"text":"This is a test audio","audio_device":"default"})
print(response.json())



