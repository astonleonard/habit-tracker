import requests
from datetime import datetime
import os

pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = os.getenv("PIXALA TOKEN")
USERNAME = "aston"
KM = input("How many kilometers did you cycle today? ")

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
GRAPH_ID = os.getenv("GRAPH_ID")

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ichou"
}

header = {
    "X-USER-TOKEN": TOKEN
}

pixela_creation_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

yesterday = datetime(year=2022, month=5, day=1).strftime("%Y%m%d")
today = datetime.now().strftime("%Y%m%d")

pixela_updated_endpoint = f"{pixela_creation_endpoint}/{today}"
pixela_creation_config = {
    "date": f"{yesterday}",
    "quantity": KM
}
pixela_updated_config = {
    "quantity": KM
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=header)
# print(response.text)

# response = requests.post(url=pixela_creation_endpoint, json=pixela_creation_config, headers=header)
# print(response.text)

response = requests.put(url=pixela_updated_endpoint, json=pixela_creation_config, headers=header)
print(response.text)

pixela_delete_endpoint = f"{pixela_creation_endpoint}/{yesterday}"

# response = requests.delete(url=pixela_delete_endpoint, headers=header)
# print(response.text)
