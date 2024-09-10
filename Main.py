import requests
import time

start_time = time.time()
print("iniciar")

response = requests.get("http://127.0.0.1:8000/json/")
print(response)

end_time = time.time()

print(f"El tiempo ejecutandose fue de: {end_time - start_time}")
